from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    status_page_maintenance_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/status_page_maintenances/{status_page_maintenance_id}".format(
            status_page_maintenance_id=quote(str(status_page_maintenance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ErrorResponse]:
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
) -> Response[Any | ErrorResponse]:
    """DeleteStatusPageMaintenance Status Pages V2

     Delete a Status Page maintenance window.

    The maintenance window and its updates stop appearing on your public status page, links to it stop
    working, and a window that has not yet run publishes no further automated updates. This cannot be
    undone.

    Subscribers are not told the window has been deleted, so anyone already emailed about it will have
    updates for a maintenance window they can no longer find.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        status_page_maintenance_id=status_page_maintenance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ErrorResponse | None:
    """DeleteStatusPageMaintenance Status Pages V2

     Delete a Status Page maintenance window.

    The maintenance window and its updates stop appearing on your public status page, links to it stop
    working, and a window that has not yet run publishes no further automated updates. This cannot be
    undone.

    Subscribers are not told the window has been deleted, so anyone already emailed about it will have
    updates for a maintenance window they can no longer find.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        status_page_maintenance_id=status_page_maintenance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ErrorResponse]:
    """DeleteStatusPageMaintenance Status Pages V2

     Delete a Status Page maintenance window.

    The maintenance window and its updates stop appearing on your public status page, links to it stop
    working, and a window that has not yet run publishes no further automated updates. This cannot be
    undone.

    Subscribers are not told the window has been deleted, so anyone already emailed about it will have
    updates for a maintenance window they can no longer find.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        status_page_maintenance_id=status_page_maintenance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_maintenance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ErrorResponse | None:
    """DeleteStatusPageMaintenance Status Pages V2

     Delete a Status Page maintenance window.

    The maintenance window and its updates stop appearing on your public status page, links to it stop
    working, and a window that has not yet run publishes no further automated updates. This cannot be
    undone.

    Subscribers are not told the window has been deleted, so anyone already emailed about it will have
    updates for a maintenance window they can no longer find.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        status_page_maintenance_id (str): ID of the status page maintenance window Example:
            01FCNDV6P870EA6S7TK1DSYDG1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            status_page_maintenance_id=status_page_maintenance_id,
            client=client,
        )
    ).parsed
