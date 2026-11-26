from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.team_grouping_preferences_update_payload_v3 import (
    TeamGroupingPreferencesUpdatePayloadV3,
)
from ...models.team_grouping_preferences_update_result_v3 import (
    TeamGroupingPreferencesUpdateResultV3,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: TeamGroupingPreferencesUpdatePayloadV3,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/team_grouping_preferences/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TeamGroupingPreferencesUpdateResultV3 | None:
    if response.status_code == 200:
        response_200 = TeamGroupingPreferencesUpdateResultV3.from_dict(response.json())

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
) -> Response[ErrorResponse | TeamGroupingPreferencesUpdateResultV3]:
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
    body: TeamGroupingPreferencesUpdatePayloadV3,
) -> Response[ErrorResponse | TeamGroupingPreferencesUpdateResultV3]:
    """Update Team Grouping Preferences V3

     Update a team's grouping preference. The team cannot change: to move a preference, delete it and
    create another.

    Args:
        id (str): Unique identifier of the preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (TeamGroupingPreferencesUpdatePayloadV3):  Example: {'default': {'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}},
            'version': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamGroupingPreferencesUpdateResultV3]
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
    body: TeamGroupingPreferencesUpdatePayloadV3,
) -> ErrorResponse | TeamGroupingPreferencesUpdateResultV3 | None:
    """Update Team Grouping Preferences V3

     Update a team's grouping preference. The team cannot change: to move a preference, delete it and
    create another.

    Args:
        id (str): Unique identifier of the preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (TeamGroupingPreferencesUpdatePayloadV3):  Example: {'default': {'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}},
            'version': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamGroupingPreferencesUpdateResultV3
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
    body: TeamGroupingPreferencesUpdatePayloadV3,
) -> Response[ErrorResponse | TeamGroupingPreferencesUpdateResultV3]:
    """Update Team Grouping Preferences V3

     Update a team's grouping preference. The team cannot change: to move a preference, delete it and
    create another.

    Args:
        id (str): Unique identifier of the preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (TeamGroupingPreferencesUpdatePayloadV3):  Example: {'default': {'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}},
            'version': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TeamGroupingPreferencesUpdateResultV3]
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
    body: TeamGroupingPreferencesUpdatePayloadV3,
) -> ErrorResponse | TeamGroupingPreferencesUpdateResultV3 | None:
    """Update Team Grouping Preferences V3

     Update a team's grouping preference. The team cannot change: to move a preference, delete it and
    create another.

    Args:
        id (str): Unique identifier of the preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (TeamGroupingPreferencesUpdatePayloadV3):  Example: {'default': {'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}},
            'version': 4}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TeamGroupingPreferencesUpdateResultV3
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
