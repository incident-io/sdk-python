from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    force: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/maintenance_windows/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Response[Any | ErrorResponse]:
    """Delete MaintenanceWindows V1

     Archives a maintenance window. Set force to archive an active window.

    Args:
        id (str): Unique identifier of the maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        force (bool | Unset): Archives the window even if it is active. This ends the window
            immediately. Its resolve_on_end and reroute_on_end actions do not run, so the alerts it is
            holding stay as they are. To run those actions, use Update to set end_at, then delete the
            window once it has ended. Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Any | ErrorResponse | None:
    """Delete MaintenanceWindows V1

     Archives a maintenance window. Set force to archive an active window.

    Args:
        id (str): Unique identifier of the maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        force (bool | Unset): Archives the window even if it is active. This ends the window
            immediately. Its resolve_on_end and reroute_on_end actions do not run, so the alerts it is
            holding stay as they are. To run those actions, use Update to set end_at, then delete the
            window once it has ended. Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Response[Any | ErrorResponse]:
    """Delete MaintenanceWindows V1

     Archives a maintenance window. Set force to archive an active window.

    Args:
        id (str): Unique identifier of the maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        force (bool | Unset): Archives the window even if it is active. This ends the window
            immediately. Its resolve_on_end and reroute_on_end actions do not run, so the alerts it is
            holding stay as they are. To run those actions, use Update to set end_at, then delete the
            window once it has ended. Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Any | ErrorResponse | None:
    """Delete MaintenanceWindows V1

     Archives a maintenance window. Set force to archive an active window.

    Args:
        id (str): Unique identifier of the maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        force (bool | Unset): Archives the window even if it is active. This ends the window
            immediately. Its resolve_on_end and reroute_on_end actions do not run, so the alerts it is
            holding stay as they are. To run those actions, use Update to set end_at, then delete the
            window once it has ended. Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            force=force,
        )
    ).parsed
