from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.escalation_path_templates_list_result_v2 import (
    EscalationPathTemplatesListResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/escalation_path_templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EscalationPathTemplatesListResultV2 | None:
    if response.status_code == 200:
        response_200 = EscalationPathTemplatesListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | EscalationPathTemplatesListResultV2]:
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
    search: str | Unset = UNSET,
) -> Response[ErrorResponse | EscalationPathTemplatesListResultV2]:
    """List Escalation Path Templates V2

     List active escalation path templates.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        search (str | Unset): Search query to filter results by name. Example: Team on-call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationPathTemplatesListResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        search=search,
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
    search: str | Unset = UNSET,
) -> ErrorResponse | EscalationPathTemplatesListResultV2 | None:
    """List Escalation Path Templates V2

     List active escalation path templates.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        search (str | Unset): Search query to filter results by name. Example: Team on-call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationPathTemplatesListResultV2
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[ErrorResponse | EscalationPathTemplatesListResultV2]:
    """List Escalation Path Templates V2

     List active escalation path templates.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        search (str | Unset): Search query to filter results by name. Example: Team on-call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationPathTemplatesListResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> ErrorResponse | EscalationPathTemplatesListResultV2 | None:
    """List Escalation Path Templates V2

     List active escalation path templates.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        search (str | Unset): Search query to filter results by name. Example: Team on-call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationPathTemplatesListResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            search=search,
        )
    ).parsed
