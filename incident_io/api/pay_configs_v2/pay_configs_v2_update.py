from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pay_configs_update_payload_v2 import PayConfigsUpdatePayloadV2
from ...models.pay_configs_update_result_v2 import PayConfigsUpdateResultV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PayConfigsUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/pay_configs/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PayConfigsUpdateResultV2 | None:
    if response.status_code == 200:
        response_200 = PayConfigsUpdateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | PayConfigsUpdateResultV2]:
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
    body: PayConfigsUpdatePayloadV2,
) -> Response[ErrorResponse | PayConfigsUpdateResultV2]:
    """Update Pay Configs V2

     Update a pay config's attributes.

    This changes the config's name, timezone, currency and base rate. It does not
    touch the config's rules, which are set when the config is created.

    Updating a config that a published report priced against additionally requires
    the schedule_pay_configs.update_published scope, because it changes the
    explanation of pay someone has already been sent.

    Args:
        id (str): Unique identifier for this pay config Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'rate_time_unit': 'hour', 'timezone': 'Europe/London'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsUpdateResultV2]
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
    body: PayConfigsUpdatePayloadV2,
) -> ErrorResponse | PayConfigsUpdateResultV2 | None:
    """Update Pay Configs V2

     Update a pay config's attributes.

    This changes the config's name, timezone, currency and base rate. It does not
    touch the config's rules, which are set when the config is created.

    Updating a config that a published report priced against additionally requires
    the schedule_pay_configs.update_published scope, because it changes the
    explanation of pay someone has already been sent.

    Args:
        id (str): Unique identifier for this pay config Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'rate_time_unit': 'hour', 'timezone': 'Europe/London'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsUpdateResultV2
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
    body: PayConfigsUpdatePayloadV2,
) -> Response[ErrorResponse | PayConfigsUpdateResultV2]:
    """Update Pay Configs V2

     Update a pay config's attributes.

    This changes the config's name, timezone, currency and base rate. It does not
    touch the config's rules, which are set when the config is created.

    Updating a config that a published report priced against additionally requires
    the schedule_pay_configs.update_published scope, because it changes the
    explanation of pay someone has already been sent.

    Args:
        id (str): Unique identifier for this pay config Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'rate_time_unit': 'hour', 'timezone': 'Europe/London'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsUpdateResultV2]
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
    body: PayConfigsUpdatePayloadV2,
) -> ErrorResponse | PayConfigsUpdateResultV2 | None:
    """Update Pay Configs V2

     Update a pay config's attributes.

    This changes the config's name, timezone, currency and base rate. It does not
    touch the config's rules, which are set when the config is created.

    Updating a config that a published report priced against additionally requires
    the schedule_pay_configs.update_published scope, because it changes the
    explanation of pay someone has already been sent.

    Args:
        id (str): Unique identifier for this pay config Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'rate_time_unit': 'hour', 'timezone': 'Europe/London'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsUpdateResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
