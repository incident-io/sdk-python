from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.follow_ups_create_from_link_payload_v3 import (
    FollowUpsCreateFromLinkPayloadV3,
)
from ...models.follow_ups_create_from_link_result_v3 import (
    FollowUpsCreateFromLinkResultV3,
)
from ...types import Response


def _get_kwargs(
    *,
    body: FollowUpsCreateFromLinkPayloadV3,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/follow_ups/actions/create_from_link",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FollowUpsCreateFromLinkResultV3 | None:
    if response.status_code == 201:
        response_201 = FollowUpsCreateFromLinkResultV3.from_dict(response.json())

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
) -> Response[ErrorResponse | FollowUpsCreateFromLinkResultV3]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreateFromLinkPayloadV3,
) -> Response[ErrorResponse | FollowUpsCreateFromLinkResultV3]:
    """CreateFromLink Follow-ups V3

     Create a follow-up from the URL of an issue that already exists in an issue tracker.

    The follow-up is created already connected to that issue, so it will not also be exported to
    a new one. Prefer this over creating a follow-up and then connecting it: that sequence races
    the automatic export, which can leave you with a duplicate issue or a connect call that
    fails because the export won.

    The follow-up's title, description and assignee are taken from the issue, and it is
    backdated to the issue's creation time. Its priority is taken from the issue only if your
    organisation has priority sync enabled, and otherwise falls back to your default priority.

    Issues that are already closed are accepted: the follow-up records the issue's completion
    time, though it is still created with an <code>outstanding</code> status until the next
    sync from the issue tracker.

    If your organisation requires a follow-up owner and the issue is unassigned, the incident
    lead is used instead. Where there is no incident lead either, this returns a validation
    error rather than creating an unowned follow-up.

    Args:
        body (FollowUpsCreateFromLinkPayloadV3):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'url': 'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsCreateFromLinkResultV3]
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
    body: FollowUpsCreateFromLinkPayloadV3,
) -> ErrorResponse | FollowUpsCreateFromLinkResultV3 | None:
    """CreateFromLink Follow-ups V3

     Create a follow-up from the URL of an issue that already exists in an issue tracker.

    The follow-up is created already connected to that issue, so it will not also be exported to
    a new one. Prefer this over creating a follow-up and then connecting it: that sequence races
    the automatic export, which can leave you with a duplicate issue or a connect call that
    fails because the export won.

    The follow-up's title, description and assignee are taken from the issue, and it is
    backdated to the issue's creation time. Its priority is taken from the issue only if your
    organisation has priority sync enabled, and otherwise falls back to your default priority.

    Issues that are already closed are accepted: the follow-up records the issue's completion
    time, though it is still created with an <code>outstanding</code> status until the next
    sync from the issue tracker.

    If your organisation requires a follow-up owner and the issue is unassigned, the incident
    lead is used instead. Where there is no incident lead either, this returns a validation
    error rather than creating an unowned follow-up.

    Args:
        body (FollowUpsCreateFromLinkPayloadV3):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'url': 'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsCreateFromLinkResultV3
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreateFromLinkPayloadV3,
) -> Response[ErrorResponse | FollowUpsCreateFromLinkResultV3]:
    """CreateFromLink Follow-ups V3

     Create a follow-up from the URL of an issue that already exists in an issue tracker.

    The follow-up is created already connected to that issue, so it will not also be exported to
    a new one. Prefer this over creating a follow-up and then connecting it: that sequence races
    the automatic export, which can leave you with a duplicate issue or a connect call that
    fails because the export won.

    The follow-up's title, description and assignee are taken from the issue, and it is
    backdated to the issue's creation time. Its priority is taken from the issue only if your
    organisation has priority sync enabled, and otherwise falls back to your default priority.

    Issues that are already closed are accepted: the follow-up records the issue's completion
    time, though it is still created with an <code>outstanding</code> status until the next
    sync from the issue tracker.

    If your organisation requires a follow-up owner and the issue is unassigned, the incident
    lead is used instead. Where there is no incident lead either, this returns a validation
    error rather than creating an unowned follow-up.

    Args:
        body (FollowUpsCreateFromLinkPayloadV3):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'url': 'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsCreateFromLinkResultV3]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreateFromLinkPayloadV3,
) -> ErrorResponse | FollowUpsCreateFromLinkResultV3 | None:
    """CreateFromLink Follow-ups V3

     Create a follow-up from the URL of an issue that already exists in an issue tracker.

    The follow-up is created already connected to that issue, so it will not also be exported to
    a new one. Prefer this over creating a follow-up and then connecting it: that sequence races
    the automatic export, which can leave you with a duplicate issue or a connect call that
    fails because the export won.

    The follow-up's title, description and assignee are taken from the issue, and it is
    backdated to the issue's creation time. Its priority is taken from the issue only if your
    organisation has priority sync enabled, and otherwise falls back to your default priority.

    Issues that are already closed are accepted: the follow-up records the issue's completion
    time, though it is still created with an <code>outstanding</code> status until the next
    sync from the issue tracker.

    If your organisation requires a follow-up owner and the issue is unassigned, the incident
    lead is used instead. Where there is no incident lead either, this returns a validation
    error rather than creating an unowned follow-up.

    Args:
        body (FollowUpsCreateFromLinkPayloadV3):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'url': 'https://linear.app/incident/issue/INC-123'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsCreateFromLinkResultV3
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
