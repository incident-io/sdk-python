from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.workflows_update_workflow_payload_v2 import (
    WorkflowsUpdateWorkflowPayloadV2,
)
from ...models.workflows_update_workflow_result_v2 import (
    WorkflowsUpdateWorkflowResultV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: WorkflowsUpdateWorkflowPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/workflows/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WorkflowsUpdateWorkflowResultV2 | None:
    if response.status_code == 200:
        response_200 = WorkflowsUpdateWorkflowResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | WorkflowsUpdateWorkflowResultV2]:
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
    body: WorkflowsUpdateWorkflowPayloadV2,
) -> Response[ErrorResponse | WorkflowsUpdateWorkflowResultV2]:
    """UpdateWorkflow Workflows V2

     Updates a workflow

    Args:
        id (str): ID of the workflow to update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (WorkflowsUpdateWorkflowPayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'continue_on_step_error':
            True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'folder': 'My folder 01', 'form_fields': [{'array': True,
            'description': 'The customer affected by this incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title':
            'Affected customer', 'type': 'User'}], 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for':
            ['incident.url'], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'owning_teams', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo',
            'skip_step_upgrades': False, 'state': 'active', 'steps': [{'for_each': 'abc123', 'id':
            'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowsUpdateWorkflowResultV2]
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
    body: WorkflowsUpdateWorkflowPayloadV2,
) -> ErrorResponse | WorkflowsUpdateWorkflowResultV2 | None:
    """UpdateWorkflow Workflows V2

     Updates a workflow

    Args:
        id (str): ID of the workflow to update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (WorkflowsUpdateWorkflowPayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'continue_on_step_error':
            True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'folder': 'My folder 01', 'form_fields': [{'array': True,
            'description': 'The customer affected by this incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title':
            'Affected customer', 'type': 'User'}], 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for':
            ['incident.url'], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'owning_teams', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo',
            'skip_step_upgrades': False, 'state': 'active', 'steps': [{'for_each': 'abc123', 'id':
            'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowsUpdateWorkflowResultV2
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
    body: WorkflowsUpdateWorkflowPayloadV2,
) -> Response[ErrorResponse | WorkflowsUpdateWorkflowResultV2]:
    """UpdateWorkflow Workflows V2

     Updates a workflow

    Args:
        id (str): ID of the workflow to update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (WorkflowsUpdateWorkflowPayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'continue_on_step_error':
            True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'folder': 'My folder 01', 'form_fields': [{'array': True,
            'description': 'The customer affected by this incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title':
            'Affected customer', 'type': 'User'}], 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for':
            ['incident.url'], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'owning_teams', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo',
            'skip_step_upgrades': False, 'state': 'active', 'steps': [{'for_each': 'abc123', 'id':
            'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowsUpdateWorkflowResultV2]
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
    body: WorkflowsUpdateWorkflowPayloadV2,
) -> ErrorResponse | WorkflowsUpdateWorkflowResultV2 | None:
    """UpdateWorkflow Workflows V2

     Updates a workflow

    Args:
        id (str): ID of the workflow to update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (WorkflowsUpdateWorkflowPayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'continue_on_step_error':
            True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'folder': 'My folder 01', 'form_fields': [{'array': True,
            'description': 'The customer affected by this incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'key': 'affected_customer', 'required': True, 'title':
            'Affected customer', 'type': 'User'}], 'include_private_escalations': True,
            'include_private_incidents': True, 'name': 'My little workflow', 'once_for':
            ['incident.url'], 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'owning_teams', 'runs_on_incident_modes': ['standard', 'test',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'shortform': 'page-the-ceo',
            'skip_step_upgrades': False, 'state': 'active', 'steps': [{'for_each': 'abc123', 'id':
            'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowsUpdateWorkflowResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
