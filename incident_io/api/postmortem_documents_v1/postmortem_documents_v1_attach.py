from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.postmortem_documents_attach_payload_v1 import (
    PostmortemDocumentsAttachPayloadV1,
)
from ...models.postmortem_documents_attach_result_v1 import (
    PostmortemDocumentsAttachResultV1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostmortemDocumentsAttachPayloadV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/postmortem_documents/actions/attach",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostmortemDocumentsAttachResultV1 | None:
    if response.status_code == 201:
        response_201 = PostmortemDocumentsAttachResultV1.from_dict(response.json())

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
) -> Response[ErrorResponse | PostmortemDocumentsAttachResultV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostmortemDocumentsAttachPayloadV1,
) -> Response[ErrorResponse | PostmortemDocumentsAttachResultV1]:
    """Attach PostmortemDocuments V1

     Link an externally-hosted post-mortem document to an incident.

    Use this to attach a retrospective document you've created in your own provider (for example
    Confluence, Notion, or Google Docs) to an existing incident. This is the API equivalent of
    pasting a document link into the incident.io dashboard, and is useful for automating your
    retrospective workflow - for example, creating a document in the right space with the right
    permissions when an incident is opened, then linking it back to the incident.

    Only one external post-mortem can be attached to an incident, and you cannot attach an external
    document to an incident that already has an in-app post-mortem. Re-attaching the same incident
    with a new permalink updates the existing link.

    Args:
        body (PostmortemDocumentsAttachPayloadV1):  Example: {'document_provider': 'notion',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'permalink':
            'https://www.notion.so/INC-123-database-is-sad'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostmortemDocumentsAttachResultV1]
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
    body: PostmortemDocumentsAttachPayloadV1,
) -> ErrorResponse | PostmortemDocumentsAttachResultV1 | None:
    """Attach PostmortemDocuments V1

     Link an externally-hosted post-mortem document to an incident.

    Use this to attach a retrospective document you've created in your own provider (for example
    Confluence, Notion, or Google Docs) to an existing incident. This is the API equivalent of
    pasting a document link into the incident.io dashboard, and is useful for automating your
    retrospective workflow - for example, creating a document in the right space with the right
    permissions when an incident is opened, then linking it back to the incident.

    Only one external post-mortem can be attached to an incident, and you cannot attach an external
    document to an incident that already has an in-app post-mortem. Re-attaching the same incident
    with a new permalink updates the existing link.

    Args:
        body (PostmortemDocumentsAttachPayloadV1):  Example: {'document_provider': 'notion',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'permalink':
            'https://www.notion.so/INC-123-database-is-sad'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostmortemDocumentsAttachResultV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostmortemDocumentsAttachPayloadV1,
) -> Response[ErrorResponse | PostmortemDocumentsAttachResultV1]:
    """Attach PostmortemDocuments V1

     Link an externally-hosted post-mortem document to an incident.

    Use this to attach a retrospective document you've created in your own provider (for example
    Confluence, Notion, or Google Docs) to an existing incident. This is the API equivalent of
    pasting a document link into the incident.io dashboard, and is useful for automating your
    retrospective workflow - for example, creating a document in the right space with the right
    permissions when an incident is opened, then linking it back to the incident.

    Only one external post-mortem can be attached to an incident, and you cannot attach an external
    document to an incident that already has an in-app post-mortem. Re-attaching the same incident
    with a new permalink updates the existing link.

    Args:
        body (PostmortemDocumentsAttachPayloadV1):  Example: {'document_provider': 'notion',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'permalink':
            'https://www.notion.so/INC-123-database-is-sad'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostmortemDocumentsAttachResultV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostmortemDocumentsAttachPayloadV1,
) -> ErrorResponse | PostmortemDocumentsAttachResultV1 | None:
    """Attach PostmortemDocuments V1

     Link an externally-hosted post-mortem document to an incident.

    Use this to attach a retrospective document you've created in your own provider (for example
    Confluence, Notion, or Google Docs) to an existing incident. This is the API equivalent of
    pasting a document link into the incident.io dashboard, and is useful for automating your
    retrospective workflow - for example, creating a document in the right space with the right
    permissions when an incident is opened, then linking it back to the incident.

    Only one external post-mortem can be attached to an incident, and you cannot attach an external
    document to an incident that already has an in-app post-mortem. Re-attaching the same incident
    with a new permalink updates the existing link.

    Args:
        body (PostmortemDocumentsAttachPayloadV1):  Example: {'document_provider': 'notion',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'permalink':
            'https://www.notion.so/INC-123-database-is-sad'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostmortemDocumentsAttachResultV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
