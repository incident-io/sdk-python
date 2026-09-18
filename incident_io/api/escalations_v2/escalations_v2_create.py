from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.escalations_create_payload_v2 import EscalationsCreatePayloadV2
from ...models.escalations_create_result_v2 import EscalationsCreateResultV2
from ...types import Response


def _get_kwargs(
    *,
    body: EscalationsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/escalations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EscalationsCreateResultV2 | None:
    if response.status_code == 201:
        response_201 = EscalationsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | EscalationsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsCreatePayloadV2,
) -> Response[ErrorResponse | EscalationsCreateResultV2]:
    """Create Escalations V2

     Create an escalation.

    An escalation pages people, either according to an escalation path, or directly to
    specific users. You must provide either an escalation_path_id OR user_ids, but not both.

    When escalating via an escalation path, the escalation will follow the configured path
    with its levels and timeouts, using your default [alert
    priority](https://app.incident.io/~/settings/alerts/configuration/priorities).

    When escalating directly to users, they will receive a high-urgency
    notification, based on their notification rules.

    This endpoint is rate-limited to 60 requests per minute, since it is intended for
    interactive use cases (for example someone clicking a "escalate to team" button
    in your internal developer platform). To escalate based on automated alerts, we
    recommend sending events to an alert source instead.

    If your API key's permissions are scoped to teams, you can only escalate via an
    escalation path that one of those teams owns. Escalating directly to user_ids
    needs the permission at the account level, because an escalation aimed at a
    person has no owning team.

    Args:
        body (EscalationsCreatePayloadV2):  Example: {'description': 'Database CPU has been above
            90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'idempotency_key':
            '2024-01-15-abc123', 'incident_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'title': 'Production
            database experiencing high CPU', 'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsCreateResultV2]
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
    body: EscalationsCreatePayloadV2,
) -> ErrorResponse | EscalationsCreateResultV2 | None:
    """Create Escalations V2

     Create an escalation.

    An escalation pages people, either according to an escalation path, or directly to
    specific users. You must provide either an escalation_path_id OR user_ids, but not both.

    When escalating via an escalation path, the escalation will follow the configured path
    with its levels and timeouts, using your default [alert
    priority](https://app.incident.io/~/settings/alerts/configuration/priorities).

    When escalating directly to users, they will receive a high-urgency
    notification, based on their notification rules.

    This endpoint is rate-limited to 60 requests per minute, since it is intended for
    interactive use cases (for example someone clicking a "escalate to team" button
    in your internal developer platform). To escalate based on automated alerts, we
    recommend sending events to an alert source instead.

    If your API key's permissions are scoped to teams, you can only escalate via an
    escalation path that one of those teams owns. Escalating directly to user_ids
    needs the permission at the account level, because an escalation aimed at a
    person has no owning team.

    Args:
        body (EscalationsCreatePayloadV2):  Example: {'description': 'Database CPU has been above
            90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'idempotency_key':
            '2024-01-15-abc123', 'incident_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'title': 'Production
            database experiencing high CPU', 'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsCreatePayloadV2,
) -> Response[ErrorResponse | EscalationsCreateResultV2]:
    """Create Escalations V2

     Create an escalation.

    An escalation pages people, either according to an escalation path, or directly to
    specific users. You must provide either an escalation_path_id OR user_ids, but not both.

    When escalating via an escalation path, the escalation will follow the configured path
    with its levels and timeouts, using your default [alert
    priority](https://app.incident.io/~/settings/alerts/configuration/priorities).

    When escalating directly to users, they will receive a high-urgency
    notification, based on their notification rules.

    This endpoint is rate-limited to 60 requests per minute, since it is intended for
    interactive use cases (for example someone clicking a "escalate to team" button
    in your internal developer platform). To escalate based on automated alerts, we
    recommend sending events to an alert source instead.

    If your API key's permissions are scoped to teams, you can only escalate via an
    escalation path that one of those teams owns. Escalating directly to user_ids
    needs the permission at the account level, because an escalation aimed at a
    person has no owning team.

    Args:
        body (EscalationsCreatePayloadV2):  Example: {'description': 'Database CPU has been above
            90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'idempotency_key':
            '2024-01-15-abc123', 'incident_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'title': 'Production
            database experiencing high CPU', 'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EscalationsCreatePayloadV2,
) -> ErrorResponse | EscalationsCreateResultV2 | None:
    """Create Escalations V2

     Create an escalation.

    An escalation pages people, either according to an escalation path, or directly to
    specific users. You must provide either an escalation_path_id OR user_ids, but not both.

    When escalating via an escalation path, the escalation will follow the configured path
    with its levels and timeouts, using your default [alert
    priority](https://app.incident.io/~/settings/alerts/configuration/priorities).

    When escalating directly to users, they will receive a high-urgency
    notification, based on their notification rules.

    This endpoint is rate-limited to 60 requests per minute, since it is intended for
    interactive use cases (for example someone clicking a "escalate to team" button
    in your internal developer platform). To escalate based on automated alerts, we
    recommend sending events to an alert source instead.

    If your API key's permissions are scoped to teams, you can only escalate via an
    escalation path that one of those teams owns. Escalating directly to user_ids
    needs the permission at the account level, because an escalation aimed at a
    person has no owning team.

    Args:
        body (EscalationsCreatePayloadV2):  Example: {'description': 'Database CPU has been above
            90% for 5 minutes', 'escalation_path_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'idempotency_key':
            '2024-01-15-abc123', 'incident_id': '01H0J1EXE7AXZ2C93K61WBPYEH', 'title': 'Production
            database experiencing high CPU', 'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsCreateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
