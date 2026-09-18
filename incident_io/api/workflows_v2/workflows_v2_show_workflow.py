from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.workflows_show_workflow_result_v2 import WorkflowsShowWorkflowResultV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    skip_step_upgrades: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["skip_step_upgrades"] = skip_step_upgrades

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/workflows/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WorkflowsShowWorkflowResultV2 | None:
    if response.status_code == 200:
        response_200 = WorkflowsShowWorkflowResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | WorkflowsShowWorkflowResultV2]:
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
    skip_step_upgrades: bool | Unset = UNSET,
) -> Response[ErrorResponse | WorkflowsShowWorkflowResultV2]:
    """ShowWorkflow Workflows V2

     Show a workflow by ID

    Args:
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        skip_step_upgrades (bool | Unset): Skips workflow step upgrades, when the parameters for
            an existing workflow step change Example: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowsShowWorkflowResultV2]
    """

    kwargs = _get_kwargs(
        id=id,
        skip_step_upgrades=skip_step_upgrades,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    skip_step_upgrades: bool | Unset = UNSET,
) -> ErrorResponse | WorkflowsShowWorkflowResultV2 | None:
    """ShowWorkflow Workflows V2

     Show a workflow by ID

    Args:
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        skip_step_upgrades (bool | Unset): Skips workflow step upgrades, when the parameters for
            an existing workflow step change Example: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowsShowWorkflowResultV2
    """

    return sync_detailed(
        id=id,
        client=client,
        skip_step_upgrades=skip_step_upgrades,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    skip_step_upgrades: bool | Unset = UNSET,
) -> Response[ErrorResponse | WorkflowsShowWorkflowResultV2]:
    """ShowWorkflow Workflows V2

     Show a workflow by ID

    Args:
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        skip_step_upgrades (bool | Unset): Skips workflow step upgrades, when the parameters for
            an existing workflow step change Example: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WorkflowsShowWorkflowResultV2]
    """

    kwargs = _get_kwargs(
        id=id,
        skip_step_upgrades=skip_step_upgrades,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    skip_step_upgrades: bool | Unset = UNSET,
) -> ErrorResponse | WorkflowsShowWorkflowResultV2 | None:
    """ShowWorkflow Workflows V2

     Show a workflow by ID

    Args:
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        skip_step_upgrades (bool | Unset): Skips workflow step upgrades, when the parameters for
            an existing workflow step change Example: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WorkflowsShowWorkflowResultV2
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            skip_step_upgrades=skip_step_upgrades,
        )
    ).parsed
