from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_forms_update_payload_v3 import IncidentFormsUpdatePayloadV3
from ...models.incident_forms_update_result_v3 import IncidentFormsUpdateResultV3
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentFormsUpdatePayloadV3,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/incident_forms/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentFormsUpdateResultV3 | None:
    if response.status_code == 200:
        response_200 = IncidentFormsUpdateResultV3.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentFormsUpdateResultV3]:
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
    body: IncidentFormsUpdatePayloadV3,
) -> Response[ErrorResponse | IncidentFormsUpdateResultV3]:
    """Update Incident Forms V3

     Replace an incident form, including its elements and expressions.

    Args:
        id (str): Unique identifier of the incident form Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (IncidentFormsUpdatePayloadV3):  Example: {'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'form_type': 'declare', 'incident_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'description': 'Shown when the incident is major or above.', 'element_type': 'name', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?",
            'required_if': 'check_engine_config', 'required_if_condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'show_if_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentFormsUpdateResultV3]
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
    body: IncidentFormsUpdatePayloadV3,
) -> ErrorResponse | IncidentFormsUpdateResultV3 | None:
    """Update Incident Forms V3

     Replace an incident form, including its elements and expressions.

    Args:
        id (str): Unique identifier of the incident form Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (IncidentFormsUpdatePayloadV3):  Example: {'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'form_type': 'declare', 'incident_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'description': 'Shown when the incident is major or above.', 'element_type': 'name', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?",
            'required_if': 'check_engine_config', 'required_if_condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'show_if_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentFormsUpdateResultV3
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
    body: IncidentFormsUpdatePayloadV3,
) -> Response[ErrorResponse | IncidentFormsUpdateResultV3]:
    """Update Incident Forms V3

     Replace an incident form, including its elements and expressions.

    Args:
        id (str): Unique identifier of the incident form Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (IncidentFormsUpdatePayloadV3):  Example: {'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'form_type': 'declare', 'incident_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'description': 'Shown when the incident is major or above.', 'element_type': 'name', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?",
            'required_if': 'check_engine_config', 'required_if_condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'show_if_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentFormsUpdateResultV3]
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
    body: IncidentFormsUpdatePayloadV3,
) -> ErrorResponse | IncidentFormsUpdateResultV3 | None:
    """Update Incident Forms V3

     Replace an incident form, including its elements and expressions.

    Args:
        id (str): Unique identifier of the incident form Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (IncidentFormsUpdatePayloadV3):  Example: {'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'form_type': 'declare', 'incident_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'lifecycle_elements': [{'can_select_no_value': False,
            'config': {'require_comment': False}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'description': 'Shown when the incident is major or above.', 'element_type': 'name', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'placeholder': "What's happening?",
            'required_if': 'check_engine_config', 'required_if_condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'show_if_condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentFormsUpdateResultV3
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
