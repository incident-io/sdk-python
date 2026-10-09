import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.on_call_notification_pauses_list_result_v2 import (
    OnCallNotificationPausesListResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/on_call_notification_pauses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OnCallNotificationPausesListResultV2 | None:
    if response.status_code == 200:
        response_200 = OnCallNotificationPausesListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | OnCallNotificationPausesListResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | OnCallNotificationPausesListResultV2]:
    """List On-call Notification Pauses V2

     List on-call notification pauses across the organisation. By default this returns pauses that are
    active now or scheduled for the future. Cancelled pauses are never returned, and pauses that were
    resumed early have ends_at set to when they were resumed.

    Args:
        from_ (datetime.datetime | Unset): Only return pauses that end after this time. Defaults
            to now, so by default only active and upcoming pauses are returned. Example:
            2021-08-17T00:00:00Z.
        to (datetime.datetime | Unset): Only return pauses that start before this time Example:
            2021-08-24T00:00:00Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A pause's ID. This endpoint will return a list of pauses after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OnCallNotificationPausesListResultV2]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | OnCallNotificationPausesListResultV2 | None:
    """List On-call Notification Pauses V2

     List on-call notification pauses across the organisation. By default this returns pauses that are
    active now or scheduled for the future. Cancelled pauses are never returned, and pauses that were
    resumed early have ends_at set to when they were resumed.

    Args:
        from_ (datetime.datetime | Unset): Only return pauses that end after this time. Defaults
            to now, so by default only active and upcoming pauses are returned. Example:
            2021-08-17T00:00:00Z.
        to (datetime.datetime | Unset): Only return pauses that start before this time Example:
            2021-08-24T00:00:00Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A pause's ID. This endpoint will return a list of pauses after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OnCallNotificationPausesListResultV2
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | OnCallNotificationPausesListResultV2]:
    """List On-call Notification Pauses V2

     List on-call notification pauses across the organisation. By default this returns pauses that are
    active now or scheduled for the future. Cancelled pauses are never returned, and pauses that were
    resumed early have ends_at set to when they were resumed.

    Args:
        from_ (datetime.datetime | Unset): Only return pauses that end after this time. Defaults
            to now, so by default only active and upcoming pauses are returned. Example:
            2021-08-17T00:00:00Z.
        to (datetime.datetime | Unset): Only return pauses that start before this time Example:
            2021-08-24T00:00:00Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A pause's ID. This endpoint will return a list of pauses after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OnCallNotificationPausesListResultV2]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | OnCallNotificationPausesListResultV2 | None:
    """List On-call Notification Pauses V2

     List on-call notification pauses across the organisation. By default this returns pauses that are
    active now or scheduled for the future. Cancelled pauses are never returned, and pauses that were
    resumed early have ends_at set to when they were resumed.

    Args:
        from_ (datetime.datetime | Unset): Only return pauses that end after this time. Defaults
            to now, so by default only active and upcoming pauses are returned. Example:
            2021-08-17T00:00:00Z.
        to (datetime.datetime | Unset): Only return pauses that start before this time Example:
            2021-08-24T00:00:00Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A pause's ID. This endpoint will return a list of pauses after this
            ID in relation to the API response order. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OnCallNotificationPausesListResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            page_size=page_size,
            after=after,
        )
    ).parsed
