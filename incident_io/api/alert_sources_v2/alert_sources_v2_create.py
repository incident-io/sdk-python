from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_sources_create_payload_v2 import AlertSourcesCreatePayloadV2
from ...models.alert_sources_create_result_v2 import AlertSourcesCreateResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlertSourcesCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/alert_sources",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertSourcesCreateResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlertSourcesCreateResultV2.from_dict(response.json())

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
) -> Response[AlertSourcesCreateResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertSourcesCreatePayloadV2,
) -> Response[AlertSourcesCreateResultV2 | ErrorResponse]:
    """Create Alert Sources V2

     Create a new alert source in your account.

    Args:
        body (AlertSourcesCreatePayloadV2):  Example: {'auto_resolve_incident_alerts': False,
            'auto_resolve_timeout_minutes': 1, 'azure_devops_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title:
            $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ?
            'resolved' : 'firing',\\n  deduplication_key: $.header_message_id,\\n}"},
            'filter_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0,
            'interval_seconds': 60}, 'http_custom_options': {'deduplication_key_path': '$.alert_id',
            'transform_expression': "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n
            status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team,
            severity: $.severity }\\n}"}, 'jira_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '10043']}, 'name': 'Production Web Dashboard Alerts',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rate_limit_sharding':
            {'rate_limit_shard_key_path': '$.priority'}, 'source_type': 'alertmanager', 'template':
            {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal':
            'SEV123', 'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSourcesCreateResultV2 | ErrorResponse]
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
    body: AlertSourcesCreatePayloadV2,
) -> AlertSourcesCreateResultV2 | ErrorResponse | None:
    """Create Alert Sources V2

     Create a new alert source in your account.

    Args:
        body (AlertSourcesCreatePayloadV2):  Example: {'auto_resolve_incident_alerts': False,
            'auto_resolve_timeout_minutes': 1, 'azure_devops_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title:
            $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ?
            'resolved' : 'firing',\\n  deduplication_key: $.header_message_id,\\n}"},
            'filter_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0,
            'interval_seconds': 60}, 'http_custom_options': {'deduplication_key_path': '$.alert_id',
            'transform_expression': "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n
            status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team,
            severity: $.severity }\\n}"}, 'jira_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '10043']}, 'name': 'Production Web Dashboard Alerts',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rate_limit_sharding':
            {'rate_limit_shard_key_path': '$.priority'}, 'source_type': 'alertmanager', 'template':
            {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal':
            'SEV123', 'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSourcesCreateResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertSourcesCreatePayloadV2,
) -> Response[AlertSourcesCreateResultV2 | ErrorResponse]:
    """Create Alert Sources V2

     Create a new alert source in your account.

    Args:
        body (AlertSourcesCreatePayloadV2):  Example: {'auto_resolve_incident_alerts': False,
            'auto_resolve_timeout_minutes': 1, 'azure_devops_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title:
            $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ?
            'resolved' : 'firing',\\n  deduplication_key: $.header_message_id,\\n}"},
            'filter_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0,
            'interval_seconds': 60}, 'http_custom_options': {'deduplication_key_path': '$.alert_id',
            'transform_expression': "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n
            status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team,
            severity: $.severity }\\n}"}, 'jira_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '10043']}, 'name': 'Production Web Dashboard Alerts',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rate_limit_sharding':
            {'rate_limit_shard_key_path': '$.priority'}, 'source_type': 'alertmanager', 'template':
            {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal':
            'SEV123', 'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSourcesCreateResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AlertSourcesCreatePayloadV2,
) -> AlertSourcesCreateResultV2 | ErrorResponse | None:
    """Create Alert Sources V2

     Create a new alert source in your account.

    Args:
        body (AlertSourcesCreatePayloadV2):  Example: {'auto_resolve_incident_alerts': False,
            'auto_resolve_timeout_minutes': 1, 'azure_devops_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}, 'email_options':
            {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title:
            $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ?
            'resolved' : 'firing',\\n  deduplication_key: $.header_message_id,\\n}"},
            'filter_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'fixed_team_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'heartbeat_options': {'failure_threshold': 1, 'grace_period_seconds': 0,
            'interval_seconds': 60}, 'http_custom_options': {'deduplication_key_path': '$.alert_id',
            'transform_expression': "return {\\n  title: $.title || $.name || 'Unknown Alert',\\n
            status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team,
            severity: $.severity }\\n}"}, 'jira_options': {'project_ids':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '10043']}, 'name': 'Production Web Dashboard Alerts',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rate_limit_sharding':
            {'rate_limit_shard_key_path': '$.priority'}, 'source_type': 'alertmanager', 'template':
            {'attributes': [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal':
            'SEV123', 'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel',
            'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}},
            'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSourcesCreateResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
