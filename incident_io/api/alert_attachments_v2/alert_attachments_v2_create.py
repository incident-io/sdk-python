from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_attachments_create_payload_v2 import (
    AlertAttachmentsCreatePayloadV2,
)
from ...models.alert_attachments_create_result_v2 import AlertAttachmentsCreateResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlertAttachmentsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/alert_attachments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertAttachmentsCreateResultV2 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = AlertAttachmentsCreateResultV2.from_dict(response.json())

        return response_201

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
) -> Response[AlertAttachmentsCreateResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAttachmentsCreatePayloadV2,
) -> Response[AlertAttachmentsCreateResultV2 | ErrorResponse]:
    """Create Alert Attachments V2

     Attach a URL to an alert or alert group. Provide exactly one of alert_id or alert_group_id. A URL
    for a ticket or pull request from a connected integration is attached as that ticket or pull
    request. Any other URL is attached as a link. A URL that is already attached returns a 422.

    Args:
        body (AlertAttachmentsCreatePayloadV2):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'title': 'Disk
            usage dashboard', 'url': 'https://linear.app/acme/issue/ENG-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertAttachmentsCreateResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAttachmentsCreatePayloadV2,
) -> AlertAttachmentsCreateResultV2 | ErrorResponse | None:
    """Create Alert Attachments V2

     Attach a URL to an alert or alert group. Provide exactly one of alert_id or alert_group_id. A URL
    for a ticket or pull request from a connected integration is attached as that ticket or pull
    request. Any other URL is attached as a link. A URL that is already attached returns a 422.

    Args:
        body (AlertAttachmentsCreatePayloadV2):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'title': 'Disk
            usage dashboard', 'url': 'https://linear.app/acme/issue/ENG-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertAttachmentsCreateResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAttachmentsCreatePayloadV2,
) -> Response[AlertAttachmentsCreateResultV2 | ErrorResponse]:
    """Create Alert Attachments V2

     Attach a URL to an alert or alert group. Provide exactly one of alert_id or alert_group_id. A URL
    for a ticket or pull request from a connected integration is attached as that ticket or pull
    request. Any other URL is attached as a link. A URL that is already attached returns a 422.

    Args:
        body (AlertAttachmentsCreatePayloadV2):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'title': 'Disk
            usage dashboard', 'url': 'https://linear.app/acme/issue/ENG-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertAttachmentsCreateResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAttachmentsCreatePayloadV2,
) -> AlertAttachmentsCreateResultV2 | ErrorResponse | None:
    """Create Alert Attachments V2

     Attach a URL to an alert or alert group. Provide exactly one of alert_id or alert_group_id. A URL
    for a ticket or pull request from a connected integration is attached as that ticket or pull
    request. Any other URL is attached as a link. A URL that is already attached returns a 422.

    Args:
        body (AlertAttachmentsCreatePayloadV2):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'title': 'Disk
            usage dashboard', 'url': 'https://linear.app/acme/issue/ENG-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertAttachmentsCreateResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
