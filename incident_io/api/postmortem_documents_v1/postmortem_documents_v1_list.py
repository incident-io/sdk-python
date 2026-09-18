from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.postmortem_documents_list_result_v1 import (
    PostmortemDocumentsListResultV1,
)
from ...models.postmortem_documents_v1_list_sort_by import (
    PostmortemDocumentsV1ListSortBy,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    sort_by: PostmortemDocumentsV1ListSortBy
    | Unset = PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params["incident_id"] = incident_id

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/postmortem_documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostmortemDocumentsListResultV1 | None:
    if response.status_code == 200:
        response_200 = PostmortemDocumentsListResultV1.from_dict(response.json())

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
) -> Response[ErrorResponse | PostmortemDocumentsListResultV1]:
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
    incident_id: str | Unset = UNSET,
    sort_by: PostmortemDocumentsV1ListSortBy
    | Unset = PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST,
) -> Response[ErrorResponse | PostmortemDocumentsListResultV1]:
    """List PostmortemDocuments V1

     List post-mortem documents for the organisation.

    Results can be filtered by incident and sorted by creation date. This endpoint returns document
    metadata only. If you want to fetch the content of the post-mortem, use the ShowContent endpoint.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A post-mortem document's ID. This endpoint will return a list of
            post-mortem documents after this ID. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_id (str | Unset): Filter to only return post-mortem documents for the given
            incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        sort_by (PostmortemDocumentsV1ListSortBy | Unset): Controls the order that results are
            returned in Default: PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST. Example:
            created_at_oldest_first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostmortemDocumentsListResultV1]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        sort_by=sort_by,
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
    incident_id: str | Unset = UNSET,
    sort_by: PostmortemDocumentsV1ListSortBy
    | Unset = PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST,
) -> ErrorResponse | PostmortemDocumentsListResultV1 | None:
    """List PostmortemDocuments V1

     List post-mortem documents for the organisation.

    Results can be filtered by incident and sorted by creation date. This endpoint returns document
    metadata only. If you want to fetch the content of the post-mortem, use the ShowContent endpoint.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A post-mortem document's ID. This endpoint will return a list of
            post-mortem documents after this ID. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_id (str | Unset): Filter to only return post-mortem documents for the given
            incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        sort_by (PostmortemDocumentsV1ListSortBy | Unset): Controls the order that results are
            returned in Default: PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST. Example:
            created_at_oldest_first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostmortemDocumentsListResultV1
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    sort_by: PostmortemDocumentsV1ListSortBy
    | Unset = PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST,
) -> Response[ErrorResponse | PostmortemDocumentsListResultV1]:
    """List PostmortemDocuments V1

     List post-mortem documents for the organisation.

    Results can be filtered by incident and sorted by creation date. This endpoint returns document
    metadata only. If you want to fetch the content of the post-mortem, use the ShowContent endpoint.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A post-mortem document's ID. This endpoint will return a list of
            post-mortem documents after this ID. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_id (str | Unset): Filter to only return post-mortem documents for the given
            incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        sort_by (PostmortemDocumentsV1ListSortBy | Unset): Controls the order that results are
            returned in Default: PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST. Example:
            created_at_oldest_first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostmortemDocumentsListResultV1]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    sort_by: PostmortemDocumentsV1ListSortBy
    | Unset = PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST,
) -> ErrorResponse | PostmortemDocumentsListResultV1 | None:
    """List PostmortemDocuments V1

     List post-mortem documents for the organisation.

    Results can be filtered by incident and sorted by creation date. This endpoint returns document
    metadata only. If you want to fetch the content of the post-mortem, use the ShowContent endpoint.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A post-mortem document's ID. This endpoint will return a list of
            post-mortem documents after this ID. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_id (str | Unset): Filter to only return post-mortem documents for the given
            incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        sort_by (PostmortemDocumentsV1ListSortBy | Unset): Controls the order that results are
            returned in Default: PostmortemDocumentsV1ListSortBy.CREATED_AT_NEWEST_FIRST. Example:
            created_at_oldest_first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostmortemDocumentsListResultV1
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            incident_id=incident_id,
            sort_by=sort_by,
        )
    ).parsed
