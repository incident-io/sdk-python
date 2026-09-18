from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_create_payload_v2 import IncidentsCreatePayloadV2
from ...models.incidents_create_result_v2 import IncidentsCreateResultV2
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentsCreateResultV2 | None:
    if response.status_code == 200:
        response_200 = IncidentsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV2,
) -> Response[ErrorResponse | IncidentsCreateResultV2]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to "retrospective" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentsCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'incident_timestamp_values':
            [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode':
            'standard', 'name': 'Our database is sad', 'retrospective_incident_options':
            {'external_id': 123, 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'slack_channel_id': 'abc123'}, 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'slack_team_id': 'T02A1FSLE8J',
            'summary': "Our database is really really sad, and we don't know why yet.", 'visibility':
            'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsCreateResultV2]
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
    body: IncidentsCreatePayloadV2,
) -> ErrorResponse | IncidentsCreateResultV2 | None:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to "retrospective" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentsCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'incident_timestamp_values':
            [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode':
            'standard', 'name': 'Our database is sad', 'retrospective_incident_options':
            {'external_id': 123, 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'slack_channel_id': 'abc123'}, 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'slack_team_id': 'T02A1FSLE8J',
            'summary': "Our database is really really sad, and we don't know why yet.", 'visibility':
            'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV2,
) -> Response[ErrorResponse | IncidentsCreateResultV2]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to "retrospective" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentsCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'incident_timestamp_values':
            [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode':
            'standard', 'name': 'Our database is sad', 'retrospective_incident_options':
            {'external_id': 123, 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'slack_channel_id': 'abc123'}, 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'slack_team_id': 'T02A1FSLE8J',
            'summary': "Our database is really really sad, and we don't know why yet.", 'visibility':
            'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsCreatePayloadV2,
) -> ErrorResponse | IncidentsCreateResultV2 | None:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to "retrospective" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentsCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'incident_timestamp_values':
            [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode':
            'standard', 'name': 'Our database is sad', 'retrospective_incident_options':
            {'external_id': 123, 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'slack_channel_id': 'abc123'}, 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'slack_team_id': 'T02A1FSLE8J',
            'summary': "Our database is really really sad, and we don't know why yet.", 'visibility':
            'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsCreateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
