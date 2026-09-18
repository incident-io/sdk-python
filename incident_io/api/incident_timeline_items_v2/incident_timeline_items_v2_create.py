from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_timeline_items_create_payload_v2 import (
    IncidentTimelineItemsCreatePayloadV2,
)
from ...models.incident_timeline_items_create_result_v2 import (
    IncidentTimelineItemsCreateResultV2,
)
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentTimelineItemsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/incident_timeline_items",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentTimelineItemsCreateResultV2 | None:
    if response.status_code == 201:
        response_201 = IncidentTimelineItemsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentTimelineItemsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentTimelineItemsCreatePayloadV2,
) -> Response[ErrorResponse | IncidentTimelineItemsCreateResultV2]:
    """Create Incident Timeline Items V2

     Add a custom item to an incident's timeline.

    Items created here are custom, so they carry no activity_log_id and their timestamp stays
    editable. Set it to when the thing actually happened rather than when you're telling us about
    it - a deploy you shipped an hour ago belongs an hour back on the timeline.

    Every request needs an idempotency_key. Retrying with a key we've already seen returns the
    item the first request created rather than writing a second one, so an automation that
    retries on a timeout doesn't leave a duplicate behind.

    Args:
        body (IncidentTimelineItemsCreatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'idempotency_key': 'deploy-4f2c1b90',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'timestamp': '2026-09-01T15:30:00Z', 'title':
            'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentTimelineItemsCreateResultV2]
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
    body: IncidentTimelineItemsCreatePayloadV2,
) -> ErrorResponse | IncidentTimelineItemsCreateResultV2 | None:
    """Create Incident Timeline Items V2

     Add a custom item to an incident's timeline.

    Items created here are custom, so they carry no activity_log_id and their timestamp stays
    editable. Set it to when the thing actually happened rather than when you're telling us about
    it - a deploy you shipped an hour ago belongs an hour back on the timeline.

    Every request needs an idempotency_key. Retrying with a key we've already seen returns the
    item the first request created rather than writing a second one, so an automation that
    retries on a timeout doesn't leave a duplicate behind.

    Args:
        body (IncidentTimelineItemsCreatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'idempotency_key': 'deploy-4f2c1b90',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'timestamp': '2026-09-01T15:30:00Z', 'title':
            'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentTimelineItemsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentTimelineItemsCreatePayloadV2,
) -> Response[ErrorResponse | IncidentTimelineItemsCreateResultV2]:
    """Create Incident Timeline Items V2

     Add a custom item to an incident's timeline.

    Items created here are custom, so they carry no activity_log_id and their timestamp stays
    editable. Set it to when the thing actually happened rather than when you're telling us about
    it - a deploy you shipped an hour ago belongs an hour back on the timeline.

    Every request needs an idempotency_key. Retrying with a key we've already seen returns the
    item the first request created rather than writing a second one, so an automation that
    retries on a timeout doesn't leave a duplicate behind.

    Args:
        body (IncidentTimelineItemsCreatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'idempotency_key': 'deploy-4f2c1b90',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'timestamp': '2026-09-01T15:30:00Z', 'title':
            'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentTimelineItemsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: IncidentTimelineItemsCreatePayloadV2,
) -> ErrorResponse | IncidentTimelineItemsCreateResultV2 | None:
    """Create Incident Timeline Items V2

     Add a custom item to an incident's timeline.

    Items created here are custom, so they carry no activity_log_id and their timestamp stays
    editable. Set it to when the thing actually happened rather than when you're telling us about
    it - a deploy you shipped an hour ago belongs an hour back on the timeline.

    Every request needs an idempotency_key. Retrying with a key we've already seen returns the
    item the first request created rather than writing a second one, so an automation that
    retries on a timeout doesn't leave a duplicate behind.

    Args:
        body (IncidentTimelineItemsCreatePayloadV2):  Example: {'description': 'Rolled back
            **payments-api** to v411 after error rate hit 12%.', 'idempotency_key': 'deploy-4f2c1b90',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'timestamp': '2026-09-01T15:30:00Z', 'title':
            'Rolled back payments-api'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentTimelineItemsCreateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
