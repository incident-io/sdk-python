import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_participant_workloads_list_hours_result_v2 import (
    IncidentParticipantWorkloadsListHoursResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["incident_id"] = incident_id

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/incident_participant_workload_hours",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2 | None:
    if response.status_code == 200:
        response_200 = IncidentParticipantWorkloadsListHoursResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2]:
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
    before: datetime.datetime | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2]:
    """ListHours IncidentParticipantWorkloads V2

     List each user's workload on each incident, hour by hour, newest first.

    Each row is the time one user spent on one incident in one hour. Sum the rows to get any
    total you need, such as the time each person spent on incidents last month. Rows come
    newest first. To cover a period, set `before` to its end, then follow
    `pagination_meta.after` until you reach rows older than its start. A page can hold
    fewer rows than `page_size`, so keep following `after` until it is absent.

    Workload is calculated periodically, so values can lag real time and the most recent period
    may still be filling. The metadata reports the time the figures are calculated up to.

    Workload on private incidents is only included for API keys with the
    `incident_workloads.view.private_incidents` scope.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): The cursor from a previous response's `pagination_meta.after`.
            Returns the rows older than that page. Example:
            1795345200_01FCNDV6P870EA6S7TK1DSYD5H_01FCNDV6P870EA6S7TK1DSYD5J.
        before (datetime.datetime | Unset): Only return hours that start before this time Example:
            2026-11-01T00:00:00Z.
        incident_id (str | Unset): Only return workload on this incident Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        user_id (str | Unset): Only return workload for this user Example:
            01FCNDV6P870EA6S7TK1DSYD5J.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        before=before,
        incident_id=incident_id,
        user_id=user_id,
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
    before: datetime.datetime | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2 | None:
    """ListHours IncidentParticipantWorkloads V2

     List each user's workload on each incident, hour by hour, newest first.

    Each row is the time one user spent on one incident in one hour. Sum the rows to get any
    total you need, such as the time each person spent on incidents last month. Rows come
    newest first. To cover a period, set `before` to its end, then follow
    `pagination_meta.after` until you reach rows older than its start. A page can hold
    fewer rows than `page_size`, so keep following `after` until it is absent.

    Workload is calculated periodically, so values can lag real time and the most recent period
    may still be filling. The metadata reports the time the figures are calculated up to.

    Workload on private incidents is only included for API keys with the
    `incident_workloads.view.private_incidents` scope.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): The cursor from a previous response's `pagination_meta.after`.
            Returns the rows older than that page. Example:
            1795345200_01FCNDV6P870EA6S7TK1DSYD5H_01FCNDV6P870EA6S7TK1DSYD5J.
        before (datetime.datetime | Unset): Only return hours that start before this time Example:
            2026-11-01T00:00:00Z.
        incident_id (str | Unset): Only return workload on this incident Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        user_id (str | Unset): Only return workload for this user Example:
            01FCNDV6P870EA6S7TK1DSYD5J.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        before=before,
        incident_id=incident_id,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2]:
    """ListHours IncidentParticipantWorkloads V2

     List each user's workload on each incident, hour by hour, newest first.

    Each row is the time one user spent on one incident in one hour. Sum the rows to get any
    total you need, such as the time each person spent on incidents last month. Rows come
    newest first. To cover a period, set `before` to its end, then follow
    `pagination_meta.after` until you reach rows older than its start. A page can hold
    fewer rows than `page_size`, so keep following `after` until it is absent.

    Workload is calculated periodically, so values can lag real time and the most recent period
    may still be filling. The metadata reports the time the figures are calculated up to.

    Workload on private incidents is only included for API keys with the
    `incident_workloads.view.private_incidents` scope.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): The cursor from a previous response's `pagination_meta.after`.
            Returns the rows older than that page. Example:
            1795345200_01FCNDV6P870EA6S7TK1DSYD5H_01FCNDV6P870EA6S7TK1DSYD5J.
        before (datetime.datetime | Unset): Only return hours that start before this time Example:
            2026-11-01T00:00:00Z.
        incident_id (str | Unset): Only return workload on this incident Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        user_id (str | Unset): Only return workload for this user Example:
            01FCNDV6P870EA6S7TK1DSYD5J.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        before=before,
        incident_id=incident_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2 | None:
    """ListHours IncidentParticipantWorkloads V2

     List each user's workload on each incident, hour by hour, newest first.

    Each row is the time one user spent on one incident in one hour. Sum the rows to get any
    total you need, such as the time each person spent on incidents last month. Rows come
    newest first. To cover a period, set `before` to its end, then follow
    `pagination_meta.after` until you reach rows older than its start. A page can hold
    fewer rows than `page_size`, so keep following `after` until it is absent.

    Workload is calculated periodically, so values can lag real time and the most recent period
    may still be filling. The metadata reports the time the figures are calculated up to.

    Workload on private incidents is only included for API keys with the
    `incident_workloads.view.private_incidents` scope.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): The cursor from a previous response's `pagination_meta.after`.
            Returns the rows older than that page. Example:
            1795345200_01FCNDV6P870EA6S7TK1DSYD5H_01FCNDV6P870EA6S7TK1DSYD5J.
        before (datetime.datetime | Unset): Only return hours that start before this time Example:
            2026-11-01T00:00:00Z.
        incident_id (str | Unset): Only return workload on this incident Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        user_id (str | Unset): Only return workload for this user Example:
            01FCNDV6P870EA6S7TK1DSYD5J.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentParticipantWorkloadsListHoursResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            before=before,
            incident_id=incident_id,
            user_id=user_id,
        )
    ).parsed
