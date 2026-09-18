from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_list_schedule_sync_rules_result_v2 import (
    SchedulesListScheduleSyncRulesResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    schedule_id: str,
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/schedules/{schedule_id}/sync_rules".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesListScheduleSyncRulesResultV2 | None:
    if response.status_code == 200:
        response_200 = SchedulesListScheduleSyncRulesResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | SchedulesListScheduleSyncRulesResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | SchedulesListScheduleSyncRulesResultV2]:
    """ListScheduleSyncRules Schedules V2

     List the sync rules configured on this schedule.

    Args:
        schedule_id (str): The schedule to list sync rules for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A sync rule's ID. This endpoint will return a list of sync rules
            after this ID in relation to the API response order. Example: 01JXYZ000000000000000000CD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesListScheduleSyncRulesResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | SchedulesListScheduleSyncRulesResultV2 | None:
    """ListScheduleSyncRules Schedules V2

     List the sync rules configured on this schedule.

    Args:
        schedule_id (str): The schedule to list sync rules for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A sync rule's ID. This endpoint will return a list of sync rules
            after this ID in relation to the API response order. Example: 01JXYZ000000000000000000CD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesListScheduleSyncRulesResultV2
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | SchedulesListScheduleSyncRulesResultV2]:
    """ListScheduleSyncRules Schedules V2

     List the sync rules configured on this schedule.

    Args:
        schedule_id (str): The schedule to list sync rules for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A sync rule's ID. This endpoint will return a list of sync rules
            after this ID in relation to the API response order. Example: 01JXYZ000000000000000000CD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesListScheduleSyncRulesResultV2]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | SchedulesListScheduleSyncRulesResultV2 | None:
    """ListScheduleSyncRules Schedules V2

     List the sync rules configured on this schedule.

    Args:
        schedule_id (str): The schedule to list sync rules for Example:
            01FDAG4SAP5TYPT98WGR2N7W91.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): A sync rule's ID. This endpoint will return a list of sync rules
            after this ID in relation to the API response order. Example: 01JXYZ000000000000000000CD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesListScheduleSyncRulesResultV2
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            page_size=page_size,
            after=after,
        )
    ).parsed
