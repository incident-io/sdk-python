"""Behavioural tests that need no API key.

`make verify` proves every generated module imports. These prove the parts we
are responsible for actually behave: the client we hand callers, and the
deprecation wrappers scripts/mark_deprecated.py appends after generation.

Requests are served by a local httpx transport rather than the real API, so
these run on a pull request. scripts/smoke_test.py covers the live API.
"""

from __future__ import annotations

import inspect

import httpx
import pytest

from incident_io import AuthenticatedClient
from incident_io.api.actions_v1 import actions_v1_list
from incident_io.api.incidents_v2 import incidents_v2_list
from incident_io.api.pay_reports_v2 import pay_reports_v2_download
from incident_io.api.severities_v1 import severities_v1_list
from incident_io.models import (
    IncidentsV2ListCreatedAt,
    IncidentsV2ListCustomField,
    IncidentsV2ListCustomFieldAdditionalProperty,
    IncidentsV2ListStatus,
    IncidentsV2ListUpdatedAt,
)

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


async def test_the_async_entry_point_works():
    client = client_returning(200, SEVERITIES_BODY)

    result = await severities_v1_list.asyncio(client=client)

    assert result.severities[0].name == "Minor"


# The generated package has no deprecated endpoints of its own — these cover
# what scripts/mark_deprecated.py adds afterwards, which is the part we own.


def test_a_deprecated_endpoint_warns():
    client = client_returning(200, {"actions": []})

    with pytest.warns(DeprecationWarning, match=r"GET /v1/actions"):
        actions_v1_list.sync_detailed(client=client)


def test_a_deprecated_endpoint_warns_once_not_twice():
    """sync() calls sync_detailed(), and both carry the wrapper. Without
    suppression the second warning points inside the SDK, which under
    -W error blames us for the caller's mistake."""
    client = client_returning(200, {"actions": []})

    with pytest.warns(DeprecationWarning) as caught:
        actions_v1_list.sync(client=client)

    assert len(caught) == 1, f"expected one warning, got {len(caught)}"
    assert "incident_io" not in caught[0].filename, (
        "the warning points inside the SDK rather than at the caller"
    )


def test_a_deprecated_async_endpoint_stays_a_coroutine_function():
    """Wrapping `async def` in a plain `def` would break anything that branches
    on inspect.iscoroutinefunction, even though `await` still works."""
    assert inspect.iscoroutinefunction(actions_v1_list.asyncio)
    assert inspect.iscoroutinefunction(actions_v1_list.asyncio_detailed)


async def test_a_deprecated_async_endpoint_warns_and_still_returns():
    client = client_returning(200, {"actions": []})

    with pytest.warns(DeprecationWarning):
        response = await actions_v1_list.asyncio_detailed(client=client)

    assert response.status_code == 200


def test_an_undeprecated_endpoint_does_not_warn(recwarn):
    client = client_returning(200, SEVERITIES_BODY)

    severities_v1_list.sync_detailed(client=client)

    assert not [w for w in recwarn.list if w.category is DeprecationWarning]


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


def filters_sent(**filters) -> dict[str, str]:
    """The query string incidents_v2_list actually puts on the wire."""
    requests: list[httpx.Request] = []
    client = client_returning(200, {"incidents": []}, requests)

    incidents_v2_list.sync_detailed(client=client, **filters)

    return dict(requests[0].url.params)


def test_object_query_parameters_keep_their_name():
    """`created_at[gte]=...`, not `gte=...`.

    The API's filters are objects keyed by operator. openapi-python-client
    hoists an object parameter's keys to the top level, which sends the
    operator as if it were the parameter, so the server sees something it
    does not know and ignores the filter. scripts/fix_generated.py rewrites
    that; this is the check that it did.
    """
    created_at = IncidentsV2ListCreatedAt()
    created_at["gte"] = ["2024-05-01"]
    status = IncidentsV2ListStatus()
    status["one_of"] = ["01GBSQF3FHF7FWZQNWGHAVQ804"]

    sent = filters_sent(created_at=created_at, status=status)

    # httpx percent-encodes the brackets. Go's net/url decodes them before the
    # handler sees the key, so this is the same key as a literal `[`.
    assert sent["created_at[gte]"] == "2024-05-01"
    assert sent["status[one_of]"] == "01GBSQF3FHF7FWZQNWGHAVQ804"
    assert "gte" not in sent
    assert "one_of" not in sent


def test_two_filters_sharing_an_operator_both_survive():
    """The hoisting bug was not only mis-keying, it lost data.

    `created_at[gte]` and `updated_at[gte]` both became `gte`, and the second
    `params.update()` overwrote the first — so one filter vanished and the
    caller got a 200 with the wrong rows.
    """
    created_at = IncidentsV2ListCreatedAt()
    created_at["gte"] = ["2024-05-01"]
    updated_at = IncidentsV2ListUpdatedAt()
    updated_at["gte"] = ["2024-06-01"]

    sent = filters_sent(created_at=created_at, updated_at=updated_at)

    assert sent["created_at[gte]"] == "2024-05-01"
    assert sent["updated_at[gte]"] == "2024-06-01"


def test_nested_filters_flatten_to_two_levels():
    """`custom_field[<id>][one_of]=...`, not a stringified dict.

    Two of the 21 object parameters nest: custom_field and incident_role are
    keyed by field ID and then by operator. Flattening one level turned those
    into `custom_field[<id>]={'one_of': [...]}`.
    """
    operators = IncidentsV2ListCustomFieldAdditionalProperty()
    operators["one_of"] = ["01ET65M7ZARSFZ6TFDFVQDN9AA"]
    custom_field = IncidentsV2ListCustomField()
    custom_field["01GBSQF3FHF7FWZQNWGHAVQ804"] = operators

    sent = filters_sent(custom_field=custom_field)
    assert (
        sent["custom_field[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]"]
        == "01ET65M7ZARSFZ6TFDFVQDN9AA"
    )
