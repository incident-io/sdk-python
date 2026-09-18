from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_list_entries_result_v3 import CatalogListEntriesResultV3
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    catalog_type_id: str,
    page_size: int = 25,
    after: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["catalog_type_id"] = catalog_type_id

    params["page_size"] = page_size

    params["after"] = after

    params["identifier"] = identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/catalog_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogListEntriesResultV3 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CatalogListEntriesResultV3.from_dict(response.json())

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
) -> Response[CatalogListEntriesResultV3 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    catalog_type_id: str,
    page_size: int = 25,
    after: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Response[CatalogListEntriesResultV3 | ErrorResponse]:
    """ListEntries Catalog V3

     List entries for a catalog type.

    Args:
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        page_size (int): The integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        identifier (str | Unset): If specified, only entries with this identifier will be
            returned. This will search by ID, external ID, and aliases.

            If 'use name as identifier' is enabled for the catalog type, this will also match on name.
            Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogListEntriesResultV3 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    catalog_type_id: str,
    page_size: int = 25,
    after: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> CatalogListEntriesResultV3 | ErrorResponse | None:
    """ListEntries Catalog V3

     List entries for a catalog type.

    Args:
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        page_size (int): The integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        identifier (str | Unset): If specified, only entries with this identifier will be
            returned. This will search by ID, external ID, and aliases.

            If 'use name as identifier' is enabled for the catalog type, this will also match on name.
            Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogListEntriesResultV3 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
        identifier=identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    catalog_type_id: str,
    page_size: int = 25,
    after: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> Response[CatalogListEntriesResultV3 | ErrorResponse]:
    """ListEntries Catalog V3

     List entries for a catalog type.

    Args:
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        page_size (int): The integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        identifier (str | Unset): If specified, only entries with this identifier will be
            returned. This will search by ID, external ID, and aliases.

            If 'use name as identifier' is enabled for the catalog type, this will also match on name.
            Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogListEntriesResultV3 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    catalog_type_id: str,
    page_size: int = 25,
    after: str | Unset = UNSET,
    identifier: str | Unset = UNSET,
) -> CatalogListEntriesResultV3 | ErrorResponse | None:
    """ListEntries Catalog V3

     List entries for a catalog type.

    Args:
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        page_size (int): The integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        identifier (str | Unset): If specified, only entries with this identifier will be
            returned. This will search by ID, external ID, and aliases.

            If 'use name as identifier' is enabled for the catalog type, this will also match on name.
            Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogListEntriesResultV3 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            catalog_type_id=catalog_type_id,
            page_size=page_size,
            after=after,
            identifier=identifier,
        )
    ).parsed
