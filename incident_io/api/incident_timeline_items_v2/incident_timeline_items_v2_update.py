from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_timeline_items_update_payload_v2 import (
    IncidentTimelineItemsUpdatePayloadV2,
)
from ...models.incident_timeline_items_update_result_v2 import (
    IncidentTimelineItemsUpdateResultV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentTimelineItemsUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/incident_timeline_items/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentTimelineItemsUpdateResultV2 | None:
    if response.status_code == 200:
        response_200 = IncidentTimelineItemsUpdateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentTimelineItemsUpdateResultV2]:
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
    body: IncidentTimelineItemsUpdatePayloadV2,
) -> Response[ErrorResponse | IncidentTimelineItemsUpdateResultV2]:
    """Update Incident Timeline Items V2

     Edit a timeline item.

    Fields you leave out are unchanged, and an empty description removes it. Timestamp can only
    be changed on a custom item: a promoted one follows the activity it came from.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentTimelineItemsUpdatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentTimelineItemsUpdateResultV2]
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
    body: IncidentTimelineItemsUpdatePayloadV2,
) -> ErrorResponse | IncidentTimelineItemsUpdateResultV2 | None:
    """Update Incident Timeline Items V2

     Edit a timeline item.

    Fields you leave out are unchanged, and an empty description removes it. Timestamp can only
    be changed on a custom item: a promoted one follows the activity it came from.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentTimelineItemsUpdatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentTimelineItemsUpdateResultV2
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
    body: IncidentTimelineItemsUpdatePayloadV2,
) -> Response[ErrorResponse | IncidentTimelineItemsUpdateResultV2]:
    """Update Incident Timeline Items V2

     Edit a timeline item.

    Fields you leave out are unchanged, and an empty description removes it. Timestamp can only
    be changed on a custom item: a promoted one follows the activity it came from.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentTimelineItemsUpdatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentTimelineItemsUpdateResultV2]
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
    body: IncidentTimelineItemsUpdatePayloadV2,
) -> ErrorResponse | IncidentTimelineItemsUpdateResultV2 | None:
    """Update Incident Timeline Items V2

     Edit a timeline item.

    Fields you leave out are unchanged, and an empty description removes it. Timestamp can only
    be changed on a custom item: a promoted one follows the activity it came from.

    Args:
        id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        body (IncidentTimelineItemsUpdatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'timestamp': '2026-09-01T15:30:00Z',
            'title': 'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentTimelineItemsUpdateResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
