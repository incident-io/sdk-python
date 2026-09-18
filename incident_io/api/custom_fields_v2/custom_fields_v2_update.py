from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_update_payload_v2 import CustomFieldsUpdatePayloadV2
from ...models.custom_fields_update_result_v2 import CustomFieldsUpdateResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CustomFieldsUpdatePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/custom_fields/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldsUpdateResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CustomFieldsUpdateResultV2.from_dict(response.json())

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
) -> Response[CustomFieldsUpdateResultV2 | ErrorResponse]:
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
    body: CustomFieldsUpdatePayloadV2,
) -> Response[CustomFieldsUpdateResultV2 | ErrorResponse]:
    """Update Custom Fields V2

     Update the details of a custom field

    Args:
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CustomFieldsUpdatePayloadV2):  Example: {'description': 'Which team is impacted by
            this issue', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0',
            'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsUpdateResultV2 | ErrorResponse]
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
    body: CustomFieldsUpdatePayloadV2,
) -> CustomFieldsUpdateResultV2 | ErrorResponse | None:
    """Update Custom Fields V2

     Update the details of a custom field

    Args:
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CustomFieldsUpdatePayloadV2):  Example: {'description': 'Which team is impacted by
            this issue', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0',
            'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsUpdateResultV2 | ErrorResponse
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
    body: CustomFieldsUpdatePayloadV2,
) -> Response[CustomFieldsUpdateResultV2 | ErrorResponse]:
    """Update Custom Fields V2

     Update the details of a custom field

    Args:
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CustomFieldsUpdatePayloadV2):  Example: {'description': 'Which team is impacted by
            this issue', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0',
            'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsUpdateResultV2 | ErrorResponse]
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
    body: CustomFieldsUpdatePayloadV2,
) -> CustomFieldsUpdateResultV2 | ErrorResponse | None:
    """Update Custom Fields V2

     Update the details of a custom field

    Args:
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CustomFieldsUpdatePayloadV2):  Example: {'description': 'Which team is impacted by
            this issue', 'filter_by': {'catalog_attribute_id': '01H2FW182TAH0NHEVBY34SCAK0',
            'custom_field_id': '01H2FW182TAH0NHEVBY34SCAK0'}, 'fixed_filter': {'catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'values': ['01H2FW182TAH0NHEVBY34SCAK0',
            '01H2FW182TAH0NHEVBY34SCAK1']}, 'group_by_catalog_attribute_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'helptext_catalog_attribute_id':
            '01H2FW182TAH0NHEVBY34SCAK0', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsUpdateResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
