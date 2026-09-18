from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.status_pages_update_status_page_maintenance_payload_v2 import (
    StatusPagesUpdateStatusPageMaintenancePayloadV2,
)
from ...models.status_pages_update_status_page_maintenance_result_v2 import (
    StatusPagesUpdateStatusPageMaintenanceResultV2,
)
from ...types import Response


def _get_kwargs(
    status_page_maintenance_id: str,
    *,
    body: StatusPagesUpdateStatusPageMaintenancePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/status_page_maintenances/{status_page_maintenance_id}".format(
            status_page_maintenance_id=quote(str(status_page_maintenance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2 | None:
    if response.status_code == 200:
        response_200 = StatusPagesUpdateStatusPageMaintenanceResultV2.from_dict(
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
) -> Response[ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesUpdateStatusPageMaintenancePayloadV2,
) -> Response[ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2]:
    """UpdateStatusPageMaintenance Status Pages V2

     Update the name and scheduled window of a Status Page maintenance window.

    The new start_at and end_at apply to every component this maintenance window affects.

    This does not publish an update to your status page and does not notify subscribers. Automated
    updates only move a window forwards, so one that has already started or completed will not move back
    to an earlier status. To move a status backwards, or to tell subscribers the schedule has changed,
    post a maintenance update to POST /status_page_maintenance_updates.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
        body (StatusPagesUpdateStatusPageMaintenancePayloadV2):  Example: {'end_at':
            '2025-01-28T12:00:00Z', 'name': 'Routine infrastructure upgrade', 'start_at':
            '2025-01-28T10:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2]
    """

    kwargs = _get_kwargs(
        status_page_maintenance_id=status_page_maintenance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesUpdateStatusPageMaintenancePayloadV2,
) -> ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2 | None:
    """UpdateStatusPageMaintenance Status Pages V2

     Update the name and scheduled window of a Status Page maintenance window.

    The new start_at and end_at apply to every component this maintenance window affects.

    This does not publish an update to your status page and does not notify subscribers. Automated
    updates only move a window forwards, so one that has already started or completed will not move back
    to an earlier status. To move a status backwards, or to tell subscribers the schedule has changed,
    post a maintenance update to POST /status_page_maintenance_updates.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
        body (StatusPagesUpdateStatusPageMaintenancePayloadV2):  Example: {'end_at':
            '2025-01-28T12:00:00Z', 'name': 'Routine infrastructure upgrade', 'start_at':
            '2025-01-28T10:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2
    """

    return sync_detailed(
        status_page_maintenance_id=status_page_maintenance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesUpdateStatusPageMaintenancePayloadV2,
) -> Response[ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2]:
    """UpdateStatusPageMaintenance Status Pages V2

     Update the name and scheduled window of a Status Page maintenance window.

    The new start_at and end_at apply to every component this maintenance window affects.

    This does not publish an update to your status page and does not notify subscribers. Automated
    updates only move a window forwards, so one that has already started or completed will not move back
    to an earlier status. To move a status backwards, or to tell subscribers the schedule has changed,
    post a maintenance update to POST /status_page_maintenance_updates.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
        body (StatusPagesUpdateStatusPageMaintenancePayloadV2):  Example: {'end_at':
            '2025-01-28T12:00:00Z', 'name': 'Routine infrastructure upgrade', 'start_at':
            '2025-01-28T10:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2]
    """

    kwargs = _get_kwargs(
        status_page_maintenance_id=status_page_maintenance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesUpdateStatusPageMaintenancePayloadV2,
) -> ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2 | None:
    """UpdateStatusPageMaintenance Status Pages V2

     Update the name and scheduled window of a Status Page maintenance window.

    The new start_at and end_at apply to every component this maintenance window affects.

    This does not publish an update to your status page and does not notify subscribers. Automated
    updates only move a window forwards, so one that has already started or completed will not move back
    to an earlier status. To move a status backwards, or to tell subscribers the schedule has changed,
    post a maintenance update to POST /status_page_maintenance_updates.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
        body (StatusPagesUpdateStatusPageMaintenancePayloadV2):  Example: {'end_at':
            '2025-01-28T12:00:00Z', 'name': 'Routine infrastructure upgrade', 'start_at':
            '2025-01-28T10:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesUpdateStatusPageMaintenanceResultV2
    """

    return (
        await asyncio_detailed(
            status_page_maintenance_id=status_page_maintenance_id,
            client=client,
            body=body,
        )
    ).parsed
