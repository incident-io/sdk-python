from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.escalations_reassign_escalation_payload_v2 import (
    EscalationsReassignEscalationPayloadV2,
)
from ...models.escalations_reassign_escalation_result_v2 import (
    EscalationsReassignEscalationResultV2,
)
from ...types import Response


def _get_kwargs(
    escalation_id: str,
    *,
    body: EscalationsReassignEscalationPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/escalations/{escalation_id}/actions/reassign".format(
            escalation_id=quote(str(escalation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EscalationsReassignEscalationResultV2 | None:
    if response.status_code == 201:
        response_201 = EscalationsReassignEscalationResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | EscalationsReassignEscalationResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    escalation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsReassignEscalationPayloadV2,
) -> Response[ErrorResponse | EscalationsReassignEscalationResultV2]:
    """ReassignEscalation Escalations V2

     Reassign an escalation to a different escalation path or set of users.

    Use this when a page reached the wrong people. Reassigning creates a new escalation
    aimed at the targets you give, linked back to the original, and carries over the
    original's title, description, priority, incident and alert so the page stays attached
    to the same alert and acknowledgements keep grouping under it.

    You must provide either an escalation_path_id OR user_ids, but not both. Both name
    incident.io escalation paths and users, so an escalation cannot be reassigned to an
    external escalator such as PagerDuty or Opsgenie.

    By default the original escalation is resolved, so the first targets stop being paged.
    Pass resolve_original=false to leave it running alongside the new one. Resolving the
    original additionally needs the "escalations.respond" permission, since it stops a page
    someone else may be responding to.

    An escalation can only be reassigned once: calling this again for the same escalation
    is rejected. Retrying a request whose response you never saw is safe in the sense that
    matters — a reassignment that already happened is never repeated, so nobody is paged
    twice — but the retry is rejected rather than returning the escalation the first call
    created, so keep the ID from the original response.

    To use this API, you will need an API key with the "Create and manage escalations"
    permission. The reassignment is attributed to the key; to attribute it to one of your
    users instead, set the X-Incident-User header, which needs the
    "api_keys.act_on_behalf_of_users" scope.

    If your API key's permissions are scoped to teams, the escalation you're reassigning
    must be owned by one of those teams, and you can only reassign via an escalation path
    one of them owns. Reassigning directly to user_ids needs the permission at the account
    level, because an escalation aimed at a person has no owning team.

    Args:
        escalation_id (str): The ID of the escalation to reassign Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (EscalationsReassignEscalationPayloadV2):  Example: {'description': 'Database CPU has
            been above 90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH',
            'resolve_original': True, 'title': 'Production database experiencing high CPU',
            'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsReassignEscalationResultV2]
    """

    kwargs = _get_kwargs(
        escalation_id=escalation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    escalation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsReassignEscalationPayloadV2,
) -> ErrorResponse | EscalationsReassignEscalationResultV2 | None:
    """ReassignEscalation Escalations V2

     Reassign an escalation to a different escalation path or set of users.

    Use this when a page reached the wrong people. Reassigning creates a new escalation
    aimed at the targets you give, linked back to the original, and carries over the
    original's title, description, priority, incident and alert so the page stays attached
    to the same alert and acknowledgements keep grouping under it.

    You must provide either an escalation_path_id OR user_ids, but not both. Both name
    incident.io escalation paths and users, so an escalation cannot be reassigned to an
    external escalator such as PagerDuty or Opsgenie.

    By default the original escalation is resolved, so the first targets stop being paged.
    Pass resolve_original=false to leave it running alongside the new one. Resolving the
    original additionally needs the "escalations.respond" permission, since it stops a page
    someone else may be responding to.

    An escalation can only be reassigned once: calling this again for the same escalation
    is rejected. Retrying a request whose response you never saw is safe in the sense that
    matters — a reassignment that already happened is never repeated, so nobody is paged
    twice — but the retry is rejected rather than returning the escalation the first call
    created, so keep the ID from the original response.

    To use this API, you will need an API key with the "Create and manage escalations"
    permission. The reassignment is attributed to the key; to attribute it to one of your
    users instead, set the X-Incident-User header, which needs the
    "api_keys.act_on_behalf_of_users" scope.

    If your API key's permissions are scoped to teams, the escalation you're reassigning
    must be owned by one of those teams, and you can only reassign via an escalation path
    one of them owns. Reassigning directly to user_ids needs the permission at the account
    level, because an escalation aimed at a person has no owning team.

    Args:
        escalation_id (str): The ID of the escalation to reassign Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (EscalationsReassignEscalationPayloadV2):  Example: {'description': 'Database CPU has
            been above 90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH',
            'resolve_original': True, 'title': 'Production database experiencing high CPU',
            'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsReassignEscalationResultV2
    """

    return sync_detailed(
        escalation_id=escalation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    escalation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsReassignEscalationPayloadV2,
) -> Response[ErrorResponse | EscalationsReassignEscalationResultV2]:
    """ReassignEscalation Escalations V2

     Reassign an escalation to a different escalation path or set of users.

    Use this when a page reached the wrong people. Reassigning creates a new escalation
    aimed at the targets you give, linked back to the original, and carries over the
    original's title, description, priority, incident and alert so the page stays attached
    to the same alert and acknowledgements keep grouping under it.

    You must provide either an escalation_path_id OR user_ids, but not both. Both name
    incident.io escalation paths and users, so an escalation cannot be reassigned to an
    external escalator such as PagerDuty or Opsgenie.

    By default the original escalation is resolved, so the first targets stop being paged.
    Pass resolve_original=false to leave it running alongside the new one. Resolving the
    original additionally needs the "escalations.respond" permission, since it stops a page
    someone else may be responding to.

    An escalation can only be reassigned once: calling this again for the same escalation
    is rejected. Retrying a request whose response you never saw is safe in the sense that
    matters — a reassignment that already happened is never repeated, so nobody is paged
    twice — but the retry is rejected rather than returning the escalation the first call
    created, so keep the ID from the original response.

    To use this API, you will need an API key with the "Create and manage escalations"
    permission. The reassignment is attributed to the key; to attribute it to one of your
    users instead, set the X-Incident-User header, which needs the
    "api_keys.act_on_behalf_of_users" scope.

    If your API key's permissions are scoped to teams, the escalation you're reassigning
    must be owned by one of those teams, and you can only reassign via an escalation path
    one of them owns. Reassigning directly to user_ids needs the permission at the account
    level, because an escalation aimed at a person has no owning team.

    Args:
        escalation_id (str): The ID of the escalation to reassign Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (EscalationsReassignEscalationPayloadV2):  Example: {'description': 'Database CPU has
            been above 90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH',
            'resolve_original': True, 'title': 'Production database experiencing high CPU',
            'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsReassignEscalationResultV2]
    """

    kwargs = _get_kwargs(
        escalation_id=escalation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    escalation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsReassignEscalationPayloadV2,
) -> ErrorResponse | EscalationsReassignEscalationResultV2 | None:
    """ReassignEscalation Escalations V2

     Reassign an escalation to a different escalation path or set of users.

    Use this when a page reached the wrong people. Reassigning creates a new escalation
    aimed at the targets you give, linked back to the original, and carries over the
    original's title, description, priority, incident and alert so the page stays attached
    to the same alert and acknowledgements keep grouping under it.

    You must provide either an escalation_path_id OR user_ids, but not both. Both name
    incident.io escalation paths and users, so an escalation cannot be reassigned to an
    external escalator such as PagerDuty or Opsgenie.

    By default the original escalation is resolved, so the first targets stop being paged.
    Pass resolve_original=false to leave it running alongside the new one. Resolving the
    original additionally needs the "escalations.respond" permission, since it stops a page
    someone else may be responding to.

    An escalation can only be reassigned once: calling this again for the same escalation
    is rejected. Retrying a request whose response you never saw is safe in the sense that
    matters — a reassignment that already happened is never repeated, so nobody is paged
    twice — but the retry is rejected rather than returning the escalation the first call
    created, so keep the ID from the original response.

    To use this API, you will need an API key with the "Create and manage escalations"
    permission. The reassignment is attributed to the key; to attribute it to one of your
    users instead, set the X-Incident-User header, which needs the
    "api_keys.act_on_behalf_of_users" scope.

    If your API key's permissions are scoped to teams, the escalation you're reassigning
    must be owned by one of those teams, and you can only reassign via an escalation path
    one of them owns. Reassigning directly to user_ids needs the permission at the account
    level, because an escalation aimed at a person has no owning team.

    Args:
        escalation_id (str): The ID of the escalation to reassign Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (EscalationsReassignEscalationPayloadV2):  Example: {'description': 'Database CPU has
            been above 90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH',
            'resolve_original': True, 'title': 'Production database experiencing high CPU',
            'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsReassignEscalationResultV2
    """

    return (
        await asyncio_detailed(
            escalation_id=escalation_id,
            client=client,
            body=body,
        )
    ).parsed
