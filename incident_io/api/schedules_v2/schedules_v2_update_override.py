from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_update_override_payload_v2 import (
    SchedulesUpdateOverridePayloadV2,
)
from ...models.schedules_update_override_result_v2 import (
    SchedulesUpdateOverrideResultV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SchedulesUpdateOverridePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/schedule_overrides/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesUpdateOverrideResultV2 | None:
    if response.status_code == 200:
        response_200 = SchedulesUpdateOverrideResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | SchedulesUpdateOverrideResultV2]:
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
    body: SchedulesUpdateOverridePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateOverrideResultV2]:
    """UpdateOverride Schedules V2

     Update a schedule override, moving its window or the rotation and layer it sits on.

    An override cannot be reassigned: send the user it already has, and delete and recreate
    it to put someone else on call for that window.

    Overrides on a layer cannot overlap, so widening one over its neighbour's window takes
    that time over. The neighbour is deleted, and any of its time left outside the new
    window comes back as new overrides with new IDs, so other override IDs on this layer
    may stop resolving — list the schedule's overrides again to pick up the replacements.

    Args:
        id (str): The override ID to update Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesUpdateOverridePayloadV2):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:00:00.000000Z', 'user': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateOverrideResultV2]
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
    body: SchedulesUpdateOverridePayloadV2,
) -> ErrorResponse | SchedulesUpdateOverrideResultV2 | None:
    """UpdateOverride Schedules V2

     Update a schedule override, moving its window or the rotation and layer it sits on.

    An override cannot be reassigned: send the user it already has, and delete and recreate
    it to put someone else on call for that window.

    Overrides on a layer cannot overlap, so widening one over its neighbour's window takes
    that time over. The neighbour is deleted, and any of its time left outside the new
    window comes back as new overrides with new IDs, so other override IDs on this layer
    may stop resolving — list the schedule's overrides again to pick up the replacements.

    Args:
        id (str): The override ID to update Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesUpdateOverridePayloadV2):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:00:00.000000Z', 'user': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateOverrideResultV2
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
    body: SchedulesUpdateOverridePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateOverrideResultV2]:
    """UpdateOverride Schedules V2

     Update a schedule override, moving its window or the rotation and layer it sits on.

    An override cannot be reassigned: send the user it already has, and delete and recreate
    it to put someone else on call for that window.

    Overrides on a layer cannot overlap, so widening one over its neighbour's window takes
    that time over. The neighbour is deleted, and any of its time left outside the new
    window comes back as new overrides with new IDs, so other override IDs on this layer
    may stop resolving — list the schedule's overrides again to pick up the replacements.

    Args:
        id (str): The override ID to update Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesUpdateOverridePayloadV2):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:00:00.000000Z', 'user': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateOverrideResultV2]
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
    body: SchedulesUpdateOverridePayloadV2,
) -> ErrorResponse | SchedulesUpdateOverrideResultV2 | None:
    """UpdateOverride Schedules V2

     Update a schedule override, moving its window or the rotation and layer it sits on.

    An override cannot be reassigned: send the user it already has, and delete and recreate
    it to put someone else on call for that window.

    Overrides on a layer cannot overlap, so widening one over its neighbour's window takes
    that time over. The neighbour is deleted, and any of its time left outside the new
    window comes back as new overrides with new IDs, so other override IDs on this layer
    may stop resolving — list the schedule's overrides again to pick up the replacements.

    Args:
        id (str): The override ID to update Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        body (SchedulesUpdateOverridePayloadV2):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:00:00.000000Z', 'user': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateOverrideResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
