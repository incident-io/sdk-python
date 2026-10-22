from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.managed_resources_create_managed_resource_payload_v2 import (
    ManagedResourcesCreateManagedResourcePayloadV2,
)
from ...models.managed_resources_create_managed_resource_result_v2 import (
    ManagedResourcesCreateManagedResourceResultV2,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ManagedResourcesCreateManagedResourcePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/managed_resources",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ManagedResourcesCreateManagedResourceResultV2 | None:
    if response.status_code == 200:
        response_200 = ManagedResourcesCreateManagedResourceResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | ManagedResourcesCreateManagedResourceResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ManagedResourcesCreateManagedResourcePayloadV2,
) -> Response[ErrorResponse | ManagedResourcesCreateManagedResourceResultV2]:
    """CreateManagedResource Managed Resources V2

     Create or update the management record for a resource. This replaces any annotations already stored
    on it.

    The annotations set `managed_by`:
    - `incident.io/terraform/version` sets it to `terraform`.
    - `incident.io/is-managed-externally` sets it to `external`. If both keys are present, `external`
    wins.
    - Neither key sets it to `dashboard`.

    This doesn't change the resource's configuration, but `managed_by` controls whether it can be edited
    in the dashboard. Returning a schedule to `dashboard` also returns its sync rules and targets.

    The API key must have the update scope for the resource type, e.g. `schedules.update` for a
    schedule.

    Args:
        body (ManagedResourcesCreateManagedResourcePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'alert_route'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ManagedResourcesCreateManagedResourceResultV2]
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
    body: ManagedResourcesCreateManagedResourcePayloadV2,
) -> ErrorResponse | ManagedResourcesCreateManagedResourceResultV2 | None:
    """CreateManagedResource Managed Resources V2

     Create or update the management record for a resource. This replaces any annotations already stored
    on it.

    The annotations set `managed_by`:
    - `incident.io/terraform/version` sets it to `terraform`.
    - `incident.io/is-managed-externally` sets it to `external`. If both keys are present, `external`
    wins.
    - Neither key sets it to `dashboard`.

    This doesn't change the resource's configuration, but `managed_by` controls whether it can be edited
    in the dashboard. Returning a schedule to `dashboard` also returns its sync rules and targets.

    The API key must have the update scope for the resource type, e.g. `schedules.update` for a
    schedule.

    Args:
        body (ManagedResourcesCreateManagedResourcePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'alert_route'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ManagedResourcesCreateManagedResourceResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ManagedResourcesCreateManagedResourcePayloadV2,
) -> Response[ErrorResponse | ManagedResourcesCreateManagedResourceResultV2]:
    """CreateManagedResource Managed Resources V2

     Create or update the management record for a resource. This replaces any annotations already stored
    on it.

    The annotations set `managed_by`:
    - `incident.io/terraform/version` sets it to `terraform`.
    - `incident.io/is-managed-externally` sets it to `external`. If both keys are present, `external`
    wins.
    - Neither key sets it to `dashboard`.

    This doesn't change the resource's configuration, but `managed_by` controls whether it can be edited
    in the dashboard. Returning a schedule to `dashboard` also returns its sync rules and targets.

    The API key must have the update scope for the resource type, e.g. `schedules.update` for a
    schedule.

    Args:
        body (ManagedResourcesCreateManagedResourcePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'alert_route'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ManagedResourcesCreateManagedResourceResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ManagedResourcesCreateManagedResourcePayloadV2,
) -> ErrorResponse | ManagedResourcesCreateManagedResourceResultV2 | None:
    """CreateManagedResource Managed Resources V2

     Create or update the management record for a resource. This replaces any annotations already stored
    on it.

    The annotations set `managed_by`:
    - `incident.io/terraform/version` sets it to `terraform`.
    - `incident.io/is-managed-externally` sets it to `external`. If both keys are present, `external`
    wins.
    - Neither key sets it to `dashboard`.

    This doesn't change the resource's configuration, but `managed_by` controls whether it can be edited
    in the dashboard. Returning a schedule to `dashboard` also returns its sync rules and targets.

    The API key must have the update scope for the resource type, e.g. `schedules.update` for a
    schedule.

    Args:
        body (ManagedResourcesCreateManagedResourcePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'alert_route'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ManagedResourcesCreateManagedResourceResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
