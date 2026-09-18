from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_statuses_update_payload_v1 import (
    IncidentStatusesUpdatePayloadV1,
)
from ...models.incident_statuses_update_result_v1 import IncidentStatusesUpdateResultV1
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentStatusesUpdatePayloadV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/incident_statuses/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentStatusesUpdateResultV1 | None:
    if response.status_code == 200:
        response_200 = IncidentStatusesUpdateResultV1.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentStatusesUpdateResultV1]:
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
    body: IncidentStatusesUpdatePayloadV1,
) -> Response[ErrorResponse | IncidentStatusesUpdateResultV1]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentStatusesUpdatePayloadV1):  Example: {'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'name': 'Closed', 'rank': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentStatusesUpdateResultV1]
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
    body: IncidentStatusesUpdatePayloadV1,
) -> ErrorResponse | IncidentStatusesUpdateResultV1 | None:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentStatusesUpdatePayloadV1):  Example: {'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'name': 'Closed', 'rank': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentStatusesUpdateResultV1
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
    body: IncidentStatusesUpdatePayloadV1,
) -> Response[ErrorResponse | IncidentStatusesUpdateResultV1]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentStatusesUpdatePayloadV1):  Example: {'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'name': 'Closed', 'rank': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentStatusesUpdateResultV1]
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
    body: IncidentStatusesUpdatePayloadV1,
) -> ErrorResponse | IncidentStatusesUpdateResultV1 | None:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentStatusesUpdatePayloadV1):  Example: {'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'name': 'Closed', 'rank': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentStatusesUpdateResultV1
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
