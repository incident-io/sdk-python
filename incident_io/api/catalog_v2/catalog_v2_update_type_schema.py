from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_update_type_schema_payload_v2 import (
    CatalogUpdateTypeSchemaPayloadV2,
)
from ...models.catalog_update_type_schema_result_v2 import (
    CatalogUpdateTypeSchemaResultV2,
)
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CatalogUpdateTypeSchemaPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/catalog_types/{id}/actions/update_schema".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogUpdateTypeSchemaResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CatalogUpdateTypeSchemaResultV2.from_dict(response.json())

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
) -> Response[CatalogUpdateTypeSchemaResultV2 | ErrorResponse]:
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
    body: CatalogUpdateTypeSchemaPayloadV2,
) -> Response[CatalogUpdateTypeSchemaResultV2 | ErrorResponse]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CatalogUpdateTypeSchemaPayloadV2):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name':
            'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}], 'version':
            1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogUpdateTypeSchemaResultV2 | ErrorResponse]
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
    body: CatalogUpdateTypeSchemaPayloadV2,
) -> CatalogUpdateTypeSchemaResultV2 | ErrorResponse | None:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CatalogUpdateTypeSchemaPayloadV2):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name':
            'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}], 'version':
            1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogUpdateTypeSchemaResultV2 | ErrorResponse
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
    body: CatalogUpdateTypeSchemaPayloadV2,
) -> Response[CatalogUpdateTypeSchemaResultV2 | ErrorResponse]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CatalogUpdateTypeSchemaPayloadV2):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name':
            'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}], 'version':
            1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogUpdateTypeSchemaResultV2 | ErrorResponse]
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
    body: CatalogUpdateTypeSchemaPayloadV2,
) -> CatalogUpdateTypeSchemaResultV2 | ErrorResponse | None:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        body (CatalogUpdateTypeSchemaPayloadV2):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name':
            'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}], 'version':
            1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogUpdateTypeSchemaResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed

# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools
import warnings as _warnings


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(
            "POST /v2/catalog_types/{id}/actions/update_schema is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated(asyncio_detailed)
asyncio = _deprecated(asyncio)
