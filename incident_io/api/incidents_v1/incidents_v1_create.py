from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_create_payload_v1 import IncidentsCreatePayloadV1
from ...models.incidents_create_result_v1 import IncidentsCreateResultV1
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentsCreatePayloadV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/incidents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentsCreateResultV1 | None:
    if response.status_code == 200:
        response_200 = IncidentsCreateResultV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | IncidentsCreateResultV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV1,
) -> Response[ErrorResponse | IncidentsCreateResultV1]:
    """Create Incidents V1

     Create a new incident.

    Args:
        body (IncidentsCreatePayloadV1):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsCreateResultV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV1,
) -> ErrorResponse | IncidentsCreateResultV1 | None:
    """Create Incidents V1

     Create a new incident.

    Args:
        body (IncidentsCreatePayloadV1):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsCreateResultV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV1,
) -> Response[ErrorResponse | IncidentsCreateResultV1]:
    """Create Incidents V1

     Create a new incident.

    Args:
        body (IncidentsCreatePayloadV1):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsCreateResultV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV1,
) -> ErrorResponse | IncidentsCreateResultV1 | None:
    """Create Incidents V1

     Create a new incident.

    Args:
        body (IncidentsCreatePayloadV1):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsCreateResultV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools
import warnings as _warnings


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(
            "POST /v1/incidents is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated(asyncio_detailed)
asyncio = _deprecated(asyncio)
