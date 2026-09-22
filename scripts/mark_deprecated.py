#!/usr/bin/env python3
"""Add deprecation warnings to the generated endpoint modules.

The generator ignores the schema's `deprecated` flag, so without this a caller
gets no warning that an endpoint is going away. sdk-go fills the same gap in
internal/postgen.

We find each module by the method and URL it calls, rather than guessing at the
generator's file naming, and append a wrapper rather than editing generated code
in place.

The async entry points need their own wrapper. Wrapping `async def` in a plain
`def` that returns the coroutine still awaits correctly, but the result is no
longer a coroutine function: `inspect.iscoroutinefunction` returns False, and
anything that branches on that — test frameworks, task runners, DI containers —
takes the wrong path.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SYNC_ENTRY_POINTS = ("sync_detailed", "sync")
ASYNC_ENTRY_POINTS = ("asyncio_detailed", "asyncio")
ENTRY_POINTS = SYNC_ENTRY_POINTS + ASYNC_ENTRY_POINTS
METHODS = ("get", "post", "put", "patch", "delete")
MARKER = "# --- deprecation markers added by scripts/mark_deprecated.py ---"

TEMPLATE = '''

{marker}
import functools as _functools  # noqa: E402
import warnings as _warnings  # noqa: E402

_DEPRECATION_MESSAGE = "{message}"


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        return _fn(*args, **kwargs)

    return _wrapper


def _deprecated_async(_fn):
    # `async def`, so the result stays a coroutine function under
    # inspect.iscoroutinefunction. See this module's docstring.
    @_functools.wraps(_fn)
    async def _wrapper(*args, **kwargs):
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        return await _fn(*args, **kwargs)

    return _wrapper

{rebinds}
'''


def deprecated_operations(spec: dict) -> set[tuple[str, str]]:
    """Return the (method, path) pairs the schema marks deprecated."""
    found = set()
    for path, item in (spec.get("paths") or {}).items():
        for method, operation in item.items():
            if method not in METHODS or not isinstance(operation, dict):
                continue
            if operation.get("deprecated"):
                found.add((method, path))
    return found


def operation_of(source: str) -> tuple[str, str] | None:
    """Read the (method, path) a generated module calls."""
    method = re.search(r'"method":\s*"([a-z]+)"', source)
    url = re.search(r'"url":\s*"([^"]+)"', source)
    if not method or not url:
        return None
    return method.group(1), url.group(1)


def mark(file: Path, method: str, path: str) -> bool:
    source = file.read_text()
    if MARKER in source:
        return False

    present = [name for name in ENTRY_POINTS if re.search(rf"^(?:async )?def {name}\(", source, re.M)]
    if not present:
        return False

    message = (
        f"{method.upper()} {path} is deprecated and will be removed. "
        "See https://api-docs.incident.io/ for the replacement."
    )
    rebinds = "\n".join(
        f"{name} = {'_deprecated_async' if name in ASYNC_ENTRY_POINTS else '_deprecated'}({name})"
        for name in present
    )
    file.write_text(source.rstrip("\n") + TEMPLATE.format(marker=MARKER, message=message, rebinds=rebinds))
    return True


def main(spec_path: str, package_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text())
    wanted = deprecated_operations(spec)
    if not wanted:
        print("No deprecated operations in schema; nothing to mark.")
        return 0

    marked: set[tuple[str, str]] = set()
    for file in sorted(Path(package_path).glob("api/*/*.py")):
        if file.name == "__init__.py":
            continue
        operation = operation_of(file.read_text())
        if operation in wanted and mark(file, *operation):
            marked.add(operation)

    print(f"Marked {len(marked)} of {len(wanted)} deprecated operations.")

    missed = wanted - marked
    if missed:
        # A deprecated operation with no module means the generator skipped it or
        # renamed something we rely on. Fail rather than ship a silent gap.
        for method, path in sorted(missed):
            print(f"  unmatched: {method.upper()} {path}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <openapi.json> <package-dir>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
