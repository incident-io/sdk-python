from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.escalations_update_path_payload_v2 import EscalationsUpdatePathPayloadV2
from ...models.escalations_update_path_result_v2 import EscalationsUpdatePathResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: EscalationsUpdatePathPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/escalation_paths/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EscalationsUpdatePathResultV2 | None:
    if response.status_code == 200:
        response_200 = EscalationsUpdatePathResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | EscalationsUpdatePathResultV2]:
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
    body: EscalationsUpdatePathPayloadV2,
) -> Response[ErrorResponse | EscalationsUpdatePathResultV2]:
    """UpdatePath Escalations V2

     Updates an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (EscalationsUpdatePathPayloadV2):  Example: {'kind': 'templated', 'name': 'Urgent
            Support', 'param_bindings': {'abc123': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path':
            {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds':
            120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'repeat_config': {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800},
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsUpdatePathResultV2]
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
    body: EscalationsUpdatePathPayloadV2,
) -> ErrorResponse | EscalationsUpdatePathResultV2 | None:
    """UpdatePath Escalations V2

     Updates an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (EscalationsUpdatePathPayloadV2):  Example: {'kind': 'templated', 'name': 'Urgent
            Support', 'param_bindings': {'abc123': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path':
            {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds':
            120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'repeat_config': {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800},
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsUpdatePathResultV2
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
    body: EscalationsUpdatePathPayloadV2,
) -> Response[ErrorResponse | EscalationsUpdatePathResultV2]:
    """UpdatePath Escalations V2

     Updates an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (EscalationsUpdatePathPayloadV2):  Example: {'kind': 'templated', 'name': 'Urgent
            Support', 'param_bindings': {'abc123': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path':
            {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds':
            120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'repeat_config': {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800},
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsUpdatePathResultV2]
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
    body: EscalationsUpdatePathPayloadV2,
) -> ErrorResponse | EscalationsUpdatePathResultV2 | None:
    """UpdatePath Escalations V2

     Updates an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (EscalationsUpdatePathPayloadV2):  Example: {'kind': 'templated', 'name': 'Urgent
            Support', 'param_bindings': {'abc123': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path':
            {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds':
            120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'repeat_config': {'delay_repeat_on_activity': False, 'repeat_after_seconds': 1800},
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsUpdatePathResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
