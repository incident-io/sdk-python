from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_update_schedule_sync_rule_payload_v2 import (
    SchedulesUpdateScheduleSyncRulePayloadV2,
)
from ...models.schedules_update_schedule_sync_rule_result_v2 import (
    SchedulesUpdateScheduleSyncRuleResultV2,
)
from ...types import Response


def _get_kwargs(
    schedule_id: str,
    id: str,
    *,
    body: SchedulesUpdateScheduleSyncRulePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/schedules/{schedule_id}/sync_rules/{id}".format(
            schedule_id=quote(str(schedule_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2 | None:
    if response.status_code == 200:
        response_200 = SchedulesUpdateScheduleSyncRuleResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesUpdateScheduleSyncRulePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2]:
    """UpdateScheduleSyncRule Schedules V2

     Update a sync rule's sync_type and permanent members in place. If the rule's sync target is shared
    with other schedules, a sync_type change propagates to every linked schedule and the entire
    operation aborts if the caller lacks edit permission on any of them. Permanent members are scoped to
    this rule and never propagate.

    Args:
        schedule_id (str): The parent schedule ID Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        id (str): The sync rule ID Example: 01JXYZ000000000000000000CD.
        body (SchedulesUpdateScheduleSyncRulePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'sync_type': 'on_call'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesUpdateScheduleSyncRulePayloadV2,
) -> ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2 | None:
    """UpdateScheduleSyncRule Schedules V2

     Update a sync rule's sync_type and permanent members in place. If the rule's sync target is shared
    with other schedules, a sync_type change propagates to every linked schedule and the entire
    operation aborts if the caller lacks edit permission on any of them. Permanent members are scoped to
    this rule and never propagate.

    Args:
        schedule_id (str): The parent schedule ID Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        id (str): The sync rule ID Example: 01JXYZ000000000000000000CD.
        body (SchedulesUpdateScheduleSyncRulePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'sync_type': 'on_call'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2
    """

    return sync_detailed(
        schedule_id=schedule_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesUpdateScheduleSyncRulePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2]:
    """UpdateScheduleSyncRule Schedules V2

     Update a sync rule's sync_type and permanent members in place. If the rule's sync target is shared
    with other schedules, a sync_type change propagates to every linked schedule and the entire
    operation aborts if the caller lacks edit permission on any of them. Permanent members are scoped to
    this rule and never propagate.

    Args:
        schedule_id (str): The parent schedule ID Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        id (str): The sync rule ID Example: 01JXYZ000000000000000000CD.
        body (SchedulesUpdateScheduleSyncRulePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'sync_type': 'on_call'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesUpdateScheduleSyncRulePayloadV2,
) -> ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2 | None:
    """UpdateScheduleSyncRule Schedules V2

     Update a sync rule's sync_type and permanent members in place. If the rule's sync target is shared
    with other schedules, a sync_type change propagates to every linked schedule and the entire
    operation aborts if the caller lacks edit permission on any of them. Permanent members are scoped to
    this rule and never propagate.

    Args:
        schedule_id (str): The parent schedule ID Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        id (str): The sync rule ID Example: 01JXYZ000000000000000000CD.
        body (SchedulesUpdateScheduleSyncRulePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'sync_type': 'on_call'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateScheduleSyncRuleResultV2
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
