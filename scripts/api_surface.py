#!/usr/bin/env python3
"""Record the SDK's public surface, and fail when anything leaves it.

The release gate is `oasdiff`, which compares the schema. What we publish is a
client generated from that schema, and the two have different notions of a
breaking change. Renaming a component schema, changing an `operationId`, moving
an operation to a different tag, renaming a path parameter and inlining a `$ref`
are all `info` to oasdiff — nothing on the wire changes — while each one renames
or deletes something a consumer imports:

    ImportError: cannot import name 'SeverityV1' from 'incident_io.models'
    TypeError: sync() got an unexpected keyword argument 'id'

So this reads the generated package instead of the schema, writes the surface to
a file we commit, and on the next release fails if any line disappeared.
Additions are fine; removals are not.

    python scripts/api_surface.py write incident_io api-surface.txt
    python scripts/api_surface.py check incident_io api-surface.txt

Run against the installed wheel, so it describes what consumers get.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
import sys
from pathlib import Path

ENTRY_POINTS = ("sync_detailed", "sync", "asyncio_detailed", "asyncio")


def endpoint_lines(package) -> list[str]:
    """One line per endpoint entry point, naming its keyword parameters.

    Catches an operation being renamed or retagged (the module path moves) and a
    path or query parameter being renamed (the parameter list changes).
    """
    lines = []
    api = importlib.import_module(f"{package.__name__}.api")
    for module in pkgutil.walk_packages(api.__path__, f"{api.__name__}."):
        if module.ispkg:
            continue
        imported = importlib.import_module(module.name)
        for name in ENTRY_POINTS:
            function = getattr(imported, name, None)
            if function is None:
                continue
            parameters = sorted(inspect.signature(function).parameters)
            lines.append(f"endpoint {module.name}.{name}({', '.join(parameters)})")
    return lines


def model_lines(package) -> list[str]:
    """One line per exported model, naming its fields or enum members.

    Catches a schema being renamed or inlined (the class leaves `__all__`), a
    response property being removed, a required property being added, and an
    enum value being removed — none of which oasdiff rates as breaking.
    """
    lines = []
    models = importlib.import_module(f"{package.__name__}.models")
    for name in sorted(getattr(models, "__all__", [])):
        obj = getattr(models, name, None)
        if obj is None:
            lines.append(f"model {name} MISSING")
            continue

        members = getattr(obj, "__members__", None)
        if members is not None:  # an enum
            lines.append(f"enum {name}({', '.join(sorted(members))})")
            continue

        fields = getattr(obj, "__attrs_attrs__", None)
        if fields is not None:
            required = sorted(f.name for f in fields if f.default is inspect.Parameter.empty)
            optional = sorted(f.name for f in fields if f.default is not inspect.Parameter.empty)
            lines.append(f"model {name}(required: {', '.join(required)} | optional: {', '.join(optional)})")
            continue

        lines.append(f"model {name}")
    return lines


def surface(package_name: str) -> list[str]:
    package = importlib.import_module(package_name)
    return sorted(endpoint_lines(package) + model_lines(package))


def check(current: list[str], recorded_path: Path) -> int:
    if not recorded_path.exists():
        sys.exit(f"{recorded_path} does not exist. Run the write command to create it.")

    recorded = recorded_path.read_text().splitlines()
    removed = sorted(set(recorded) - set(current))
    added = sorted(set(current) - set(recorded))

    for line in added:
        print(f"  + {line}")

    if not removed:
        print(f"surface: {len(current)} entries, {len(added)} added, nothing removed")
        return 0

    print(f"\n{len(removed)} entries left the public surface:", file=sys.stderr)
    for line in removed[:40]:
        print(f"  - {line}", file=sys.stderr)
    if len(removed) > 40:
        print(f"  ... and {len(removed) - 40} more", file=sys.stderr)
    print(
        "\nConsumers import these by name, so removing one breaks them at import "
        "or call time even when the wire contract is unchanged. This needs a major "
        "version, not the automatic minor bump.",
        file=sys.stderr,
    )
    return 1


def main(argv: list[str]) -> int:
    if len(argv) != 4 or argv[1] not in ("write", "check"):
        print(f"usage: {argv[0]} <write|check> <package> <surface-file>", file=sys.stderr)
        return 2

    _, command, package_name, path = argv
    current = surface(package_name)

    if command == "write":
        Path(path).write_text("\n".join(current) + "\n")
        print(f"surface: wrote {len(current)} entries to {path}")
        return 0

    return check(current, Path(path))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
