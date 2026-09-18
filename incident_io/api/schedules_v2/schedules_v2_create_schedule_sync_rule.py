from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_create_schedule_sync_rule_payload_v2 import (
    SchedulesCreateScheduleSyncRulePayloadV2,
)
from ...models.schedules_create_schedule_sync_rule_result_v2 import (
    SchedulesCreateScheduleSyncRuleResultV2,
)
from ...types import Response


def _get_kwargs(
    schedule_id: str,
    *,
    body: SchedulesCreateScheduleSyncRulePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/schedules/{schedule_id}/sync_rules".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2 | None:
    if response.status_code == 201:
        response_201 = SchedulesCreateScheduleSyncRuleResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesCreateScheduleSyncRulePayloadV2,
) -> Response[ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2]:
    """CreateScheduleSyncRule Schedules V2

     Create a new sync rule linking a schedule to a sync target.

    Args:
        schedule_id (str): The schedule to create a sync rule for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesCreateScheduleSyncRulePayloadV2):  Example: {'schedule_sync_rule':
            {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT',
            'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesCreateScheduleSyncRulePayloadV2,
) -> ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2 | None:
    """CreateScheduleSyncRule Schedules V2

     Create a new sync rule linking a schedule to a sync target.

    Args:
        schedule_id (str): The schedule to create a sync rule for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesCreateScheduleSyncRulePayloadV2):  Example: {'schedule_sync_rule':
            {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT',
            'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesCreateScheduleSyncRulePayloadV2,
) -> Response[ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2]:
    """CreateScheduleSyncRule Schedules V2

     Create a new sync rule linking a schedule to a sync target.

    Args:
        schedule_id (str): The schedule to create a sync rule for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesCreateScheduleSyncRulePayloadV2):  Example: {'schedule_sync_rule':
            {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT',
            'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchedulesCreateScheduleSyncRulePayloadV2,
) -> ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2 | None:
    """CreateScheduleSyncRule Schedules V2

     Create a new sync rule linking a schedule to a sync target.

    Args:
        schedule_id (str): The schedule to create a sync rule for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesCreateScheduleSyncRulePayloadV2):  Example: {'schedule_sync_rule':
            {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT',
            'schedule_sync_target_id': '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesCreateScheduleSyncRuleResultV2
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            body=body,
        )
    ).parsed
