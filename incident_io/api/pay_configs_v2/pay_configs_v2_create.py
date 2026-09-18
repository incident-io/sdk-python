from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pay_configs_create_payload_v2 import PayConfigsCreatePayloadV2
from ...models.pay_configs_create_result_v2 import PayConfigsCreateResultV2
from ...types import Response


def _get_kwargs(
    *,
    body: PayConfigsCreatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/pay_configs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PayConfigsCreateResultV2 | None:
    if response.status_code == 201:
        response_201 = PayConfigsCreateResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | PayConfigsCreateResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsCreatePayloadV2,
) -> Response[ErrorResponse | PayConfigsCreateResultV2]:
    """Create Pay Configs V2

     Create a pay config.

    The config is created as a draft, and becomes visible to everyone in the
    organisation once a report that prices against it is published.

    Args:
        body (PayConfigsCreatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'rate_time_unit': 'hour', 'timezone':
            'Europe/London', 'weekly_rules': [{'end_time': '17:00', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsCreateResultV2]
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
    body: PayConfigsCreatePayloadV2,
) -> ErrorResponse | PayConfigsCreateResultV2 | None:
    """Create Pay Configs V2

     Create a pay config.

    The config is created as a draft, and becomes visible to everyone in the
    organisation once a report that prices against it is published.

    Args:
        body (PayConfigsCreatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'rate_time_unit': 'hour', 'timezone':
            'Europe/London', 'weekly_rules': [{'end_time': '17:00', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsCreateResultV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsCreatePayloadV2,
) -> Response[ErrorResponse | PayConfigsCreateResultV2]:
    """Create Pay Configs V2

     Create a pay config.

    The config is created as a draft, and becomes visible to everyone in the
    organisation once a report that prices against it is published.

    Args:
        body (PayConfigsCreatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'rate_time_unit': 'hour', 'timezone':
            'Europe/London', 'weekly_rules': [{'end_time': '17:00', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsCreateResultV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsCreatePayloadV2,
) -> ErrorResponse | PayConfigsCreateResultV2 | None:
    """Create Pay Configs V2

     Create a pay config.

    The config is created as a draft, and becomes visible to everyone in the
    organisation once a report that prices against it is published.

    Args:
        body (PayConfigsCreatePayloadV2):  Example: {'base_rate_cents': 1200, 'currency': 'GBP',
            'name': 'Engineering on-call', 'one_off_rules': [{'end_at': '2021-08-17T13:28:57.801578Z',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Christmas day', 'rate_cents': 4800,
            'start_at': '2021-08-17T13:28:57.801578Z'}], 'rate_time_unit': 'hour', 'timezone':
            'Europe/London', 'weekly_rules': [{'end_time': '17:00', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'rate_cents': 2400, 'start_time': '09:00', 'weekdays':
            ['monday']}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsCreateResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
