from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedules_update_payload_v2 import SchedulesUpdatePayloadV2
from ...models.schedules_update_result_v2 import SchedulesUpdateResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SchedulesUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/schedules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SchedulesUpdateResultV2 | None:
    if response.status_code == 200:
        response_200 = SchedulesUpdateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | SchedulesUpdateResultV2]:
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
    body: SchedulesUpdatePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateResultV2]:
    """Update Schedules V2

     Update a schedule.

    Updating a schedule replaces its entire configuration with the one you send,
    including any scheduled future versions of its rotations — fetch the schedule
    first and include every version you want to keep.

    To change who's in a rotation from a future date without affecting shifts
    before then, keep the current version unchanged and add another version of the
    same rotation with `effective_from` set to when the change should land —
    ideally an upcoming handover, so nobody is swapped mid-shift. You can check the
    effect of any configuration before saving it with Preview schedule entries.

    Args:
        id (str): The schedule ID to update. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (SchedulesUpdatePayloadV2):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users': [{'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}],
            'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}, 'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'Primary
            On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone':
            'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateResultV2]
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
    body: SchedulesUpdatePayloadV2,
) -> ErrorResponse | SchedulesUpdateResultV2 | None:
    """Update Schedules V2

     Update a schedule.

    Updating a schedule replaces its entire configuration with the one you send,
    including any scheduled future versions of its rotations — fetch the schedule
    first and include every version you want to keep.

    To change who's in a rotation from a future date without affecting shifts
    before then, keep the current version unchanged and add another version of the
    same rotation with `effective_from` set to when the change should land —
    ideally an upcoming handover, so nobody is swapped mid-shift. You can check the
    effect of any configuration before saving it with Preview schedule entries.

    Args:
        id (str): The schedule ID to update. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (SchedulesUpdatePayloadV2):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users': [{'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}],
            'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}, 'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'Primary
            On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone':
            'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateResultV2
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
    body: SchedulesUpdatePayloadV2,
) -> Response[ErrorResponse | SchedulesUpdateResultV2]:
    """Update Schedules V2

     Update a schedule.

    Updating a schedule replaces its entire configuration with the one you send,
    including any scheduled future versions of its rotations — fetch the schedule
    first and include every version you want to keep.

    To change who's in a rotation from a future date without affecting shifts
    before then, keep the current version unchanged and add another version of the
    same rotation with `effective_from` set to when the change should land —
    ideally an upcoming handover, so nobody is swapped mid-shift. You can check the
    effect of any configuration before saving it with Preview schedule entries.

    Args:
        id (str): The schedule ID to update. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (SchedulesUpdatePayloadV2):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users': [{'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}],
            'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}, 'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'Primary
            On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone':
            'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SchedulesUpdateResultV2]
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
    body: SchedulesUpdatePayloadV2,
) -> ErrorResponse | SchedulesUpdateResultV2 | None:
    """Update Schedules V2

     Update a schedule.

    Updating a schedule replaces its entire configuration with the one you send,
    including any scheduled future versions of its rotations — fetch the schedule
    first and include every version you want to keep.

    To change who's in a rotation from a future date without affecting shifts
    before then, keep the current version unchanged and add another version of the
    same rotation with `effective_from` set to when the change should land —
    ideally an upcoming handover, so nobody is swapped mid-shift. You can check the
    effect of any configuration before saving it with Preview schedule entries.

    Args:
        id (str): The schedule ID to update. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (SchedulesUpdatePayloadV2):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'hourly'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users': [{'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}],
            'working_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'monday'}]}]}, 'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'Primary
            On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone':
            'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SchedulesUpdateResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
