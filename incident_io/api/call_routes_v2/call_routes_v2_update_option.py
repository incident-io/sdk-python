from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_routes_update_option_payload_v2 import (
    CallRoutesUpdateOptionPayloadV2,
)
from ...models.call_routes_update_option_result_v2 import CallRoutesUpdateOptionResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    call_route_id: str,
    id: str,
    *,
    body: CallRoutesUpdateOptionPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/call_routes/{call_route_id}/options/{id}".format(
            call_route_id=quote(str(call_route_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CallRoutesUpdateOptionResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CallRoutesUpdateOptionResultV2.from_dict(response.json())

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
) -> Response[CallRoutesUpdateOptionResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    call_route_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CallRoutesUpdateOptionPayloadV2,
) -> Response[CallRoutesUpdateOptionResultV2 | ErrorResponse]:
    """UpdateOption Call Routes V2

     Replace a phone-tree option.

    Two live options can't share a digit, so moving an option onto a digit the menu
    already uses is rejected.

    Args:
        call_route_id (str): The call route's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        id (str): The option's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CallRoutesUpdateOptionPayloadV2):  Example: {'digit': '1', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text':
            'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallRoutesUpdateOptionResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        call_route_id=call_route_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_route_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CallRoutesUpdateOptionPayloadV2,
) -> CallRoutesUpdateOptionResultV2 | ErrorResponse | None:
    """UpdateOption Call Routes V2

     Replace a phone-tree option.

    Two live options can't share a digit, so moving an option onto a digit the menu
    already uses is rejected.

    Args:
        call_route_id (str): The call route's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        id (str): The option's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CallRoutesUpdateOptionPayloadV2):  Example: {'digit': '1', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text':
            'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallRoutesUpdateOptionResultV2 | ErrorResponse
    """

    return sync_detailed(
        call_route_id=call_route_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    call_route_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CallRoutesUpdateOptionPayloadV2,
) -> Response[CallRoutesUpdateOptionResultV2 | ErrorResponse]:
    """UpdateOption Call Routes V2

     Replace a phone-tree option.

    Two live options can't share a digit, so moving an option onto a digit the menu
    already uses is rejected.

    Args:
        call_route_id (str): The call route's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        id (str): The option's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CallRoutesUpdateOptionPayloadV2):  Example: {'digit': '1', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text':
            'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallRoutesUpdateOptionResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        call_route_id=call_route_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_route_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CallRoutesUpdateOptionPayloadV2,
) -> CallRoutesUpdateOptionResultV2 | ErrorResponse | None:
    """UpdateOption Call Routes V2

     Replace a phone-tree option.

    Two live options can't share a digit, so moving an option onto a digit the menu
    already uses is rejected.

    Args:
        call_route_id (str): The call route's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        id (str): The option's ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CallRoutesUpdateOptionPayloadV2):  Example: {'digit': '1', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text':
            'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallRoutesUpdateOptionResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            call_route_id=call_route_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
