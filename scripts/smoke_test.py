#!/usr/bin/env python3
"""Check the SDK against the live API.

Importing the generated package proves it parses. It proves nothing about
whether a request actually works, which is what this covers: auth, URL
building, deserialising real responses, enum values the schema may not know
about, the pagination cursor, and the async path.

Read-only throughout. It never creates or changes anything.

    export INCIDENT_API_KEY=inc_...
    python scripts/smoke_test.py
"""

from __future__ import annotations

import asyncio
import os
import sys
import warnings

from incident_io import AuthenticatedClient
from incident_io.api.actions_v1 import actions_v1_list
from incident_io.api.incidents_v2 import incidents_v2_list
from incident_io.api.severities_v1 import severities_v1_list
from incident_io.models.incidents_list_result_v2 import IncidentsListResultV2
from incident_io.types import UNSET

BASE_URL = os.environ.get("INCIDENT_BASE_URL", "https://api.incident.io")

failures: list[str] = []


def check(name: str):
    """Run a check, record the failure, keep going."""

    def run(fn):
        try:
            detail = fn()
        except Exception as exc:  # noqa: BLE001 - we want every failure, not the first
            failures.append(name)
            print(f"FAIL  {name}\n        {type(exc).__name__}: {exc}")
        else:
            print(f"ok    {name}" + (f" — {detail}" if detail else ""))
        return fn

    return run


def main() -> int:
    token = os.environ.get("INCIDENT_API_KEY")
    if not token:
        print("Set INCIDENT_API_KEY first. A viewer-scoped key is enough.", file=sys.stderr)
        return 2

    client = AuthenticatedClient(base_url=BASE_URL, token=token)
    print(f"Testing against {BASE_URL}\n")

    @check("authenticates and returns 200")
    def _():
        response = severities_v1_list.sync_detailed(client=client)
        assert response.status_code == 200, f"got {response.status_code}: {response.content[:200]!r}"
        return f"{len(response.parsed.severities)} severities"

    @check("deserialises incidents, including enums and timestamps")
    def _():
        result = incidents_v2_list.sync(client=client, page_size=5)
        # Our error responses are typed, so a failure comes back as an
        # ErrorResponse rather than None or an exception.
        assert isinstance(result, IncidentsListResultV2), f"request failed: {result}"
        if not result.incidents:
            return "no incidents on this account, nothing to deserialise"
        first = result.incidents[0]
        # Touching these is the point: an enum value the schema doesn't list
        # raises here rather than at request time.
        return f"{first.reference}, status {first.incident_status.category}, created {first.created_at:%Y-%m-%d}"

    @check("pagination cursor round-trips")
    def _():
        first = incidents_v2_list.sync(client=client, page_size=1)
        assert isinstance(first, IncidentsListResultV2), f"request failed: {first}"
        if not first.incidents or first.pagination_meta.after is UNSET:
            return "fewer than two pages available, cursor not exercised"
        second = incidents_v2_list.sync(client=client, page_size=1, after=first.pagination_meta.after)
        assert second.incidents, "second page came back empty"
        assert second.incidents[0].id != first.incidents[0].id, "cursor returned the same incident"
        return f"page 1 {first.incidents[0].reference}, page 2 {second.incidents[0].reference}"

    @check("async client works")
    def _():
        async def go():
            return await severities_v1_list.asyncio_detailed(client=client)

        response = asyncio.run(go())
        assert response.status_code == 200, f"got {response.status_code}"
        return f"{len(response.parsed.severities)} severities"

    @check("deprecated endpoints warn")
    def _():
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            actions_v1_list.sync_detailed(client=client)
        messages = [str(w.message) for w in caught if w.category is DeprecationWarning]
        assert messages, "no DeprecationWarning was raised"
        return messages[0]

    @check("a bad key is reported, not swallowed")
    def _():
        bad = AuthenticatedClient(base_url=BASE_URL, token="definitely-not-a-key")
        response = severities_v1_list.sync_detailed(client=bad)
        assert response.status_code == 401, f"expected 401, got {response.status_code}"
        return "401 as expected"

    print()
    if failures:
        print(f"{len(failures)} check(s) failed: {', '.join(failures)}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
