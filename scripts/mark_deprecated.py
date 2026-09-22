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

# sync() calls sync_detailed(), and both are wrapped, so a single user call
# would warn twice — the second time with a stacklevel pointing inside the SDK,
# which under -W error blames us for the user's call. This suppresses the inner
# warning. Module-level rather than thread-local because it is only ever set
# for the duration of one synchronous call frame.
_warning_in_progress = False


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        global _warning_in_progress
        if _warning_in_progress:
            return _fn(*args, **kwargs)
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        _warning_in_progress = True
        try:
            return _fn(*args, **kwargs)
        finally:
            _warning_in_progress = False

    return _wrapper


def _deprecated_async(_fn):
    # `async def`, so the result stays a coroutine function under
    # inspect.iscoroutinefunction. See this module's docstring.
    @_functools.wraps(_fn)
    async def _wrapper(*args, **kwargs):
        global _warning_in_progress
        if _warning_in_progress:
            return await _fn(*args, **kwargs)
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        _warning_in_progress = True
        try:
            return await _fn(*args, **kwargs)
        finally:
            _warning_in_progress = False

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
                found.add((method, normalise_path(path)))
    return found


def normalise_path(path: str) -> str:
    """Snake_case the parameter names in a path, the way the generator does.

    The schema is free to name a path parameter `followUpId` or `action-id`;
    the generated URL always says `follow_up_id`. Comparing the raw spec path
    against the generated one therefore misses those, and a miss fails the
    release. Only the parameter names are touched — the literal segments are
    already whatever the API serves.
    """

    def snake(match: re.Match[str]) -> str:
        name = match.group(1)
        name = re.sub(r"[-\s]+", "_", name)
        name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)
        return "{" + name.lower() + "}"

    return re.sub(r"\{([^}]+)\}", snake, path)


def operation_of(source: str) -> tuple[str, str] | None:
    """Read the (method, path) a generated module calls."""
    method = re.search(r'"method":\s*"([a-z]+)"', source)
    url = re.search(r'"url":\s*"([^"]+)"', source)
    if not method or not url:
        return None
    return method.group(1), url.group(1)


def mark(file: Path, method: str, path: str) -> bool:
    """Append the wrappers. True if the module ends up marked, including when
    it already was — otherwise a second run reports every operation as missing
    and blames the generator for it."""
    source = file.read_text()
    if MARKER in source:
        return True

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
