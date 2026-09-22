"""Behavioural tests that need no API key.

`make verify` proves every generated module imports. These prove the parts we
are responsible for actually behave: the client we hand callers, and the
deprecation wrappers scripts/mark_deprecated.py appends after generation.

Requests are served by a local httpx transport rather than the real API, so
these run on a pull request. scripts/smoke_test.py covers the live API.
"""

from __future__ import annotations

import inspect
import warnings
from pathlib import Path

import httpx
import pytest

import incident_io
from incident_io import AuthenticatedClient
from incident_io.api.actions_v1 import actions_v1_list
from incident_io.api.pay_reports_v2 import pay_reports_v2_download
from incident_io.api.severities_v1 import severities_v1_list

SEVERITIES_BODY = {
    "severities": [
        {
            "id": "01FCNDV6P870EA6S7TK1DSYDG0",
            "name": "Minor",
            "description": "Issues with low impact.",
            "rank": 1,
            "created_at": "2021-08-17T13:28:57.801578Z",
            "updated_at": "2021-08-17T13:28:57.801578Z",
        }
    ]
}


def client_returning(status_code: int, body: dict, record: list[httpx.Request] | None = None):
    """An AuthenticatedClient wired to a stub transport instead of the network."""

    def handler(request: httpx.Request) -> httpx.Response:
        if record is not None:
            record.append(request)
        return httpx.Response(status_code, json=body)

    # Handed to the SDK as an httpx argument rather than via set_httpx_client,
    # which would replace the client the SDK builds and so bypass the base_url
    # and auth header these tests exist to check.
    return AuthenticatedClient(
        base_url="https://api.incident.io",
        token="test-key",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def test_sends_bearer_token_and_builds_the_url():
    requests: list[httpx.Request] = []
    client = client_returning(200, SEVERITIES_BODY, requests)

    severities_v1_list.sync_detailed(client=client)

    assert len(requests) == 1
    assert requests[0].headers["Authorization"] == "Bearer test-key"
    assert str(requests[0].url) == "https://api.incident.io/v1/severities"


def test_deserialises_a_response():
    client = client_returning(200, SEVERITIES_BODY)

    result = severities_v1_list.sync(client=client)

    assert len(result.severities) == 1
    assert result.severities[0].name == "Minor"
    # Dates come back parsed, not as strings.
    assert result.severities[0].created_at.year == 2021


def test_an_error_status_is_returned_not_raised():
    body = {
        "type": "validation_error",
        "status": 422,
        "request_id": "01FCNDV6P870EA6S7TK1DSYDG0",
        "errors": [{"code": "invalid", "message": "Something was wrong"}],
    }
    client = client_returning(422, body)

    response = severities_v1_list.sync_detailed(client=client)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_the_async_entry_point_works():
    client = client_returning(200, SEVERITIES_BODY)

    result = await severities_v1_list.asyncio(client=client)

    assert result.severities[0].name == "Minor"


# The generated package has no deprecated endpoints of its own — these cover
# what scripts/mark_deprecated.py adds afterwards, which is the part we own.


def test_a_deprecated_endpoint_warns():
    client = client_returning(200, {"actions": []})

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        actions_v1_list.sync_detailed(client=client)

    messages = [str(w.message) for w in caught if w.category is DeprecationWarning]
    assert messages, "no DeprecationWarning was raised"
    assert "GET /v1/actions" in messages[0]


def test_a_deprecated_endpoint_warns_once_not_twice():
    """sync() calls sync_detailed(), and both carry the wrapper. Without
    suppression the second warning points inside the SDK, which under
    -W error blames us for the caller's mistake."""
    client = client_returning(200, {"actions": []})

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        actions_v1_list.sync(client=client)

    deprecations = [w for w in caught if w.category is DeprecationWarning]
    assert len(deprecations) == 1, f"expected one warning, got {len(deprecations)}"
    assert "incident_io" not in deprecations[0].filename, (
        "the warning points inside the SDK rather than at the caller"
    )


def test_a_deprecated_async_endpoint_stays_a_coroutine_function():
    """Wrapping `async def` in a plain `def` would break anything that branches
    on inspect.iscoroutinefunction, even though `await` still works."""
    assert inspect.iscoroutinefunction(actions_v1_list.asyncio)
    assert inspect.iscoroutinefunction(actions_v1_list.asyncio_detailed)


@pytest.mark.asyncio
async def test_a_deprecated_async_endpoint_warns_and_still_returns():
    client = client_returning(200, {"actions": []})

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        response = await actions_v1_list.asyncio_detailed(client=client)

    assert response.status_code == 200
    assert [w for w in caught if w.category is DeprecationWarning]


def test_an_undeprecated_endpoint_does_not_warn():
    client = client_returning(200, SEVERITIES_BODY)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        severities_v1_list.sync_detailed(client=client)

    assert not [w for w in caught if w.category is DeprecationWarning]


def test_a_binary_download_returns_bytes():
    """The generator decodes binary responses with response.text and hands the
    str to BytesIO, which raises. scripts/fix_generated.py patches that, and
    an import-only check would never catch it coming back."""
    # client_returning serialises its body as JSON; a download returns raw bytes.
    csv = b"member,hours\nalice,12\n"

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=csv)

    client = AuthenticatedClient(
        base_url="https://api.incident.io",
        token="test-key",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    response = pay_reports_v2_download.sync_detailed(client=client, id="abc")

    assert response.status_code == 200
    assert response.parsed.payload.read() == csv


def test_the_package_ships_a_py_typed_marker():
    """Without it, mypy and pyright ignore every annotation in the SDK. `make
    generate` removes the package and recreates the marker, so this catches it
    going missing."""
    marker = Path(incident_io.__path__[0]) / "py.typed"

    assert marker.exists(), f"{marker} is missing"
