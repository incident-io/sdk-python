from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pay_reports_unpublish_payload_v2 import PayReportsUnpublishPayloadV2
from ...models.pay_reports_unpublish_result_v2 import PayReportsUnpublishResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PayReportsUnpublishPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/pay_reports/{id}/actions/unpublish".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PayReportsUnpublishResultV2 | None:
    if response.status_code == 200:
        response_200 = PayReportsUnpublishResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | PayReportsUnpublishResultV2]:
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
    body: PayReportsUnpublishPayloadV2,
) -> Response[ErrorResponse | PayReportsUnpublishResultV2]:
    """Unpublish Pay Reports V2

     Unpublish a published pay report, recording a reason it should not be used.

    A draft cannot be unpublished: delete it instead.

    Unpublishing is terminal: the report no longer appears in List or Show, and cannot be
    published again. The reason is shown to anyone who still has a permalink.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayReportsUnpublishPayloadV2):  Example: {'unpublish_reason': 'The date range is
            wrong and one schedule was incorrectly synced.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayReportsUnpublishResultV2]
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
    body: PayReportsUnpublishPayloadV2,
) -> ErrorResponse | PayReportsUnpublishResultV2 | None:
    """Unpublish Pay Reports V2

     Unpublish a published pay report, recording a reason it should not be used.

    A draft cannot be unpublished: delete it instead.

    Unpublishing is terminal: the report no longer appears in List or Show, and cannot be
    published again. The reason is shown to anyone who still has a permalink.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayReportsUnpublishPayloadV2):  Example: {'unpublish_reason': 'The date range is
            wrong and one schedule was incorrectly synced.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayReportsUnpublishResultV2
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
    body: PayReportsUnpublishPayloadV2,
) -> Response[ErrorResponse | PayReportsUnpublishResultV2]:
    """Unpublish Pay Reports V2

     Unpublish a published pay report, recording a reason it should not be used.

    A draft cannot be unpublished: delete it instead.

    Unpublishing is terminal: the report no longer appears in List or Show, and cannot be
    published again. The reason is shown to anyone who still has a permalink.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayReportsUnpublishPayloadV2):  Example: {'unpublish_reason': 'The date range is
            wrong and one schedule was incorrectly synced.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayReportsUnpublishResultV2]
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
    body: PayReportsUnpublishPayloadV2,
) -> ErrorResponse | PayReportsUnpublishResultV2 | None:
    """Unpublish Pay Reports V2

     Unpublish a published pay report, recording a reason it should not be used.

    A draft cannot be unpublished: delete it instead.

    Unpublishing is terminal: the report no longer appears in List or Show, and cannot be
    published again. The reason is shown to anyone who still has a permalink.

    Args:
        id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayReportsUnpublishPayloadV2):  Example: {'unpublish_reason': 'The date range is
            wrong and one schedule was incorrectly synced.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayReportsUnpublishResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
