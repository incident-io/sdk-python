from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_edit_payload_v2 import IncidentsEditPayloadV2
from ...models.incidents_edit_result_v2 import IncidentsEditResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentsEditPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents/{id}/actions/edit".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentsEditResultV2 | None:
    if response.status_code == 200:
        response_200 = IncidentsEditResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentsEditResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsEditPayloadV2,
) -> Response[ErrorResponse | IncidentsEditResultV2]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    The API key must have the scope corresponding to each property it changes:

    - `incidents.update_name` for the name
    - `incidents.update_summary` for the summary
    - `incidents.update_severity` for the severity
    - `incidents.update_status` for the status
    - `incidents.update_custom_fields` for custom fields
    - `incidents.update_timestamps` for timestamps
    - `incidents.update_role_assignments` for role assignments
    - `incident_calls.create` to set the call URL
    - `incident_calls.destroy` when replacing an existing call URL

    Args:
        id (str): The unique identifier of the incident that you want to edit Example:
            01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsEditPayloadV2):  Example: {'incident': {'call_url': 'https://zoom.us/foo',
            'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsEditResultV2]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsEditPayloadV2,
) -> ErrorResponse | IncidentsEditResultV2 | None:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    The API key must have the scope corresponding to each property it changes:

    - `incidents.update_name` for the name
    - `incidents.update_summary` for the summary
    - `incidents.update_severity` for the severity
    - `incidents.update_status` for the status
    - `incidents.update_custom_fields` for custom fields
    - `incidents.update_timestamps` for timestamps
    - `incidents.update_role_assignments` for role assignments
    - `incident_calls.create` to set the call URL
    - `incident_calls.destroy` when replacing an existing call URL

    Args:
        id (str): The unique identifier of the incident that you want to edit Example:
            01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsEditPayloadV2):  Example: {'incident': {'call_url': 'https://zoom.us/foo',
            'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsEditResultV2
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsEditPayloadV2,
) -> Response[ErrorResponse | IncidentsEditResultV2]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    The API key must have the scope corresponding to each property it changes:

    - `incidents.update_name` for the name
    - `incidents.update_summary` for the summary
    - `incidents.update_severity` for the severity
    - `incidents.update_status` for the status
    - `incidents.update_custom_fields` for custom fields
    - `incidents.update_timestamps` for timestamps
    - `incidents.update_role_assignments` for role assignments
    - `incident_calls.create` to set the call URL
    - `incident_calls.destroy` when replacing an existing call URL

    Args:
        id (str): The unique identifier of the incident that you want to edit Example:
            01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsEditPayloadV2):  Example: {'incident': {'call_url': 'https://zoom.us/foo',
            'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsEditResultV2]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IncidentsEditPayloadV2,
) -> ErrorResponse | IncidentsEditResultV2 | None:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    The API key must have the scope corresponding to each property it changes:

    - `incidents.update_name` for the name
    - `incidents.update_summary` for the summary
    - `incidents.update_severity` for the severity
    - `incidents.update_status` for the status
    - `incidents.update_custom_fields` for custom fields
    - `incidents.update_timestamps` for timestamps
    - `incidents.update_role_assignments` for role assignments
    - `incident_calls.create` to set the call URL
    - `incident_calls.destroy` when replacing an existing call URL

    Args:
        id (str): The unique identifier of the incident that you want to edit Example:
            01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsEditPayloadV2):  Example: {'incident': {'call_url': 'https://zoom.us/foo',
            'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_status_id': 'abc123', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsEditResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
