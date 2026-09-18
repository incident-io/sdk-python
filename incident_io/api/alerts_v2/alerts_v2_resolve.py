from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alerts_resolve_result_v2 import AlertsResolveResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/alerts/{id}/actions/resolve".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertsResolveResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlertsResolveResultV2.from_dict(response.json())

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
) -> Response[AlertsResolveResultV2 | ErrorResponse]:
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
) -> Response[AlertsResolveResultV2 | ErrorResponse]:
    """Resolve Alerts V2

     Resolve a currently firing alert.

    This marks the alert as resolved with the current time, attributing the resolution to the API key
    that made the request. Resolving an already-resolved alert is a no-op and returns the alert
    unchanged.

    Some alert sources are 'externally resolved' (for example, Datadog) — those alerts can only be
    resolved by the third-party system itself, and this endpoint will return a 422 explaining that.

    Private alerts: an API key without the 'view all alerts' scope can only resolve non-private alerts;
    private alerts will return a 404. Grant the API key a role that includes the global alerts access
    scope to resolve private alerts.

    Args:
        id (str): Unique identifier for the alert Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsResolveResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AlertsResolveResultV2 | ErrorResponse | None:
    """Resolve Alerts V2

     Resolve a currently firing alert.

    This marks the alert as resolved with the current time, attributing the resolution to the API key
    that made the request. Resolving an already-resolved alert is a no-op and returns the alert
    unchanged.

    Some alert sources are 'externally resolved' (for example, Datadog) — those alerts can only be
    resolved by the third-party system itself, and this endpoint will return a 422 explaining that.

    Private alerts: an API key without the 'view all alerts' scope can only resolve non-private alerts;
    private alerts will return a 404. Grant the API key a role that includes the global alerts access
    scope to resolve private alerts.

    Args:
        id (str): Unique identifier for the alert Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsResolveResultV2 | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AlertsResolveResultV2 | ErrorResponse]:
    """Resolve Alerts V2

     Resolve a currently firing alert.

    This marks the alert as resolved with the current time, attributing the resolution to the API key
    that made the request. Resolving an already-resolved alert is a no-op and returns the alert
    unchanged.

    Some alert sources are 'externally resolved' (for example, Datadog) — those alerts can only be
    resolved by the third-party system itself, and this endpoint will return a 422 explaining that.

    Private alerts: an API key without the 'view all alerts' scope can only resolve non-private alerts;
    private alerts will return a 404. Grant the API key a role that includes the global alerts access
    scope to resolve private alerts.

    Args:
        id (str): Unique identifier for the alert Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsResolveResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AlertsResolveResultV2 | ErrorResponse | None:
    """Resolve Alerts V2

     Resolve a currently firing alert.

    This marks the alert as resolved with the current time, attributing the resolution to the API key
    that made the request. Resolving an already-resolved alert is a no-op and returns the alert
    unchanged.

    Some alert sources are 'externally resolved' (for example, Datadog) — those alerts can only be
    resolved by the third-party system itself, and this endpoint will return a 422 explaining that.

    Private alerts: an API key without the 'view all alerts' scope can only resolve non-private alerts;
    private alerts will return a 404. Grant the API key a role that includes the global alerts access
    scope to resolve private alerts.

    Args:
        id (str): Unique identifier for the alert Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsResolveResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
