from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.policies_update_payload_v2 import PoliciesUpdatePayloadV2
from ...models.policies_update_result_v2 import PoliciesUpdateResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PoliciesUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/policies/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PoliciesUpdateResultV2 | None:
    if response.status_code == 200:
        response_200 = PoliciesUpdateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | PoliciesUpdateResultV2]:
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
    body: PoliciesUpdatePayloadV2,
) -> Response[ErrorResponse | PoliciesUpdateResultV2]:
    """Update Policies V2

     Update an existing policy.

    The <code>policy_type</code> of an existing policy cannot be changed: sending a
    different type is rejected. Create a new policy instead.

    Args:
        id (str): Unique identifier for the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (PoliciesUpdatePayloadV2):  Example: {'assignment_rules': {'bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after':
            {'interval': 'daily'}, 'reminder_cadence_before': {'interval': 'daily'},
            'reminder_detected_date_offset_hours': [0, 48], 'reminder_due_date_offset_hours': [-24, 0,
            24]}, 'conditions': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'debrief': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'description': 'All critical
            incidents must export follow-ups to an external issue tracker before 7 days has passed
            since closure.', 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'follow_up': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'name': 'Critical incidents
            must export follow-ups', 'on_call_readiness': {'enforcement': 'advisory', 'high_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}]}, 'policy_type': 'follow_up',
            'post_mortem': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z',
            'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'run_on_private_incidents': False}, 'schedule':
            {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}, 'status': 'enabled'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PoliciesUpdateResultV2]
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
    body: PoliciesUpdatePayloadV2,
) -> ErrorResponse | PoliciesUpdateResultV2 | None:
    """Update Policies V2

     Update an existing policy.

    The <code>policy_type</code> of an existing policy cannot be changed: sending a
    different type is rejected. Create a new policy instead.

    Args:
        id (str): Unique identifier for the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (PoliciesUpdatePayloadV2):  Example: {'assignment_rules': {'bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after':
            {'interval': 'daily'}, 'reminder_cadence_before': {'interval': 'daily'},
            'reminder_detected_date_offset_hours': [0, 48], 'reminder_due_date_offset_hours': [-24, 0,
            24]}, 'conditions': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'debrief': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'description': 'All critical
            incidents must export follow-ups to an external issue tracker before 7 days has passed
            since closure.', 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'follow_up': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'name': 'Critical incidents
            must export follow-ups', 'on_call_readiness': {'enforcement': 'advisory', 'high_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}]}, 'policy_type': 'follow_up',
            'post_mortem': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z',
            'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'run_on_private_incidents': False}, 'schedule':
            {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}, 'status': 'enabled'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PoliciesUpdateResultV2
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
    body: PoliciesUpdatePayloadV2,
) -> Response[ErrorResponse | PoliciesUpdateResultV2]:
    """Update Policies V2

     Update an existing policy.

    The <code>policy_type</code> of an existing policy cannot be changed: sending a
    different type is rejected. Create a new policy instead.

    Args:
        id (str): Unique identifier for the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (PoliciesUpdatePayloadV2):  Example: {'assignment_rules': {'bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after':
            {'interval': 'daily'}, 'reminder_cadence_before': {'interval': 'daily'},
            'reminder_detected_date_offset_hours': [0, 48], 'reminder_due_date_offset_hours': [-24, 0,
            24]}, 'conditions': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'debrief': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'description': 'All critical
            incidents must export follow-ups to an external issue tracker before 7 days has passed
            since closure.', 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'follow_up': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'name': 'Critical incidents
            must export follow-ups', 'on_call_readiness': {'enforcement': 'advisory', 'high_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}]}, 'policy_type': 'follow_up',
            'post_mortem': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z',
            'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'run_on_private_incidents': False}, 'schedule':
            {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}, 'status': 'enabled'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PoliciesUpdateResultV2]
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
    body: PoliciesUpdatePayloadV2,
) -> ErrorResponse | PoliciesUpdateResultV2 | None:
    """Update Policies V2

     Update an existing policy.

    The <code>policy_type</code> of an existing policy cannot be changed: sending a
    different type is rejected. Create a new policy instead.

    Args:
        id (str): Unique identifier for the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (PoliciesUpdatePayloadV2):  Example: {'assignment_rules': {'bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after':
            {'interval': 'daily'}, 'reminder_cadence_before': {'interval': 'daily'},
            'reminder_detected_date_offset_hours': [0, 48], 'reminder_due_date_offset_hours': [-24, 0,
            24]}, 'conditions': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'debrief': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'description': 'All critical
            incidents must export follow-ups to an external issue tracker before 7 days has passed
            since closure.', 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'follow_up': {'due_date_config': {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'requirements': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'run_on_private_incidents': False}, 'name': 'Critical incidents
            must export follow-ups', 'on_call_readiness': {'enforcement': 'advisory', 'high_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}], 'low_urgency':
            [{'max_delay_seconds': 300, 'method_types': ['slack']}]}, 'policy_type': 'follow_up',
            'post_mortem': {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z',
            'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'run_on_private_incidents': False}, 'schedule':
            {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}, 'status': 'enabled'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PoliciesUpdateResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
