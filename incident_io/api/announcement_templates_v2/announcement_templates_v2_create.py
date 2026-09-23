from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.announcement_templates_create_payload_v2 import (
    AnnouncementTemplatesCreatePayloadV2,
)
from ...models.announcement_templates_create_result_v2 import (
    AnnouncementTemplatesCreateResultV2,
)
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AnnouncementTemplatesCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/announcement_templates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnnouncementTemplatesCreateResultV2 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = AnnouncementTemplatesCreateResultV2.from_dict(response.json())

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
) -> Response[AnnouncementTemplatesCreateResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnouncementTemplatesCreatePayloadV2,
) -> Response[AnnouncementTemplatesCreateResultV2 | ErrorResponse]:
    """Create Announcement Templates V2

     Create an announcement template.

    Args:
        body (AnnouncementTemplatesCreatePayloadV2):  Example: {'actions': [{'action_type':
            'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text':
            {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnouncementTemplatesCreateResultV2 | ErrorResponse]
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
    body: AnnouncementTemplatesCreatePayloadV2,
) -> AnnouncementTemplatesCreateResultV2 | ErrorResponse | None:
    """Create Announcement Templates V2

     Create an announcement template.

    Args:
        body (AnnouncementTemplatesCreatePayloadV2):  Example: {'actions': [{'action_type':
            'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text':
            {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnouncementTemplatesCreateResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnouncementTemplatesCreatePayloadV2,
) -> Response[AnnouncementTemplatesCreateResultV2 | ErrorResponse]:
    """Create Announcement Templates V2

     Create an announcement template.

    Args:
        body (AnnouncementTemplatesCreatePayloadV2):  Example: {'actions': [{'action_type':
            'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text':
            {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnouncementTemplatesCreateResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AnnouncementTemplatesCreatePayloadV2,
) -> AnnouncementTemplatesCreateResultV2 | ErrorResponse | None:
    """Create Announcement Templates V2

     Create an announcement template.

    Args:
        body (AnnouncementTemplatesCreatePayloadV2):  Example: {'actions': [{'action_type':
            'announcement_post_actions_homepage', 'emoji': 'slack', 'rank': 1}], 'fields':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'emoji': 'fire', 'field_type':
            'announcement_post_fields_status', 'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'rank': 1, 'rich_text':
            {'contents': 'If you work on **payments**, please join {{incident.reference}}', 'type':
            'markdown'}}], 'name': 'Major incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnouncementTemplatesCreateResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
