import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_list_schedule_entries_result_v2 import (
    SchedulesListScheduleEntriesResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    schedule_id: str,
    entry_window_start: str | Unset = UNSET,
    entry_window_end: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["schedule_id"] = schedule_id

    params["entry_window_start"] = entry_window_start

    json_entry_window_end: str | Unset = UNSET
    if not isinstance(entry_window_end, Unset):
        json_entry_window_end = entry_window_end.isoformat()
    params["entry_window_end"] = json_entry_window_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/schedule_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesListScheduleEntriesResultV2 | None:
    if response.status_code == 200:
        response_200 = SchedulesListScheduleEntriesResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | SchedulesListScheduleEntriesResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    schedule_id: str,
    entry_window_start: str | Unset = UNSET,
    entry_window_end: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | SchedulesListScheduleEntriesResultV2]:
    """ListScheduleEntries Schedules V2

     List the schedule entries for a schedule over a window of time.

    Use this endpoint to find out who is on-call for a schedule, either right now or
    at any point in the future. Common uses include:

    - Building a calendar or timeline view of who is on-call.
    - Looking up who was on-call at a particular moment (for example, when an
      incident fired).
    - Exporting upcoming shifts into another system, such as a payroll or
      scheduling tool.

    The response groups entries into three lists: `scheduled` (the entries the
    rotation rules produce, before any overrides), `overrides` (any one-off
    overrides that apply in the window) and `final` (the effective schedule
    after overrides have been merged in — this is normally the list you want).

    Each entry includes the `rotation_id` and `layer_id` it belongs to.
    Schedules can be made up of multiple rotations (for example, a primary and
    a secondary rotation) and each rotation can have several layers, and we
    return entries for every rotation and layer on the schedule.

    The endpoint returns all entries that overlap with the given window. If no
    window is provided we default to a sensible range starting from now.

    ## Pagination

    Responses are paginated. When more entries are available than fit on a single
    page, the response includes a `pagination_meta` block with two fields:

    - `after_url` — a fully-formed URL for the next page. The simplest way
      to paginate is to keep following this URL until it is no longer present.
    - `after` — an opaque cursor token. To fetch the next page manually,
      re-issue the request with `entry_window_start` set to this value and
      `entry_window_end` left unchanged from the original request. Treat
      the token as opaque — do not parse or modify it.

    Keep paginating until `pagination_meta` is absent from the response, at
    which point you have received every entry in the window.

    Args:
        schedule_id (str): The ID of the schedule to get entries for. Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        entry_window_start (str | Unset): The start of the window to get entries for. May also
            carry an opaque pagination cursor previously returned in `pagination_meta.after` — pass it
            back here unchanged to fetch the next page (leave `entry_window_end` unchanged from the
            original request). Example: 2021-01-01T00:00:00Z.
        entry_window_end (datetime.datetime | Unset): The end of the window to get entries for.
            Example: 2021-01-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesListScheduleEntriesResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    schedule_id: str,
    entry_window_start: str | Unset = UNSET,
    entry_window_end: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | SchedulesListScheduleEntriesResultV2 | None:
    """ListScheduleEntries Schedules V2

     List the schedule entries for a schedule over a window of time.

    Use this endpoint to find out who is on-call for a schedule, either right now or
    at any point in the future. Common uses include:

    - Building a calendar or timeline view of who is on-call.
    - Looking up who was on-call at a particular moment (for example, when an
      incident fired).
    - Exporting upcoming shifts into another system, such as a payroll or
      scheduling tool.

    The response groups entries into three lists: `scheduled` (the entries the
    rotation rules produce, before any overrides), `overrides` (any one-off
    overrides that apply in the window) and `final` (the effective schedule
    after overrides have been merged in — this is normally the list you want).

    Each entry includes the `rotation_id` and `layer_id` it belongs to.
    Schedules can be made up of multiple rotations (for example, a primary and
    a secondary rotation) and each rotation can have several layers, and we
    return entries for every rotation and layer on the schedule.

    The endpoint returns all entries that overlap with the given window. If no
    window is provided we default to a sensible range starting from now.

    ## Pagination

    Responses are paginated. When more entries are available than fit on a single
    page, the response includes a `pagination_meta` block with two fields:

    - `after_url` — a fully-formed URL for the next page. The simplest way
      to paginate is to keep following this URL until it is no longer present.
    - `after` — an opaque cursor token. To fetch the next page manually,
      re-issue the request with `entry_window_start` set to this value and
      `entry_window_end` left unchanged from the original request. Treat
      the token as opaque — do not parse or modify it.

    Keep paginating until `pagination_meta` is absent from the response, at
    which point you have received every entry in the window.

    Args:
        schedule_id (str): The ID of the schedule to get entries for. Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        entry_window_start (str | Unset): The start of the window to get entries for. May also
            carry an opaque pagination cursor previously returned in `pagination_meta.after` — pass it
            back here unchanged to fetch the next page (leave `entry_window_end` unchanged from the
            original request). Example: 2021-01-01T00:00:00Z.
        entry_window_end (datetime.datetime | Unset): The end of the window to get entries for.
            Example: 2021-01-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesListScheduleEntriesResultV2
    """

    return sync_detailed(
        client=client,
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    schedule_id: str,
    entry_window_start: str | Unset = UNSET,
    entry_window_end: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | SchedulesListScheduleEntriesResultV2]:
    """ListScheduleEntries Schedules V2

     List the schedule entries for a schedule over a window of time.

    Use this endpoint to find out who is on-call for a schedule, either right now or
    at any point in the future. Common uses include:

    - Building a calendar or timeline view of who is on-call.
    - Looking up who was on-call at a particular moment (for example, when an
      incident fired).
    - Exporting upcoming shifts into another system, such as a payroll or
      scheduling tool.

    The response groups entries into three lists: `scheduled` (the entries the
    rotation rules produce, before any overrides), `overrides` (any one-off
    overrides that apply in the window) and `final` (the effective schedule
    after overrides have been merged in — this is normally the list you want).

    Each entry includes the `rotation_id` and `layer_id` it belongs to.
    Schedules can be made up of multiple rotations (for example, a primary and
    a secondary rotation) and each rotation can have several layers, and we
    return entries for every rotation and layer on the schedule.

    The endpoint returns all entries that overlap with the given window. If no
    window is provided we default to a sensible range starting from now.

    ## Pagination

    Responses are paginated. When more entries are available than fit on a single
    page, the response includes a `pagination_meta` block with two fields:

    - `after_url` — a fully-formed URL for the next page. The simplest way
      to paginate is to keep following this URL until it is no longer present.
    - `after` — an opaque cursor token. To fetch the next page manually,
      re-issue the request with `entry_window_start` set to this value and
      `entry_window_end` left unchanged from the original request. Treat
      the token as opaque — do not parse or modify it.

    Keep paginating until `pagination_meta` is absent from the response, at
    which point you have received every entry in the window.

    Args:
        schedule_id (str): The ID of the schedule to get entries for. Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        entry_window_start (str | Unset): The start of the window to get entries for. May also
            carry an opaque pagination cursor previously returned in `pagination_meta.after` — pass it
            back here unchanged to fetch the next page (leave `entry_window_end` unchanged from the
            original request). Example: 2021-01-01T00:00:00Z.
        entry_window_end (datetime.datetime | Unset): The end of the window to get entries for.
            Example: 2021-01-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesListScheduleEntriesResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    schedule_id: str,
    entry_window_start: str | Unset = UNSET,
    entry_window_end: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | SchedulesListScheduleEntriesResultV2 | None:
    """ListScheduleEntries Schedules V2

     List the schedule entries for a schedule over a window of time.

    Use this endpoint to find out who is on-call for a schedule, either right now or
    at any point in the future. Common uses include:

    - Building a calendar or timeline view of who is on-call.
    - Looking up who was on-call at a particular moment (for example, when an
      incident fired).
    - Exporting upcoming shifts into another system, such as a payroll or
      scheduling tool.

    The response groups entries into three lists: `scheduled` (the entries the
    rotation rules produce, before any overrides), `overrides` (any one-off
    overrides that apply in the window) and `final` (the effective schedule
    after overrides have been merged in — this is normally the list you want).

    Each entry includes the `rotation_id` and `layer_id` it belongs to.
    Schedules can be made up of multiple rotations (for example, a primary and
    a secondary rotation) and each rotation can have several layers, and we
    return entries for every rotation and layer on the schedule.

    The endpoint returns all entries that overlap with the given window. If no
    window is provided we default to a sensible range starting from now.

    ## Pagination

    Responses are paginated. When more entries are available than fit on a single
    page, the response includes a `pagination_meta` block with two fields:

    - `after_url` — a fully-formed URL for the next page. The simplest way
      to paginate is to keep following this URL until it is no longer present.
    - `after` — an opaque cursor token. To fetch the next page manually,
      re-issue the request with `entry_window_start` set to this value and
      `entry_window_end` left unchanged from the original request. Treat
      the token as opaque — do not parse or modify it.

    Keep paginating until `pagination_meta` is absent from the response, at
    which point you have received every entry in the window.

    Args:
        schedule_id (str): The ID of the schedule to get entries for. Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        entry_window_start (str | Unset): The start of the window to get entries for. May also
            carry an opaque pagination cursor previously returned in `pagination_meta.after` — pass it
            back here unchanged to fetch the next page (leave `entry_window_end` unchanged from the
            original request). Example: 2021-01-01T00:00:00Z.
        entry_window_end (datetime.datetime | Unset): The end of the window to get entries for.
            Example: 2021-01-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesListScheduleEntriesResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            schedule_id=schedule_id,
            entry_window_start=entry_window_start,
            entry_window_end=entry_window_end,
        )
    ).parsed
