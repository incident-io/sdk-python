from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.follow_ups_connect_external_issue_payload_v2 import (
    FollowUpsConnectExternalIssuePayloadV2,
)
from ...models.follow_ups_connect_external_issue_result_v2 import (
    FollowUpsConnectExternalIssueResultV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: FollowUpsConnectExternalIssuePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/follow_ups/{id}/actions/connect_external_issue".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FollowUpsConnectExternalIssueResultV2 | None:
    if response.status_code == 200:
        response_200 = FollowUpsConnectExternalIssueResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | FollowUpsConnectExternalIssueResultV2]:
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
    body: FollowUpsConnectExternalIssuePayloadV2,
) -> Response[ErrorResponse | FollowUpsConnectExternalIssueResultV2]:
    """ConnectExternalIssue Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST
    /v3/follow_ups/{id}/actions/connect_external_issue</code> instead.

    Connect a follow-up to an existing issue in an issue tracker, using the URL of the issue.

    This will not work if the follow-up is already connected to an external issue.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (FollowUpsConnectExternalIssuePayloadV2):  Example: {'provider': 'linear', 'url':
            'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsConnectExternalIssueResultV2]
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
    body: FollowUpsConnectExternalIssuePayloadV2,
) -> ErrorResponse | FollowUpsConnectExternalIssueResultV2 | None:
    """ConnectExternalIssue Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST
    /v3/follow_ups/{id}/actions/connect_external_issue</code> instead.

    Connect a follow-up to an existing issue in an issue tracker, using the URL of the issue.

    This will not work if the follow-up is already connected to an external issue.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (FollowUpsConnectExternalIssuePayloadV2):  Example: {'provider': 'linear', 'url':
            'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsConnectExternalIssueResultV2
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
    body: FollowUpsConnectExternalIssuePayloadV2,
) -> Response[ErrorResponse | FollowUpsConnectExternalIssueResultV2]:
    """ConnectExternalIssue Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST
    /v3/follow_ups/{id}/actions/connect_external_issue</code> instead.

    Connect a follow-up to an existing issue in an issue tracker, using the URL of the issue.

    This will not work if the follow-up is already connected to an external issue.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (FollowUpsConnectExternalIssuePayloadV2):  Example: {'provider': 'linear', 'url':
            'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsConnectExternalIssueResultV2]
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
    body: FollowUpsConnectExternalIssuePayloadV2,
) -> ErrorResponse | FollowUpsConnectExternalIssueResultV2 | None:
    """ConnectExternalIssue Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST
    /v3/follow_ups/{id}/actions/connect_external_issue</code> instead.

    Connect a follow-up to an existing issue in an issue tracker, using the URL of the issue.

    This will not work if the follow-up is already connected to an external issue.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (FollowUpsConnectExternalIssuePayloadV2):  Example: {'provider': 'linear', 'url':
            'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsConnectExternalIssueResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed

# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools
import warnings as _warnings


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(
            "POST /v2/follow_ups/{id}/actions/connect_external_issue is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated(asyncio_detailed)
asyncio = _deprecated(asyncio)
