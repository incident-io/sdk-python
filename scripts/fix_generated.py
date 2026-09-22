#!/usr/bin/env python3
"""Repair defects in the generated client that the generator will not.

Each fix names the exact text it replaces and fails if that text is missing, so
an upstream generator change surfaces as a failed release rather than a silently
skipped patch. Report these upstream; delete a fix here when it lands there.

Fixes:

1. The context-manager signatures don't type-check. `__exit__` and `__aexit__`
   take `*args: object` and splat that into httpx's, which is typed for the
   three specific arguments. Harmless at runtime, but the package ships
   `py.typed`, so it has to check cleanly.

2. Object-valued query parameters lose their name. The API's filters are
   `created_at[gte]=2024-05-01`: a parameter whose value is an object, keyed
   by operator. The generator hoists that object's keys to the top level
   instead, sending `gte=2024-05-01`, so the server sees a parameter it does
   not know and ignores the filter.

   Worse, the hoisted keys collide. `created_at[gte]` and `updated_at[gte]`
   both become `gte`, and the second `params.update()` overwrites the first,
   so one of the two filters vanishes with no error. A caller gets a 200 and
   the wrong rows.

   Some filters nest a second level, so the flattening recurses and lives in
   a `_query.py` written out beside the generated code — a comprehension at
   each call site cannot.

   The spec is the root cause — it declares these `type: object` with no
   `style`, so the OpenAPI default `style: form, explode: true` applies, and
   hoisting is the correct reading of that. But openapi-python-client ignores
   `style: deepObject` entirely (verified: byte-identical output with and
   without it), so fixing the spec would not fix this client. This patch
   stays either way.

3. Models accept positional arguments. attrs orders fields required-then-
   optional in schema order, and our schema emits properties alphabetically, so
   adding one optional field moves every positional argument after it. A caller
   writing `Payload(Status.FIRING, "disk full", "dedup-123")` silently sends
   that last value as a different field: no exception, no type error, no failed
   test, and oasdiff rates adding an optional property `info`, so it publishes
   automatically. Keyword-only turns that into a TypeError at the call site.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Only for the failure message; the real pin lives in the Makefile.
OPC_HINT = "(pinned in the Makefile)"

METHODS = ("get", "post", "put", "patch", "delete")


QUERY_HELPER = '''"""Query-string helpers added by scripts/fix_generated.py."""

from __future__ import annotations

from typing import Any


def flatten_deep_object(name: str, value: Any) -> dict[str, Any]:
    """Flatten an object-valued query parameter into bracketed keys.

    The API's filters are objects keyed by operator, and some nest a second
    level keyed by field ID:

        flatten_deep_object("created_at", {"gte": ["2024-05-01"]})
        -> {"created_at[gte]": ["2024-05-01"]}

        flatten_deep_object("custom_field", {"01ABC": {"one_of": ["x"]}})
        -> {"custom_field[01ABC][one_of]": ["x"]}

    See scripts/fix_generated.py for why the generated client needs this.
    """
    flattened: dict[str, Any] = {}

    for key, inner in value.items():
        bracketed = f"{name}[{key}]"
        if isinstance(inner, dict):
            flattened.update(flatten_deep_object(bracketed, inner))
        else:
            flattened[bracketed] = inner

    return flattened
'''

# `params.update(json_x)` is the hoist. The identifier after `json_` is the
# generator's `python_name` for the parameter, which is a lossy transform of
# the wire name — `createdAt` and `created-at` would both arrive here as
# `created_at`. So the wire name is read back from the schema rather than
# inferred from this, and a name that does not map is an error.
DEEP_OBJECT = re.compile(
    r"    if not isinstance\(json_(\w+), Unset\):\n        params\.update\(json_\1\)\n"
)

# Every api module carries this, byte-identical, from endpoint_module.py.jinja.
CLIENT_IMPORT = "from ...client import AuthenticatedClient, Client\n"
HELPER_IMPORT = "from ..._query import flatten_deep_object\n"


def object_query_parameters(spec_path: Path) -> tuple[dict[str, str], int]:
    """Object-valued query parameters, from the schema rather than the code.

    Returns the wire name for each `python_name` the generator will produce,
    and how many call sites there should be in total — a parameter shared by
    six endpoints is six of them.
    """
    document = json.loads(spec_path.read_text())

    names: dict[str, str] = {}
    expected = 0
    for item in document["paths"].values():
        for method, operation in item.items():
            if method not in METHODS or not isinstance(operation, dict):
                continue
            for parameter in operation.get("parameters", []):
                schema = parameter.get("schema") or {}
                if parameter.get("in") != "query" or schema.get("type") != "object":
                    continue
                # The generator's transform, for the shapes this schema uses.
                # Anything it does not cover fails the lookup below rather
                # than guessing.
                names[parameter["name"].replace("-", "_").lower()] = parameter["name"]
                expected += 1

    return names, expected


def fix_deep_object_params(package: Path, spec_path: Path) -> tuple[int, int, list[str]]:
    """Send `created_at[gte]=...` rather than hoisting `gte` to the top level.

    See fix 2 in the module docstring.

    Returns (call sites rewritten, call sites the schema expects, problems).
    The counts are compared rather than floored: a partial match ships the
    very bug this exists to fix, silently, on whichever filters it missed.
    """
    wire_names, expected = object_query_parameters(spec_path)
    problems: list[str] = []
    fixed = 0

    def rewrite(match: re.Match[str]) -> str:
        identifier = match.group(1)
        name = wire_names.get(identifier)
        if name is None:
            problems.append(
                f"no object query parameter in the schema maps to `json_{identifier}` "
                f"— the generator's python_name transform has diverged from the "
                f"wire name, so the filter would be sent under the wrong key"
            )
            return match.group(0)
        return (
            f"    if not isinstance(json_{identifier}, Unset):\n"
            f'        params.update(flatten_deep_object("{name}", json_{identifier}))\n'
        )

    for file in sorted(package.glob("api/*/*.py")):
        source = file.read_text()
        patched, count = DEEP_OBJECT.subn(rewrite, source)
        if not count:
            continue

        if CLIENT_IMPORT not in patched:
            problems.append(f"no import anchor in {file.name}; the helper is unreachable")
            continue

        # Relative, like every other import the generator writes into these
        # modules, all of which sit at the same depth.
        patched = patched.replace(CLIENT_IMPORT, HELPER_IMPORT + CLIENT_IMPORT, 1)
        file.write_text(patched)
        fixed += count

    if fixed:
        (package / "_query.py").write_text(QUERY_HELPER)

    return fixed, expected, problems


@dataclass(frozen=True)
class Fix:
    """A single replacement, applied to every file matching `glob`."""

    name: str
    glob: str
    old: str
    new: str


FIXES = (
    Fix(
        name="models take keyword arguments only",
        glob="models/*.py",
        old="@_attrs_define\n",
        new="@_attrs_define(kw_only=True)\n",
    ),
    Fix(
        name="__exit__ passes httpx the types it declares",
        glob="client.py",
        old=(
            "    def __exit__(self, *args: object, **kwargs: Any) -> None:\n"
            '        """Exit a context manager for internal httpx.Client (see httpx docs)"""\n'
            "        self.get_httpx_client().__exit__(*args, **kwargs)"
        ),
        new=(
            "    def __exit__(\n"
            "        self,\n"
            "        exc_type: type[BaseException] | None = None,\n"
            "        exc_value: BaseException | None = None,\n"
            "        traceback: TracebackType | None = None,\n"
            "    ) -> None:\n"
            '        """Exit a context manager for internal httpx.Client (see httpx docs)"""\n'
            "        self.get_httpx_client().__exit__(exc_type, exc_value, traceback)"
        ),
    ),
    Fix(
        name="__aexit__ passes httpx the types it declares",
        glob="client.py",
        old=(
            "    async def __aexit__(self, *args: object, **kwargs: Any) -> None:\n"
            '        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""\n'
            "        await self.get_async_httpx_client().__aexit__(*args, **kwargs)"
        ),
        new=(
            "    async def __aexit__(\n"
            "        self,\n"
            "        exc_type: type[BaseException] | None = None,\n"
            "        exc_value: BaseException | None = None,\n"
            "        traceback: TracebackType | None = None,\n"
            "    ) -> None:\n"
            '        """Exit a context manager for underlying httpx.AsyncClient (see httpx docs)"""\n'
            "        await self.get_async_httpx_client().__aexit__(exc_type, exc_value, traceback)"
        ),
    ),
    # The two above reference TracebackType, which the generated client
    # doesn't import.
    Fix(
        name="client.py imports TracebackType",
        glob="client.py",
        # Anchored on the newline: the real line is `from typing import Any,
        # Self`, and an unanchored match would insert mid-line.
        old="import ssl\n",
        new="import ssl\nfrom types import TracebackType\n",
    ),
)


def apply(fix: Fix, package: Path) -> int:
    """Replace every occurrence, returning how many."""
    applied = 0
    for file in sorted(package.glob(fix.glob)):
        source = file.read_text()
        occurrences = source.count(fix.old)
        if not occurrences:
            continue
        file.write_text(source.replace(fix.old, fix.new))
        applied += occurrences
    return applied


def main(package_path: str, spec_path: str) -> int:
    package = Path(package_path)
    unmatched = []

    name = "object query parameters keep their name"
    fixed, expected, problems = fix_deep_object_params(package, Path(spec_path))
    for problem in problems:
        unmatched.append(name)
        print(f"  {problem}", file=sys.stderr)
    if fixed != expected:
        unmatched.append(name)
        print(
            f"  rewrote {fixed} call sites, the schema has {expected}", file=sys.stderr
        )
    else:
        print(f"Fixed: {name} ({fixed} call sites)")

    for fix in FIXES:
        applied = apply(fix, package)
        if not applied:
            unmatched.append(fix.name)
            print(f"  no match: {fix.name}", file=sys.stderr)
        else:
            print(f"Fixed: {fix.name} ({applied} replacement{'s' if applied != 1 else ''})")

    if unmatched:
        # Either the generator fixed the defect upstream, or it changed its
        # output and the defect is back unpatched. Both need a human, and both
        # have to stop the release: publishing a wheel whose binary responses
        # are broken, or whose models silently accept positional arguments, is
        # worse than not publishing. The workflow turns this into an issue.
        print(
            f"\n{len(unmatched)} fix(es) matched nothing. Check whether "
            f"openapi-python-client {OPC_HINT} changed its output, or fixed "
            f"these upstream — in which case delete them here.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <package-dir> <openapi.json>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
