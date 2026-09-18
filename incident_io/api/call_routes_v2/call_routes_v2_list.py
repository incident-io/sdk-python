from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_routes_list_result_v2 import CallRoutesListResultV2
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/call_routes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CallRoutesListResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CallRoutesListResultV2.from_dict(response.json())

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
) -> Response[CallRoutesListResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[CallRoutesListResultV2 | ErrorResponse]:
    """List Call Routes V2

     List all call routes for this organisation.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A call route's ID. This endpoint will return a list of call routes
            after this ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallRoutesListResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> CallRoutesListResultV2 | ErrorResponse | None:
    """List Call Routes V2

     List all call routes for this organisation.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A call route's ID. This endpoint will return a list of call routes
            after this ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallRoutesListResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[CallRoutesListResultV2 | ErrorResponse]:
    """List Call Routes V2

     List all call routes for this organisation.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A call route's ID. This endpoint will return a list of call routes
            after this ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallRoutesListResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> CallRoutesListResultV2 | ErrorResponse | None:
    """List Call Routes V2

     List all call routes for this organisation.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A call route's ID. This endpoint will return a list of call routes
            after this ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallRoutesListResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
        )
    ).parsed
