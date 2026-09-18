from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pay_configs_update_one_off_rule_payload_v2 import (
    PayConfigsUpdateOneOffRulePayloadV2,
)
from ...models.pay_configs_update_one_off_rule_result_v2 import (
    PayConfigsUpdateOneOffRuleResultV2,
)
from ...types import Response


def _get_kwargs(
    pay_config_id: str,
    id: str,
    *,
    body: PayConfigsUpdateOneOffRulePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/pay_configs/{pay_config_id}/one_off_rules/{id}".format(
            pay_config_id=quote(str(pay_config_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PayConfigsUpdateOneOffRuleResultV2 | None:
    if response.status_code == 200:
        response_200 = PayConfigsUpdateOneOffRuleResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | PayConfigsUpdateOneOffRuleResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pay_config_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsUpdateOneOffRulePayloadV2,
) -> Response[ErrorResponse | PayConfigsUpdateOneOffRuleResultV2]:
    """UpdateOneOffRule Pay Configs V2

     Update a one-off rule. It may not be moved to overlap another rule on the same config.

    Args:
        pay_config_id (str): The pay config's ID Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        id (str): Unique identifier for this rule, stable across edits to the config Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdateOneOffRulePayloadV2):  Example: {'end_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsUpdateOneOffRuleResultV2]
    """

    kwargs = _get_kwargs(
        pay_config_id=pay_config_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pay_config_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsUpdateOneOffRulePayloadV2,
) -> ErrorResponse | PayConfigsUpdateOneOffRuleResultV2 | None:
    """UpdateOneOffRule Pay Configs V2

     Update a one-off rule. It may not be moved to overlap another rule on the same config.

    Args:
        pay_config_id (str): The pay config's ID Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        id (str): Unique identifier for this rule, stable across edits to the config Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdateOneOffRulePayloadV2):  Example: {'end_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsUpdateOneOffRuleResultV2
    """

    return sync_detailed(
        pay_config_id=pay_config_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pay_config_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsUpdateOneOffRulePayloadV2,
) -> Response[ErrorResponse | PayConfigsUpdateOneOffRuleResultV2]:
    """UpdateOneOffRule Pay Configs V2

     Update a one-off rule. It may not be moved to overlap another rule on the same config.

    Args:
        pay_config_id (str): The pay config's ID Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        id (str): Unique identifier for this rule, stable across edits to the config Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdateOneOffRulePayloadV2):  Example: {'end_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PayConfigsUpdateOneOffRuleResultV2]
    """

    kwargs = _get_kwargs(
        pay_config_id=pay_config_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pay_config_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PayConfigsUpdateOneOffRulePayloadV2,
) -> ErrorResponse | PayConfigsUpdateOneOffRuleResultV2 | None:
    """UpdateOneOffRule Pay Configs V2

     Update a one-off rule. It may not be moved to overlap another rule on the same config.

    Args:
        pay_config_id (str): The pay config's ID Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        id (str): Unique identifier for this rule, stable across edits to the config Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        body (PayConfigsUpdateOneOffRulePayloadV2):  Example: {'end_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Christmas day', 'rate_cents': 4800, 'start_at':
            '2021-08-17T13:28:57.801578Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PayConfigsUpdateOneOffRuleResultV2
    """

    return (
        await asyncio_detailed(
            pay_config_id=pay_config_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
