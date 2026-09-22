from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ..._query import flatten_deep_object
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.workflow_runs_list_result_v2 import WorkflowRunsListResultV2
from ...models.workflow_runs_v2_list_created_at import WorkflowRunsV2ListCreatedAt
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workflow_id: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    created_at: WorkflowRunsV2ListCreatedAt | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workflow_id"] = workflow_id

    params["incident_id"] = incident_id

    json_created_at: dict[str, Any] | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.to_dict()
    if not isinstance(json_created_at, Unset):
        params.update(flatten_deep_object("created_at", json_created_at))

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/workflow_runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WorkflowRunsListResultV2 | None:
    if response.status_code == 200:
        response_200 = WorkflowRunsListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | WorkflowRunsListResultV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    created_at: WorkflowRunsV2ListCreatedAt | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | WorkflowRunsListResultV2]:
    """List WorkflowRuns V2

     List workflow runs, newest first. Cancelled runs are never returned.

    The webhook delivery on each step omits the headers and bodies. Fetch a single run to see them.

    You can filter on when a run was created:

    ```
    # Runs created on or after a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[gte]=2026-07-01'

    # Runs created on or before a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[lte]=2026-07-31'

    # Runs created between two dates
    curl 'https://api.incident.io/v2/workflow_runs?created_at[date_range]=2026-07-01~2026-07-31'
    ```

    Paginate by passing the last run's ID as `after`. The response's
    `pagination_meta.after` carries the value to send next, and is absent on the last page.
    An `after` that isn't a run in your organisation returns 404.

    Args:
        workflow_id (str | Unset): Unique identifier for the workflow to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str | Unset): Unique identifier for the incident to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (WorkflowRunsV2ListCreatedAt | Unset): Filter on workflow run created at
            timestamp. The accepted operators are 'gte', 'lte' and 'date_range'. Example:
            {'date_range': ['2026-07-01~2026-07-31']}.
        page_size (int | Unset): Number of workflow runs to return per page Default: 25. Example:
            25.
        after (str | Unset): A workflow run's ID. This endpoint will return a list of workflow
            runs after this ID in relation to the API response order. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowRunsListResultV2]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        incident_id=incident_id,
        created_at=created_at,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    created_at: WorkflowRunsV2ListCreatedAt | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | WorkflowRunsListResultV2 | None:
    """List WorkflowRuns V2

     List workflow runs, newest first. Cancelled runs are never returned.

    The webhook delivery on each step omits the headers and bodies. Fetch a single run to see them.

    You can filter on when a run was created:

    ```
    # Runs created on or after a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[gte]=2026-07-01'

    # Runs created on or before a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[lte]=2026-07-31'

    # Runs created between two dates
    curl 'https://api.incident.io/v2/workflow_runs?created_at[date_range]=2026-07-01~2026-07-31'
    ```

    Paginate by passing the last run's ID as `after`. The response's
    `pagination_meta.after` carries the value to send next, and is absent on the last page.
    An `after` that isn't a run in your organisation returns 404.

    Args:
        workflow_id (str | Unset): Unique identifier for the workflow to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str | Unset): Unique identifier for the incident to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (WorkflowRunsV2ListCreatedAt | Unset): Filter on workflow run created at
            timestamp. The accepted operators are 'gte', 'lte' and 'date_range'. Example:
            {'date_range': ['2026-07-01~2026-07-31']}.
        page_size (int | Unset): Number of workflow runs to return per page Default: 25. Example:
            25.
        after (str | Unset): A workflow run's ID. This endpoint will return a list of workflow
            runs after this ID in relation to the API response order. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowRunsListResultV2
    """

    return sync_detailed(
        client=client,
        workflow_id=workflow_id,
        incident_id=incident_id,
        created_at=created_at,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    created_at: WorkflowRunsV2ListCreatedAt | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> Response[ErrorResponse | WorkflowRunsListResultV2]:
    """List WorkflowRuns V2

     List workflow runs, newest first. Cancelled runs are never returned.

    The webhook delivery on each step omits the headers and bodies. Fetch a single run to see them.

    You can filter on when a run was created:

    ```
    # Runs created on or after a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[gte]=2026-07-01'

    # Runs created on or before a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[lte]=2026-07-31'

    # Runs created between two dates
    curl 'https://api.incident.io/v2/workflow_runs?created_at[date_range]=2026-07-01~2026-07-31'
    ```

    Paginate by passing the last run's ID as `after`. The response's
    `pagination_meta.after` carries the value to send next, and is absent on the last page.
    An `after` that isn't a run in your organisation returns 404.

    Args:
        workflow_id (str | Unset): Unique identifier for the workflow to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str | Unset): Unique identifier for the incident to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (WorkflowRunsV2ListCreatedAt | Unset): Filter on workflow run created at
            timestamp. The accepted operators are 'gte', 'lte' and 'date_range'. Example:
            {'date_range': ['2026-07-01~2026-07-31']}.
        page_size (int | Unset): Number of workflow runs to return per page Default: 25. Example:
            25.
        after (str | Unset): A workflow run's ID. This endpoint will return a list of workflow
            runs after this ID in relation to the API response order. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowRunsListResultV2]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        incident_id=incident_id,
        created_at=created_at,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    incident_id: str | Unset = UNSET,
    created_at: WorkflowRunsV2ListCreatedAt | Unset = UNSET,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
) -> ErrorResponse | WorkflowRunsListResultV2 | None:
    """List WorkflowRuns V2

     List workflow runs, newest first. Cancelled runs are never returned.

    The webhook delivery on each step omits the headers and bodies. Fetch a single run to see them.

    You can filter on when a run was created:

    ```
    # Runs created on or after a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[gte]=2026-07-01'

    # Runs created on or before a date
    curl 'https://api.incident.io/v2/workflow_runs?created_at[lte]=2026-07-31'

    # Runs created between two dates
    curl 'https://api.incident.io/v2/workflow_runs?created_at[date_range]=2026-07-01~2026-07-31'
    ```

    Paginate by passing the last run's ID as `after`. The response's
    `pagination_meta.after` carries the value to send next, and is absent on the last page.
    An `after` that isn't a run in your organisation returns 404.

    Args:
        workflow_id (str | Unset): Unique identifier for the workflow to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str | Unset): Unique identifier for the incident to filter by Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (WorkflowRunsV2ListCreatedAt | Unset): Filter on workflow run created at
            timestamp. The accepted operators are 'gte', 'lte' and 'date_range'. Example:
            {'date_range': ['2026-07-01~2026-07-31']}.
        page_size (int | Unset): Number of workflow runs to return per page Default: 25. Example:
            25.
        after (str | Unset): A workflow run's ID. This endpoint will return a list of workflow
            runs after this ID in relation to the API response order. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowRunsListResultV2
    """

    return (
        await asyncio_detailed(
            client=client,
            workflow_id=workflow_id,
            incident_id=incident_id,
            created_at=created_at,
            page_size=page_size,
            after=after,
        )
    ).parsed
