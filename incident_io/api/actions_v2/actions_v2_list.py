from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_list_result_v2 import ActionsListResultV2
from ...models.actions_v2_list_incident_mode import ActionsV2ListIncidentMode
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV2ListIncidentMode | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["incident_id"] = incident_id

    json_incident_mode: str | Unset = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value

    params["incident_mode"] = json_incident_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionsListResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ActionsListResultV2.from_dict(response.json())

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
) -> Response[ActionsListResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV2ListIncidentMode | Unset = UNSET,
) -> Response[ActionsListResultV2 | ErrorResponse]:
    """List Actions V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>GET /v3/actions</code>
    instead.

    List all actions for an organisation.

    Args:
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV2ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsListResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        incident_mode=incident_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV2ListIncidentMode | Unset = UNSET,
) -> ActionsListResultV2 | ErrorResponse | None:
    """List Actions V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>GET /v3/actions</code>
    instead.

    List all actions for an organisation.

    Args:
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV2ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsListResultV2 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV2ListIncidentMode | Unset = UNSET,
) -> Response[ActionsListResultV2 | ErrorResponse]:
    """List Actions V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>GET /v3/actions</code>
    instead.

    List all actions for an organisation.

    Args:
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV2ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsListResultV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        incident_mode=incident_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    incident_id: str | Unset = UNSET,
    incident_mode: ActionsV2ListIncidentMode | Unset = UNSET,
) -> ActionsListResultV2 | ErrorResponse | None:
    """List Actions V2

     Deprecated: this endpoint will be removed on 31 December 2026. Use <code>GET /v3/actions</code>
    instead.

    List all actions for an organisation.

    Args:
        incident_id (str | Unset):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (ActionsV2ListIncidentMode | Unset): Filter to actions from incidents of the
            given mode. If not set, only actions from `standard` and `retrospective` incidents are
            returned Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsListResultV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_mode=incident_mode,
        )
    ).parsed

# --- deprecation markers added by scripts/mark_deprecated.py ---
import functools as _functools
import warnings as _warnings


def _deprecated(_fn):
    @_functools.wraps(_fn)
    def _wrapper(*args, **kwargs):
        _warnings.warn(
            "GET /v2/actions is deprecated and will be removed. See https://api-docs.incident.io/ for the replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _fn(*args, **kwargs)

    return _wrapper

sync_detailed = _deprecated(sync_detailed)
sync = _deprecated(sync)
asyncio_detailed = _deprecated(asyncio_detailed)
asyncio = _deprecated(asyncio)
