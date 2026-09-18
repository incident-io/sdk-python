from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.status_pages_create_status_page_incident_update_payload_v2 import (
    StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
)
from ...models.status_pages_create_status_page_incident_update_result_v2 import (
    StatusPagesCreateStatusPageIncidentUpdateResultV2,
)
from ...types import Response


def _get_kwargs(
    *,
    body: StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/status_page_incident_updates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2 | None:
    if response.status_code == 201:
        response_201 = StatusPagesCreateStatusPageIncidentUpdateResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
) -> Response[ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2]:
    """CreateStatusPageIncidentUpdate Status Pages V2

     Post an update on a Status Page incident.

    This is the endpoint to use when resolving an incident - set incident_status to "resolved" to end
    the incident. There is a limit of 100 updates per incident.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        body (StatusPagesCreateStatusPageIncidentUpdatePayloadV2):  Example:
            {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'incident_status': 'investigating', 'message': 'The fix has been deployed
            and we are monitoring the situation. Some users may still experience intermittent
            issues.', 'notify_subscribers': True, 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2]
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
    body: StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
) -> ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2 | None:
    """CreateStatusPageIncidentUpdate Status Pages V2

     Post an update on a Status Page incident.

    This is the endpoint to use when resolving an incident - set incident_status to "resolved" to end
    the incident. There is a limit of 100 updates per incident.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        body (StatusPagesCreateStatusPageIncidentUpdatePayloadV2):  Example:
            {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'incident_status': 'investigating', 'message': 'The fix has been deployed
            and we are monitoring the situation. Some users may still experience intermittent
            issues.', 'notify_subscribers': True, 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
) -> Response[ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2]:
    """CreateStatusPageIncidentUpdate Status Pages V2

     Post an update on a Status Page incident.

    This is the endpoint to use when resolving an incident - set incident_status to "resolved" to end
    the incident. There is a limit of 100 updates per incident.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        body (StatusPagesCreateStatusPageIncidentUpdatePayloadV2):  Example:
            {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'incident_status': 'investigating', 'message': 'The fix has been deployed
            and we are monitoring the situation. Some users may still experience intermittent
            issues.', 'notify_subscribers': True, 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StatusPagesCreateStatusPageIncidentUpdatePayloadV2,
) -> ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2 | None:
    """CreateStatusPageIncidentUpdate Status Pages V2

     Post an update on a Status Page incident.

    This is the endpoint to use when resolving an incident - set incident_status to "resolved" to end
    the incident. There is a limit of 100 updates per incident.

    This endpoint requires an API key with the "Create status page incidents, status page maintenance
    windows, and publish status page updates" scope.

    Args:
        body (StatusPagesCreateStatusPageIncidentUpdatePayloadV2):  Example:
            {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status':
            'operational'}], 'incident_status': 'investigating', 'message': 'The fix has been deployed
            and we are monitoring the situation. Some users may still experience intermittent
            issues.', 'notify_subscribers': True, 'status_page_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StatusPagesCreateStatusPageIncidentUpdateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
