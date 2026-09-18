from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_list_result_v3 import ActionsListResultV3
from ...models.actions_v3_list_created_at import ActionsV3ListCreatedAt
from ...models.actions_v3_list_incident_mode import ActionsV3ListIncidentMode
from ...models.actions_v3_list_updated_at import ActionsV3ListUpdatedAt
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV3ListIncidentMode | Unset = UNSET,
    created_at: ActionsV3ListCreatedAt | Unset = UNSET,
    updated_at: ActionsV3ListUpdatedAt | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params["incident_id"] = incident_id

    json_incident_mode: str | Unset = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value

    params["incident_mode"] = json_incident_mode

    json_created_at: dict[str, Any] | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.to_dict()
    if not isinstance(json_created_at, Unset):
        params.update(json_created_at)

    json_updated_at: dict[str, Any] | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.to_dict()
    if not isinstance(json_updated_at, Unset):
        params.update(json_updated_at)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionsListResultV3 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ActionsListResultV3.from_dict(response.json())

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
) -> Response[ActionsListResultV3 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV3ListIncidentMode | Unset = UNSET,
    created_at: ActionsV3ListCreatedAt | Unset = UNSET,
    updated_at: ActionsV3ListUpdatedAt | Unset = UNSET,
) -> Response[ActionsListResultV3 | ErrorResponse]:
    """ List Actions V3

     List actions for an organisation.

    Results are paginated and ordered by action ID, oldest first. Use the <code>after</code>
    value from <code>pagination_meta</code> to fetch the next page; it is only set when there
    may be more results.

    ### By created_at and updated_at

    Both timestamp filters accept the operators "gte" (greater than or equal to), "lte" (less
    than or equal to) and "date_range" (between two dates). The following example finds all
    actions updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    To find actions created within a specific date range, use the date_range operator with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    Filtering on updated_at is useful for incrementally syncing actions: poll with
    updated_at[gte] set to your last sync time instead of re-fetching the full history. Two
    caveats: updated_at moves whenever the action row itself is written, but changes to
    embedded objects (e.g. an assignee being renamed) can alter the payload without bumping
    it. And timestamps are stamped before commit, so an action can become visible with an
    older updated_at than rows you have already seen — overlap your sync window by a few
    minutes to allow for writes that commit out of timestamp order.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An action's ID. This endpoint will return a list of actions after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV3ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.
        created_at (ActionsV3ListCreatedAt | Unset): Filter on action created at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (ActionsV3ListUpdatedAt | Unset): Filter on action updated at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsListResultV3 | ErrorResponse]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        incident_mode=incident_mode,
        created_at=created_at,
        updated_at=updated_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV3ListIncidentMode | Unset = UNSET,
    created_at: ActionsV3ListCreatedAt | Unset = UNSET,
    updated_at: ActionsV3ListUpdatedAt | Unset = UNSET,
) -> ActionsListResultV3 | ErrorResponse | None:
    """ List Actions V3

     List actions for an organisation.

    Results are paginated and ordered by action ID, oldest first. Use the <code>after</code>
    value from <code>pagination_meta</code> to fetch the next page; it is only set when there
    may be more results.

    ### By created_at and updated_at

    Both timestamp filters accept the operators "gte" (greater than or equal to), "lte" (less
    than or equal to) and "date_range" (between two dates). The following example finds all
    actions updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    To find actions created within a specific date range, use the date_range operator with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    Filtering on updated_at is useful for incrementally syncing actions: poll with
    updated_at[gte] set to your last sync time instead of re-fetching the full history. Two
    caveats: updated_at moves whenever the action row itself is written, but changes to
    embedded objects (e.g. an assignee being renamed) can alter the payload without bumping
    it. And timestamps are stamped before commit, so an action can become visible with an
    older updated_at than rows you have already seen — overlap your sync window by a few
    minutes to allow for writes that commit out of timestamp order.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An action's ID. This endpoint will return a list of actions after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV3ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.
        created_at (ActionsV3ListCreatedAt | Unset): Filter on action created at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (ActionsV3ListUpdatedAt | Unset): Filter on action updated at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsListResultV3 | ErrorResponse
     """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        incident_mode=incident_mode,
        created_at=created_at,
        updated_at=updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV3ListIncidentMode | Unset = UNSET,
    created_at: ActionsV3ListCreatedAt | Unset = UNSET,
    updated_at: ActionsV3ListUpdatedAt | Unset = UNSET,
) -> Response[ActionsListResultV3 | ErrorResponse]:
    """ List Actions V3

     List actions for an organisation.

    Results are paginated and ordered by action ID, oldest first. Use the <code>after</code>
    value from <code>pagination_meta</code> to fetch the next page; it is only set when there
    may be more results.

    ### By created_at and updated_at

    Both timestamp filters accept the operators "gte" (greater than or equal to), "lte" (less
    than or equal to) and "date_range" (between two dates). The following example finds all
    actions updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    To find actions created within a specific date range, use the date_range operator with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    Filtering on updated_at is useful for incrementally syncing actions: poll with
    updated_at[gte] set to your last sync time instead of re-fetching the full history. Two
    caveats: updated_at moves whenever the action row itself is written, but changes to
    embedded objects (e.g. an assignee being renamed) can alter the payload without bumping
    it. And timestamps are stamped before commit, so an action can become visible with an
    older updated_at than rows you have already seen — overlap your sync window by a few
    minutes to allow for writes that commit out of timestamp order.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An action's ID. This endpoint will return a list of actions after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV3ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.
        created_at (ActionsV3ListCreatedAt | Unset): Filter on action created at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (ActionsV3ListUpdatedAt | Unset): Filter on action updated at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsListResultV3 | ErrorResponse]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        incident_id=incident_id,
        incident_mode=incident_mode,
        created_at=created_at,
        updated_at=updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV3ListIncidentMode | Unset = UNSET,
    created_at: ActionsV3ListCreatedAt | Unset = UNSET,
    updated_at: ActionsV3ListUpdatedAt | Unset = UNSET,
) -> ActionsListResultV3 | ErrorResponse | None:
    """ List Actions V3

     List actions for an organisation.

    Results are paginated and ordered by action ID, oldest first. Use the <code>after</code>
    value from <code>pagination_meta</code> to fetch the next page; it is only set when there
    may be more results.

    ### By created_at and updated_at

    Both timestamp filters accept the operators "gte" (greater than or equal to), "lte" (less
    than or equal to) and "date_range" (between two dates). The following example finds all
    actions updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    To find actions created within a specific date range, use the date_range operator with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v3/actions' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    Filtering on updated_at is useful for incrementally syncing actions: poll with
    updated_at[gte] set to your last sync time instead of re-fetching the full history. Two
    caveats: updated_at moves whenever the action row itself is written, but changes to
    embedded objects (e.g. an assignee being renamed) can alter the payload without bumping
    it. And timestamps are stamped before commit, so an action can become visible with an
    older updated_at than rows you have already seen — overlap your sync window by a few
    minutes to allow for writes that commit out of timestamp order.

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An action's ID. This endpoint will return a list of actions after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV3ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.
        created_at (ActionsV3ListCreatedAt | Unset): Filter on action created at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (ActionsV3ListUpdatedAt | Unset): Filter on action updated at timestamp.
            Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsListResultV3 | ErrorResponse
     """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            incident_id=incident_id,
            incident_mode=incident_mode,
            created_at=created_at,
            updated_at=updated_at,
        )
    ).parsed
