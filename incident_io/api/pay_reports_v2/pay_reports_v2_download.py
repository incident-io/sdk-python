from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/pay_reports/{id}/download".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[ErrorResponse | File]:
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
) -> Response[ErrorResponse | File]:
    """Download Pay Reports V2

     Download a pay report as CSV.

    One row per user, carrying what they earned over the report's window and how long they
    were on-call for it. Each value appears twice: once formatted for a person to read, and
    once as an integer for a system to parse.

    Only a report that has finished generating can be downloaded, since an incomplete one has
    no totals to write. Check the report's status first.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | File | None:
    """Download Pay Reports V2

     Download a pay report as CSV.

    One row per user, carrying what they earned over the report's window and how long they
    were on-call for it. Each value appears twice: once formatted for a person to read, and
    once as an integer for a system to parse.

    Only a report that has finished generating can be downloaded, since an incomplete one has
    no totals to write. Check the report's status first.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | File]:
    """Download Pay Reports V2

     Download a pay report as CSV.

    One row per user, carrying what they earned over the report's window and how long they
    were on-call for it. Each value appears twice: once formatted for a person to read, and
    once as an integer for a system to parse.

    Only a report that has finished generating can be downloaded, since an incomplete one has
    no totals to write. Check the report's status first.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | File | None:
    """Download Pay Reports V2

     Download a pay report as CSV.

    One row per user, carrying what they earned over the report's window and how long they
    were on-call for it. Each value appears twice: once formatted for a person to read, and
    once as an integer for a system to parse.

    Only a report that has finished generating can be downloaded, since an incomplete one has
    no totals to write. Check the report's status first.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
