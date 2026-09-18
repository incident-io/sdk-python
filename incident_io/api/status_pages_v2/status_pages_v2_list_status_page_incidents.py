import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.status_pages_list_status_page_incidents_result_v2 import (
    StatusPagesListStatusPageIncidentsResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status_page_id: str,
    component_id: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    sub_page_id: str | Unset = UNSET,
    start_at: datetime.datetime | Unset = UNSET,
    end_at: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status_page_id"] = status_page_id

    params["component_id"] = component_id

    params["group_id"] = group_id

    params["sub_page_id"] = sub_page_id

    json_start_at: str | Unset = UNSET
    if not isinstance(start_at, Unset):
        json_start_at = start_at.isoformat()
    params["start_at"] = json_start_at

    json_end_at: str | Unset = UNSET
    if not isinstance(end_at, Unset):
        json_end_at = end_at.isoformat()
    params["end_at"] = json_end_at

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/status_page_incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StatusPagesListStatusPageIncidentsResultV2 | None:
    if response.status_code == 200:
        response_200 = StatusPagesListStatusPageIncidentsResultV2.from_dict(
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
) -> Response[ErrorResponse | StatusPagesListStatusPageIncidentsResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status_page_id: str,
    component_id: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    sub_page_id: str | Unset = UNSET,
    start_at: datetime.datetime | Unset = UNSET,
    end_at: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | StatusPagesListStatusPageIncidentsResultV2]:
    """ListStatusPageIncidents Status Pages V2

     List status page incidents.

    This endpoint requires a valid API key but no specific scopes.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str | Unset): Filter status page incidents to only those that impacted the
            specified component. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        group_id (str | Unset): Filter status page incidents to only those that impacted
            components in the specified group. This ID may be found by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG2.
        sub_page_id (str | Unset): Filter status page incidents to only those that impacted the
            specified sub-page. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG3.
        start_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or after this time. Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or before this time. Example: 2021-08-17T13:28:57.801578Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesListStatusPageIncidentsResultV2]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        component_id=component_id,
        group_id=group_id,
        sub_page_id=sub_page_id,
        start_at=start_at,
        end_at=end_at,
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
    status_page_id: str,
    component_id: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    sub_page_id: str | Unset = UNSET,
    start_at: datetime.datetime | Unset = UNSET,
    end_at: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | StatusPagesListStatusPageIncidentsResultV2 | None:
    """ListStatusPageIncidents Status Pages V2

     List status page incidents.

    This endpoint requires a valid API key but no specific scopes.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str | Unset): Filter status page incidents to only those that impacted the
            specified component. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        group_id (str | Unset): Filter status page incidents to only those that impacted
            components in the specified group. This ID may be found by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG2.
        sub_page_id (str | Unset): Filter status page incidents to only those that impacted the
            specified sub-page. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG3.
        start_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or after this time. Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or before this time. Example: 2021-08-17T13:28:57.801578Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesListStatusPageIncidentsResultV2
    """

    return sync_detailed(
        client=client,
        status_page_id=status_page_id,
        component_id=component_id,
        group_id=group_id,
        sub_page_id=sub_page_id,
        start_at=start_at,
        end_at=end_at,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status_page_id: str,
    component_id: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    sub_page_id: str | Unset = UNSET,
    start_at: datetime.datetime | Unset = UNSET,
    end_at: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | StatusPagesListStatusPageIncidentsResultV2]:
    """ListStatusPageIncidents Status Pages V2

     List status page incidents.

    This endpoint requires a valid API key but no specific scopes.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str | Unset): Filter status page incidents to only those that impacted the
            specified component. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        group_id (str | Unset): Filter status page incidents to only those that impacted
            components in the specified group. This ID may be found by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG2.
        sub_page_id (str | Unset): Filter status page incidents to only those that impacted the
            specified sub-page. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG3.
        start_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or after this time. Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or before this time. Example: 2021-08-17T13:28:57.801578Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesListStatusPageIncidentsResultV2]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        component_id=component_id,
        group_id=group_id,
        sub_page_id=sub_page_id,
        start_at=start_at,
        end_at=end_at,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status_page_id: str,
    component_id: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    sub_page_id: str | Unset = UNSET,
    start_at: datetime.datetime | Unset = UNSET,
    end_at: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | StatusPagesListStatusPageIncidentsResultV2 | None:
    """ListStatusPageIncidents Status Pages V2

     List status page incidents.

    This endpoint requires a valid API key but no specific scopes.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str | Unset): Filter status page incidents to only those that impacted the
            specified component. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        group_id (str | Unset): Filter status page incidents to only those that impacted
            components in the specified group. This ID may be found by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG2.
        sub_page_id (str | Unset): Filter status page incidents to only those that impacted the
            specified sub-page. This ID may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG3.
        start_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or after this time. Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime | Unset): Filter status page incidents to only those that had
            impacts during or before this time. Example: 2021-08-17T13:28:57.801578Z.
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An record's ID. This endpoint will return a list of records after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesListStatusPageIncidentsResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            status_page_id=status_page_id,
            component_id=component_id,
            group_id=group_id,
            sub_page_id=sub_page_id,
            start_at=start_at,
            end_at=end_at,
            page_size=page_size,
            after=after,
        )
    ).parsed
