from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_import_postmortem_document_payload_v2 import (
    IncidentsImportPostmortemDocumentPayloadV2,
)
from ...models.incidents_import_postmortem_document_result_v2 import (
    IncidentsImportPostmortemDocumentResultV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentsImportPostmortemDocumentPayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents/{id}/actions/import_postmortem_document".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentsImportPostmortemDocumentResultV2 | None:
    if response.status_code == 201:
        response_201 = IncidentsImportPostmortemDocumentResultV2.from_dict(
            response.json()
        )

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
) -> Response[ErrorResponse | IncidentsImportPostmortemDocumentResultV2]:
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
    body: IncidentsImportPostmortemDocumentPayloadV2,
) -> Response[ErrorResponse | IncidentsImportPostmortemDocumentResultV2]:
    """ImportPostmortemDocument Incidents V2

     Import a postmortem document from markdown into an incident.

    The document content should be provided as GitHub-Flavored Markdown. It will be
    parsed and converted into the collaborative editor format, and a new postmortem
    document will be created for the incident.

    If no main postmortem document exists for the incident, the imported document
    will become the main document.

    Args:
        id (str): The unique identifier of the incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        body (IncidentsImportPostmortemDocumentPayloadV2):  Example: {'content': '##
            Summary\\n\\nA database migration caused increased latency...', 'title': 'INC-123: Post-
            incident review'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsImportPostmortemDocumentResultV2]
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
    body: IncidentsImportPostmortemDocumentPayloadV2,
) -> ErrorResponse | IncidentsImportPostmortemDocumentResultV2 | None:
    """ImportPostmortemDocument Incidents V2

     Import a postmortem document from markdown into an incident.

    The document content should be provided as GitHub-Flavored Markdown. It will be
    parsed and converted into the collaborative editor format, and a new postmortem
    document will be created for the incident.

    If no main postmortem document exists for the incident, the imported document
    will become the main document.

    Args:
        id (str): The unique identifier of the incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        body (IncidentsImportPostmortemDocumentPayloadV2):  Example: {'content': '##
            Summary\\n\\nA database migration caused increased latency...', 'title': 'INC-123: Post-
            incident review'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsImportPostmortemDocumentResultV2
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
    body: IncidentsImportPostmortemDocumentPayloadV2,
) -> Response[ErrorResponse | IncidentsImportPostmortemDocumentResultV2]:
    """ImportPostmortemDocument Incidents V2

     Import a postmortem document from markdown into an incident.

    The document content should be provided as GitHub-Flavored Markdown. It will be
    parsed and converted into the collaborative editor format, and a new postmortem
    document will be created for the incident.

    If no main postmortem document exists for the incident, the imported document
    will become the main document.

    Args:
        id (str): The unique identifier of the incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        body (IncidentsImportPostmortemDocumentPayloadV2):  Example: {'content': '##
            Summary\\n\\nA database migration caused increased latency...', 'title': 'INC-123: Post-
            incident review'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsImportPostmortemDocumentResultV2]
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
    body: IncidentsImportPostmortemDocumentPayloadV2,
) -> ErrorResponse | IncidentsImportPostmortemDocumentResultV2 | None:
    """ImportPostmortemDocument Incidents V2

     Import a postmortem document from markdown into an incident.

    The document content should be provided as GitHub-Flavored Markdown. It will be
    parsed and converted into the collaborative editor format, and a new postmortem
    document will be created for the incident.

    If no main postmortem document exists for the incident, the imported document
    will become the main document.

    Args:
        id (str): The unique identifier of the incident Example: 01GBA8J19SMXQWPJMX3P2ESCVG.
        body (IncidentsImportPostmortemDocumentPayloadV2):  Example: {'content': '##
            Summary\\n\\nA database migration caused increased latency...', 'title': 'INC-123: Post-
            incident review'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsImportPostmortemDocumentResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
