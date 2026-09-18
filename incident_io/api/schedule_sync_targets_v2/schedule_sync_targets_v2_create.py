from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedule_sync_targets_create_payload_v2 import (
    ScheduleSyncTargetsCreatePayloadV2,
)
from ...models.schedule_sync_targets_create_result_v2 import (
    ScheduleSyncTargetsCreateResultV2,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ScheduleSyncTargetsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/schedule_sync_targets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ScheduleSyncTargetsCreateResultV2 | None:
    if response.status_code == 201:
        response_201 = ScheduleSyncTargetsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | ScheduleSyncTargetsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleSyncTargetsCreatePayloadV2,
) -> Response[ErrorResponse | ScheduleSyncTargetsCreateResultV2]:
    """Create Schedule Sync Targets V2

     Create a new schedule sync target for a Slack user group.

    Args:
        body (ScheduleSyncTargetsCreatePayloadV2):  Example: {'schedule_sync_target':
            {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'},
            'new_slack_user_group': {'description': 'The team responsible for Project A', 'handle':
            'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'},
            'slack_user_group_id': 'S06MNNU5BMK'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduleSyncTargetsCreateResultV2]
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
    body: ScheduleSyncTargetsCreatePayloadV2,
) -> ErrorResponse | ScheduleSyncTargetsCreateResultV2 | None:
    """Create Schedule Sync Targets V2

     Create a new schedule sync target for a Slack user group.

    Args:
        body (ScheduleSyncTargetsCreatePayloadV2):  Example: {'schedule_sync_target':
            {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'},
            'new_slack_user_group': {'description': 'The team responsible for Project A', 'handle':
            'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'},
            'slack_user_group_id': 'S06MNNU5BMK'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduleSyncTargetsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleSyncTargetsCreatePayloadV2,
) -> Response[ErrorResponse | ScheduleSyncTargetsCreateResultV2]:
    """Create Schedule Sync Targets V2

     Create a new schedule sync target for a Slack user group.

    Args:
        body (ScheduleSyncTargetsCreatePayloadV2):  Example: {'schedule_sync_target':
            {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'},
            'new_slack_user_group': {'description': 'The team responsible for Project A', 'handle':
            'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'},
            'slack_user_group_id': 'S06MNNU5BMK'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduleSyncTargetsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleSyncTargetsCreatePayloadV2,
) -> ErrorResponse | ScheduleSyncTargetsCreateResultV2 | None:
    """Create Schedule Sync Targets V2

     Create a new schedule sync target for a Slack user group.

    Args:
        body (ScheduleSyncTargetsCreatePayloadV2):  Example: {'schedule_sync_target':
            {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'},
            'new_slack_user_group': {'description': 'The team responsible for Project A', 'handle':
            'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'},
            'slack_user_group_id': 'S06MNNU5BMK'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduleSyncTargetsCreateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
