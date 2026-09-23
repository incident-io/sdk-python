from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.maintenance_windows_create_payload_v1 import (
    MaintenanceWindowsCreatePayloadV1,
)
from ...models.maintenance_windows_create_result_v1 import (
    MaintenanceWindowsCreateResultV1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: MaintenanceWindowsCreatePayloadV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/maintenance_windows",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | MaintenanceWindowsCreateResultV1 | None:
    if response.status_code == 201:
        response_201 = MaintenanceWindowsCreateResultV1.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | MaintenanceWindowsCreateResultV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceWindowsCreatePayloadV1,
) -> Response[ErrorResponse | MaintenanceWindowsCreateResultV1]:
    """Create MaintenanceWindows V1

     Create a new maintenance window.

    Args:
        body (MaintenanceWindowsCreatePayloadV1):  Example: {'alert_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'end_at':
            '2021-08-17T14:28:57.801578Z', 'escalation_targets': [{'escalation_paths': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lead': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for
            database migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name':
            'general', 'channel_type': 'public'}], 'notify_end_minutes_before': 5,
            'notify_start_minutes_before': 15, 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'reroute_on_end': False, 'resolve_on_end': False, 'show_in_sidebar': True, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MaintenanceWindowsCreateResultV1]
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
    body: MaintenanceWindowsCreatePayloadV1,
) -> ErrorResponse | MaintenanceWindowsCreateResultV1 | None:
    """Create MaintenanceWindows V1

     Create a new maintenance window.

    Args:
        body (MaintenanceWindowsCreatePayloadV1):  Example: {'alert_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'end_at':
            '2021-08-17T14:28:57.801578Z', 'escalation_targets': [{'escalation_paths': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lead': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for
            database migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name':
            'general', 'channel_type': 'public'}], 'notify_end_minutes_before': 5,
            'notify_start_minutes_before': 15, 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'reroute_on_end': False, 'resolve_on_end': False, 'show_in_sidebar': True, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MaintenanceWindowsCreateResultV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceWindowsCreatePayloadV1,
) -> Response[ErrorResponse | MaintenanceWindowsCreateResultV1]:
    """Create MaintenanceWindows V1

     Create a new maintenance window.

    Args:
        body (MaintenanceWindowsCreatePayloadV1):  Example: {'alert_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'end_at':
            '2021-08-17T14:28:57.801578Z', 'escalation_targets': [{'escalation_paths': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lead': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for
            database migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name':
            'general', 'channel_type': 'public'}], 'notify_end_minutes_before': 5,
            'notify_start_minutes_before': 15, 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'reroute_on_end': False, 'resolve_on_end': False, 'show_in_sidebar': True, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MaintenanceWindowsCreateResultV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MaintenanceWindowsCreatePayloadV1,
) -> ErrorResponse | MaintenanceWindowsCreateResultV1 | None:
    """Create MaintenanceWindows V1

     Create a new maintenance window.

    Args:
        body (MaintenanceWindowsCreatePayloadV1):  Example: {'alert_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'end_at':
            '2021-08-17T14:28:57.801578Z', 'escalation_targets': [{'escalation_paths': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'lead': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for
            database migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name':
            'general', 'channel_type': 'public'}], 'notify_end_minutes_before': 5,
            'notify_start_minutes_before': 15, 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'reroute_on_end': False, 'resolve_on_end': False, 'show_in_sidebar': True, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MaintenanceWindowsCreateResultV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
