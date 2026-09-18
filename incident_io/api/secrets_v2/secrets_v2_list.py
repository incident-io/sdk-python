from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.secrets_list_result_v2 import SecretsListResultV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_team_ids: list[str] | Unset = UNSET
    if not isinstance(team_ids, Unset):
        json_team_ids = team_ids

    params["team_ids"] = json_team_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/secrets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SecretsListResultV2 | None:
    if response.status_code == 200:
        response_200 = SecretsListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | SecretsListResultV2]:
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
    team_ids: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | SecretsListResultV2]:
    """List Secrets V2

     List all secrets for this organisation. Returns metadata only, never values.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A secret's ID. This endpoint will return a list of secrets after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        team_ids (list[str] | Unset): Filter to secrets owned by any of these teams Example:
            ['abc123'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecretsListResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        team_ids=team_ids,
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
    team_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | SecretsListResultV2 | None:
    """List Secrets V2

     List all secrets for this organisation. Returns metadata only, never values.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A secret's ID. This endpoint will return a list of secrets after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        team_ids (list[str] | Unset): Filter to secrets owned by any of these teams Example:
            ['abc123'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecretsListResultV2
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        team_ids=team_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | SecretsListResultV2]:
    """List Secrets V2

     List all secrets for this organisation. Returns metadata only, never values.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A secret's ID. This endpoint will return a list of secrets after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        team_ids (list[str] | Unset): Filter to secrets owned by any of these teams Example:
            ['abc123'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecretsListResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        team_ids=team_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    team_ids: list[str] | Unset = UNSET,
) -> ErrorResponse | SecretsListResultV2 | None:
    """List Secrets V2

     List all secrets for this organisation. Returns metadata only, never values.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A secret's ID. This endpoint will return a list of secrets after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        team_ids (list[str] | Unset): Filter to secrets owned by any of these teams Example:
            ['abc123'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecretsListResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            team_ids=team_ids,
        )
    ).parsed
