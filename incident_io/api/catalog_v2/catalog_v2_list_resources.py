from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_list_resources_result_v2 import CatalogListResourcesResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/catalog_resources",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogListResourcesResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CatalogListResourcesResultV2.from_dict(response.json())

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
) -> Response[CatalogListResourcesResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CatalogListResourcesResultV2 | ErrorResponse]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogListResourcesResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> CatalogListResourcesResultV2 | ErrorResponse | None:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogListResourcesResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CatalogListResourcesResultV2 | ErrorResponse]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogListResourcesResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> CatalogListResourcesResultV2 | ErrorResponse | None:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogListResourcesResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed


# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools  # noqa: E402
import warnings as _warnings  # noqa: E402

_DEPRECATION_MESSAGE = "GET /v2/catalog_resources is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement."

# sync() calls sync_detailed(), and both are wrapped, so a single user call
# would warn twice — the second time with a stacklevel pointing inside the SDK,
# which under -W error blames us for the user's call. This suppresses the inner
# warning. Module-level rather than thread-local because it is only ever set
# for the duration of one synchronous call frame.
_warning_in_progress = False


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        global _warning_in_progress
        if _warning_in_progress:
            return _fn(*args, **kwargs)
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        _warning_in_progress = True
        try:
            return _fn(*args, **kwargs)
        finally:
            _warning_in_progress = False

    return _wrapper


def _deprecated_async(_fn):
    # `async def`, so the result stays a coroutine function under
    # inspect.iscoroutinefunction. See this module's docstring.
    @_functools.wraps(_fn)
    async def _wrapper(*args, **kwargs):
        global _warning_in_progress
        if _warning_in_progress:
            return await _fn(*args, **kwargs)
        _warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
        _warning_in_progress = True
        try:
            return await _fn(*args, **kwargs)
        finally:
            _warning_in_progress = False

    return _wrapper


sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated_async(asyncio_detailed)
asyncio = _deprecated_async(asyncio)
