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

2. Models accept positional arguments. attrs orders fields required-then-
   optional in schema order, and our schema emits properties alphabetically, so
   adding one optional field moves every positional argument after it. A caller
   writing `Payload(Status.FIRING, "disk full", "dedup-123")` silently sends
   that last value as a different field: no exception, no type error, no failed
   test, and oasdiff rates adding an optional property `info`, so it publishes
   automatically. Keyword-only turns that into a TypeError at the call site.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

# Only for the failure message; the real pin lives in the Makefile.
OPC_HINT = "(pinned in the Makefile)"


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


def main(package_path: str) -> int:
    package = Path(package_path)
    unmatched = []

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
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <package-dir>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
