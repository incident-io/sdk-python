from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_connect_external_issue_payload_v2 import (
    IncidentsConnectExternalIssuePayloadV2,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentsConnectExternalIssuePayloadV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents/{id}/actions/connect_external_issue".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ErrorResponse]:
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
    body: IncidentsConnectExternalIssuePayloadV2,
) -> Response[Any | ErrorResponse]:
    """ConnectExternalIssue Incidents V2

     Connect an existing issue in an issue tracker to an incident, as its external issue.

    The issue is synced using the given incident ticket template, as if incident.io had
    created it from that template. The next sync writes the incident's fields into the issue.

    This needs the incidents.connect_external_issue scope, either across the organisation or
    from an incident role on this incident.

    This fails if the incident already has a different external issue (unless replace is
    true), or if the issue is already linked to another incident or follow-up.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference.

    Args:
        id (str): The unique identifier of the incident Example: 01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsConnectExternalIssuePayloadV2):  Example: {'issue_template_id':
            '01GBA8J19SMXQWPJMX3P2ESCVG', 'provider': 'jira', 'replace': False, 'url':
            'https://example.atlassian.net/browse/OPS-42'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
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
    body: IncidentsConnectExternalIssuePayloadV2,
) -> Any | ErrorResponse | None:
    """ConnectExternalIssue Incidents V2

     Connect an existing issue in an issue tracker to an incident, as its external issue.

    The issue is synced using the given incident ticket template, as if incident.io had
    created it from that template. The next sync writes the incident's fields into the issue.

    This needs the incidents.connect_external_issue scope, either across the organisation or
    from an incident role on this incident.

    This fails if the incident already has a different external issue (unless replace is
    true), or if the issue is already linked to another incident or follow-up.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference.

    Args:
        id (str): The unique identifier of the incident Example: 01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsConnectExternalIssuePayloadV2):  Example: {'issue_template_id':
            '01GBA8J19SMXQWPJMX3P2ESCVG', 'provider': 'jira', 'replace': False, 'url':
            'https://example.atlassian.net/browse/OPS-42'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
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
    body: IncidentsConnectExternalIssuePayloadV2,
) -> Response[Any | ErrorResponse]:
    """ConnectExternalIssue Incidents V2

     Connect an existing issue in an issue tracker to an incident, as its external issue.

    The issue is synced using the given incident ticket template, as if incident.io had
    created it from that template. The next sync writes the incident's fields into the issue.

    This needs the incidents.connect_external_issue scope, either across the organisation or
    from an incident role on this incident.

    This fails if the incident already has a different external issue (unless replace is
    true), or if the issue is already linked to another incident or follow-up.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference.

    Args:
        id (str): The unique identifier of the incident Example: 01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsConnectExternalIssuePayloadV2):  Example: {'issue_template_id':
            '01GBA8J19SMXQWPJMX3P2ESCVG', 'provider': 'jira', 'replace': False, 'url':
            'https://example.atlassian.net/browse/OPS-42'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
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
    body: IncidentsConnectExternalIssuePayloadV2,
) -> Any | ErrorResponse | None:
    """ConnectExternalIssue Incidents V2

     Connect an existing issue in an issue tracker to an incident, as its external issue.

    The issue is synced using the given incident ticket template, as if incident.io had
    created it from that template. The next sync writes the incident's fields into the issue.

    This needs the incidents.connect_external_issue scope, either across the organisation or
    from an incident role on this incident.

    This fails if the incident already has a different external issue (unless replace is
    true), or if the issue is already linked to another incident or follow-up.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference.

    Args:
        id (str): The unique identifier of the incident Example: 01G18REBY9AYH6CMWCJ2CVCYCH.
        body (IncidentsConnectExternalIssuePayloadV2):  Example: {'issue_template_id':
            '01GBA8J19SMXQWPJMX3P2ESCVG', 'provider': 'jira', 'replace': False, 'url':
            'https://example.atlassian.net/browse/OPS-42'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
