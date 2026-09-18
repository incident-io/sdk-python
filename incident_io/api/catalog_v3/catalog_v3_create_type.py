from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_create_type_payload_v3 import CatalogCreateTypePayloadV3
from ...models.catalog_create_type_result_v3 import CatalogCreateTypeResultV3
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CatalogCreateTypePayloadV3,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/catalog_types",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogCreateTypeResultV3 | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CatalogCreateTypeResultV3.from_dict(response.json())

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
) -> Response[CatalogCreateTypeResultV3 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateTypePayloadV3,
) -> Response[CatalogCreateTypeResultV3 | ErrorResponse]:
    """CreateType Catalog V3

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV3):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog',
            'type_name': 'Custom["BackstageGroup"]', 'use_name_as_identifier': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCreateTypeResultV3 | ErrorResponse]
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
    body: CatalogCreateTypePayloadV3,
) -> CatalogCreateTypeResultV3 | ErrorResponse | None:
    """CreateType Catalog V3

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV3):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog',
            'type_name': 'Custom["BackstageGroup"]', 'use_name_as_identifier': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCreateTypeResultV3 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateTypePayloadV3,
) -> Response[CatalogCreateTypeResultV3 | ErrorResponse]:
    """CreateType Catalog V3

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV3):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog',
            'type_name': 'Custom["BackstageGroup"]', 'use_name_as_identifier': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCreateTypeResultV3 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CatalogCreateTypePayloadV3,
) -> CatalogCreateTypeResultV3 | ErrorResponse | None:
    """CreateType Catalog V3

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV3):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog',
            'type_name': 'Custom["BackstageGroup"]', 'use_name_as_identifier': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCreateTypeResultV3 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
