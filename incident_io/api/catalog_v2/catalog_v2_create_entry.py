from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_create_entry_payload_v2 import CatalogCreateEntryPayloadV2
from ...models.catalog_create_entry_result_v2 import CatalogCreateEntryResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CatalogCreateEntryPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/catalog_entries",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogCreateEntryResultV2 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CatalogCreateEntryResultV2.from_dict(response.json())

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
) -> Response[CatalogCreateEntryResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateEntryPayloadV2,
) -> Response[CatalogCreateEntryResultV2 | ErrorResponse]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogCreateEntryPayloadV2):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCreateEntryResultV2 | ErrorResponse]
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
    body: CatalogCreateEntryPayloadV2,
) -> CatalogCreateEntryResultV2 | ErrorResponse | None:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogCreateEntryPayloadV2):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCreateEntryResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateEntryPayloadV2,
) -> Response[CatalogCreateEntryResultV2 | ErrorResponse]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogCreateEntryPayloadV2):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCreateEntryResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateEntryPayloadV2,
) -> CatalogCreateEntryResultV2 | ErrorResponse | None:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogCreateEntryPayloadV2):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCreateEntryResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools  # noqa: E402
import warnings as _warnings  # noqa: E402

_DEPRECATION_MESSAGE = "POST /v2/catalog_entries is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement."


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        return _fn(*args, **kwargs)

    return _wrapper


def _deprecated_async(_fn):
    # `async def`, so the result stays a coroutine function under
    # inspect.iscoroutinefunction. See this module's docstring.
    @_functools.wraps(_fn)
    async def _wrapper(*args, **kwargs):
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        return await _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated_async(asyncio_detailed)
asyncio = _deprecated_async(asyncio)
