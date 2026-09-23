import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.status_pages_show_status_page_component_availability_result_v2 import (
    StatusPagesShowStatusPageComponentAvailabilityResultV2,
)
from ...types import UNSET, Response


def _get_kwargs(
    status_page_id: str,
    component_id: str,
    *,
    start_at: datetime.datetime,
    end_at: datetime.datetime,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_at = start_at.isoformat()
    params["start_at"] = json_start_at

    json_end_at = end_at.isoformat()
    params["end_at"] = json_end_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/status_pages/{status_page_id}/components/{component_id}/availability".format(
            status_page_id=quote(str(status_page_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2 | None:
    if response.status_code == 200:
        response_200 = StatusPagesShowStatusPageComponentAvailabilityResultV2.from_dict(
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
) -> Response[ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_at: datetime.datetime,
    end_at: datetime.datetime,
) -> Response[ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2]:
    """ShowStatusPageComponentAvailability Status Pages V2

     Show availability for a status page component over a time window.

    Pass start_at and end_at as RFC3339 timestamps. The window cannot be longer than 366 days.
    Availability uses the same rules as the public status page: full and partial outages count as
    downtime, overlapping impacts are merged, and time before we have data for the component is excluded
    rather than counted as up.

    This endpoint requires a valid API key but no specific scopes. Use ListStatusPages and
    ShowStatusPageStructure to find status page and component IDs.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str): ID of the component. You can find this by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        start_at (datetime.datetime): Start of the availability window Example:
            2026-01-01T00:00:00Z.
        end_at (datetime.datetime): End of the availability window Example: 2026-02-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        component_id=component_id,
        start_at=start_at,
        end_at=end_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_at: datetime.datetime,
    end_at: datetime.datetime,
) -> ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2 | None:
    """ShowStatusPageComponentAvailability Status Pages V2

     Show availability for a status page component over a time window.

    Pass start_at and end_at as RFC3339 timestamps. The window cannot be longer than 366 days.
    Availability uses the same rules as the public status page: full and partial outages count as
    downtime, overlapping impacts are merged, and time before we have data for the component is excluded
    rather than counted as up.

    This endpoint requires a valid API key but no specific scopes. Use ListStatusPages and
    ShowStatusPageStructure to find status page and component IDs.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str): ID of the component. You can find this by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        start_at (datetime.datetime): Start of the availability window Example:
            2026-01-01T00:00:00Z.
        end_at (datetime.datetime): End of the availability window Example: 2026-02-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2
    """

    return sync_detailed(
        status_page_id=status_page_id,
        component_id=component_id,
        client=client,
        start_at=start_at,
        end_at=end_at,
    ).parsed


async def asyncio_detailed(
    status_page_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_at: datetime.datetime,
    end_at: datetime.datetime,
) -> Response[ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2]:
    """ShowStatusPageComponentAvailability Status Pages V2

     Show availability for a status page component over a time window.

    Pass start_at and end_at as RFC3339 timestamps. The window cannot be longer than 366 days.
    Availability uses the same rules as the public status page: full and partial outages count as
    downtime, overlapping impacts are merged, and time before we have data for the component is excluded
    rather than counted as up.

    This endpoint requires a valid API key but no specific scopes. Use ListStatusPages and
    ShowStatusPageStructure to find status page and component IDs.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str): ID of the component. You can find this by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        start_at (datetime.datetime): Start of the availability window Example:
            2026-01-01T00:00:00Z.
        end_at (datetime.datetime): End of the availability window Example: 2026-02-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        component_id=component_id,
        start_at=start_at,
        end_at=end_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_at: datetime.datetime,
    end_at: datetime.datetime,
) -> ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2 | None:
    """ShowStatusPageComponentAvailability Status Pages V2

     Show availability for a status page component over a time window.

    Pass start_at and end_at as RFC3339 timestamps. The window cannot be longer than 366 days.
    Availability uses the same rules as the public status page: full and partial outages count as
    downtime, overlapping impacts are merged, and time before we have data for the component is excluded
    rather than counted as up.

    This endpoint requires a valid API key but no specific scopes. Use ListStatusPages and
    ShowStatusPageStructure to find status page and component IDs.

    Args:
        status_page_id (str): ID of the status page. You can find this by calling the
            ListStatusPages endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        component_id (str): ID of the component. You can find this by calling the
            ShowStatusPageStructure endpoint. Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        start_at (datetime.datetime): Start of the availability window Example:
            2026-01-01T00:00:00Z.
        end_at (datetime.datetime): End of the availability window Example: 2026-02-01T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesShowStatusPageComponentAvailabilityResultV2
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            component_id=component_id,
            client=client,
            start_at=start_at,
            end_at=end_at,
        )
    ).parsed
