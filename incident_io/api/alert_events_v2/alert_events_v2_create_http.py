from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_events_create_http_payload_v2 import AlertEventsCreateHTTPPayloadV2
from ...models.alert_events_create_http_result_v2 import AlertEventsCreateHTTPResultV2
from ...models.alert_events_v2_create_http_query import AlertEventsV2CreateHttpQuery
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_source_config_id: str,
    *,
    body: AlertEventsCreateHTTPPayloadV2,
    token: str | Unset = UNSET,
    query: AlertEventsV2CreateHttpQuery | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["token"] = token

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/alert_events/http/{alert_source_config_id}".format(
            alert_source_config_id=quote(str(alert_source_config_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertEventsCreateHTTPResultV2 | ErrorResponse | None:
    if response.status_code == 202:
        response_202 = AlertEventsCreateHTTPResultV2.from_dict(response.json())

        return response_202

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
) -> Response[AlertEventsCreateHTTPResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_source_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AlertEventsCreateHTTPPayloadV2,
    token: str | Unset = UNSET,
    query: AlertEventsV2CreateHttpQuery | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[AlertEventsCreateHTTPResultV2 | ErrorResponse]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str): Which alert source config produced this alert Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (str | Unset): Token used to authenticate the request, generated when configuring
            the alert source. Will be consumed via a URL query string parameter Example: some-random-
            string.
        query (AlertEventsV2CreateHttpQuery | Unset):
        authorization (str | Unset): Whatever is provided in the Authorization header. We support
            either Basic or Bearer authorization with the secret provided on the alert source.
            Example: some-random-string.
        body (AlertEventsCreateHTTPPayloadV2):  Example: {'deduplication_key': '4293868629',
            'description': "We've detected a number of timeouts on hello.world.com, the service may be
            down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']},
            'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status':
            'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventsCreateHTTPResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
        body=body,
        token=token,
        query=query,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_source_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AlertEventsCreateHTTPPayloadV2,
    token: str | Unset = UNSET,
    query: AlertEventsV2CreateHttpQuery | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> AlertEventsCreateHTTPResultV2 | ErrorResponse | None:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str): Which alert source config produced this alert Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (str | Unset): Token used to authenticate the request, generated when configuring
            the alert source. Will be consumed via a URL query string parameter Example: some-random-
            string.
        query (AlertEventsV2CreateHttpQuery | Unset):
        authorization (str | Unset): Whatever is provided in the Authorization header. We support
            either Basic or Bearer authorization with the secret provided on the alert source.
            Example: some-random-string.
        body (AlertEventsCreateHTTPPayloadV2):  Example: {'deduplication_key': '4293868629',
            'description': "We've detected a number of timeouts on hello.world.com, the service may be
            down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']},
            'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status':
            'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventsCreateHTTPResultV2 | ErrorResponse
    """

    return sync_detailed(
        alert_source_config_id=alert_source_config_id,
        client=client,
        body=body,
        token=token,
        query=query,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    alert_source_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AlertEventsCreateHTTPPayloadV2,
    token: str | Unset = UNSET,
    query: AlertEventsV2CreateHttpQuery | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[AlertEventsCreateHTTPResultV2 | ErrorResponse]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str): Which alert source config produced this alert Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (str | Unset): Token used to authenticate the request, generated when configuring
            the alert source. Will be consumed via a URL query string parameter Example: some-random-
            string.
        query (AlertEventsV2CreateHttpQuery | Unset):
        authorization (str | Unset): Whatever is provided in the Authorization header. We support
            either Basic or Bearer authorization with the secret provided on the alert source.
            Example: some-random-string.
        body (AlertEventsCreateHTTPPayloadV2):  Example: {'deduplication_key': '4293868629',
            'description': "We've detected a number of timeouts on hello.world.com, the service may be
            down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']},
            'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status':
            'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventsCreateHTTPResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
        body=body,
        token=token,
        query=query,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_source_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AlertEventsCreateHTTPPayloadV2,
    token: str | Unset = UNSET,
    query: AlertEventsV2CreateHttpQuery | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> AlertEventsCreateHTTPResultV2 | ErrorResponse | None:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str): Which alert source config produced this alert Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (str | Unset): Token used to authenticate the request, generated when configuring
            the alert source. Will be consumed via a URL query string parameter Example: some-random-
            string.
        query (AlertEventsV2CreateHttpQuery | Unset):
        authorization (str | Unset): Whatever is provided in the Authorization header. We support
            either Basic or Bearer authorization with the secret provided on the alert source.
            Example: some-random-string.
        body (AlertEventsCreateHTTPPayloadV2):  Example: {'deduplication_key': '4293868629',
            'description': "We've detected a number of timeouts on hello.world.com, the service may be
            down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']},
            'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status':
            'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventsCreateHTTPResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            alert_source_config_id=alert_source_config_id,
            client=client,
            body=body,
            token=token,
            query=query,
            authorization=authorization,
        )
    ).parsed
