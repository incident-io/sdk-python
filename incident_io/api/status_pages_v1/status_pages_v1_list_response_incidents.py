from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.status_pages_list_response_incidents_result_v1 import (
    StatusPagesListResponseIncidentsResultV1,
)
from ...types import Response


def _get_kwargs(
    id: str,
    incident_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/status-pages/{id}/incidents/{incident_id}/response-incidents".format(
            id=quote(str(id), safe=""),
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StatusPagesListResponseIncidentsResultV1 | None:
    if response.status_code == 200:
        response_200 = StatusPagesListResponseIncidentsResultV1.from_dict(
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
) -> Response[ErrorResponse | StatusPagesListResponseIncidentsResultV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | StatusPagesListResponseIncidentsResultV1]:
    """ListResponseIncidents Status Pages V1

     List the linked Response incidents for a status page incident.

    Args:
        id (str): ID of the status page Example: abc123.
        incident_id (str): ID of the status page incident Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesListResponseIncidentsResultV1]
    """

    kwargs = _get_kwargs(
        id=id,
        incident_id=incident_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | StatusPagesListResponseIncidentsResultV1 | None:
    """ListResponseIncidents Status Pages V1

     List the linked Response incidents for a status page incident.

    Args:
        id (str): ID of the status page Example: abc123.
        incident_id (str): ID of the status page incident Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesListResponseIncidentsResultV1
    """

    return sync_detailed(
        id=id,
        incident_id=incident_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | StatusPagesListResponseIncidentsResultV1]:
    """ListResponseIncidents Status Pages V1

     List the linked Response incidents for a status page incident.

    Args:
        id (str): ID of the status page Example: abc123.
        incident_id (str): ID of the status page incident Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesListResponseIncidentsResultV1]
    """

    kwargs = _get_kwargs(
        id=id,
        incident_id=incident_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | StatusPagesListResponseIncidentsResultV1 | None:
    """ListResponseIncidents Status Pages V1

     List the linked Response incidents for a status page incident.

    Args:
        id (str): ID of the status page Example: abc123.
        incident_id (str): ID of the status page incident Example: abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesListResponseIncidentsResultV1
    """

    return (
        await asyncio_detailed(
            id=id,
            incident_id=incident_id,
            client=client,
        )
    ).parsed
