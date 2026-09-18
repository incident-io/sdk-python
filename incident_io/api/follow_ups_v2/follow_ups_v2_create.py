from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.follow_ups_create_payload_v2 import FollowUpsCreatePayloadV2
from ...models.follow_ups_create_result_v2 import FollowUpsCreateResultV2
from ...types import Response


def _get_kwargs(
    *,
    body: FollowUpsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/follow_ups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FollowUpsCreateResultV2 | None:
    if response.status_code == 201:
        response_201 = FollowUpsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | FollowUpsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreatePayloadV2,
) -> Response[ErrorResponse | FollowUpsCreateResultV2]:
    """Create Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST /v3/follow_ups</code>
    instead.

    Create a new incident follow-up.

    Args:
        body (FollowUpsCreatePayloadV2):  Example: {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade',
            'external_issue_reference_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'follow_up_category_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'labels':
            ['bug', 'urgent'], 'title': 'Add alerting on replica lag'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsCreateResultV2]
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
    body: FollowUpsCreatePayloadV2,
) -> ErrorResponse | FollowUpsCreateResultV2 | None:
    """Create Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST /v3/follow_ups</code>
    instead.

    Create a new incident follow-up.

    Args:
        body (FollowUpsCreatePayloadV2):  Example: {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade',
            'external_issue_reference_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'follow_up_category_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'labels':
            ['bug', 'urgent'], 'title': 'Add alerting on replica lag'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreatePayloadV2,
) -> Response[ErrorResponse | FollowUpsCreateResultV2]:
    """Create Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST /v3/follow_ups</code>
    instead.

    Create a new incident follow-up.

    Args:
        body (FollowUpsCreatePayloadV2):  Example: {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade',
            'external_issue_reference_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'follow_up_category_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'labels':
            ['bug', 'urgent'], 'title': 'Add alerting on replica lag'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FollowUpsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FollowUpsCreatePayloadV2,
) -> ErrorResponse | FollowUpsCreateResultV2 | None:
    """Create Follow-ups V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>POST /v3/follow_ups</code>
    instead.

    Create a new incident follow-up.

    Args:
        body (FollowUpsCreatePayloadV2):  Example: {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'assignee_team_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade',
            'external_issue_reference_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'follow_up_category_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'follow_up_priority_option_id':
            '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'labels':
            ['bug', 'urgent'], 'title': 'Add alerting on replica lag'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FollowUpsCreateResultV2
    """

    return (
        await asyncio_detailed(
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
            "POST /v2/follow_ups is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated(asyncio_detailed)
asyncio = _deprecated(asyncio)
