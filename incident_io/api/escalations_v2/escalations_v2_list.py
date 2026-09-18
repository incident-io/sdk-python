from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.escalations_list_result_v2 import EscalationsListResultV2
from ...models.escalations_v2_list_alert import EscalationsV2ListAlert
from ...models.escalations_v2_list_created_at import EscalationsV2ListCreatedAt
from ...models.escalations_v2_list_escalation_path import (
    EscalationsV2ListEscalationPath,
)
from ...models.escalations_v2_list_idempotency_key import (
    EscalationsV2ListIdempotencyKey,
)
from ...models.escalations_v2_list_incident import EscalationsV2ListIncident
from ...models.escalations_v2_list_status import EscalationsV2ListStatus
from ...models.escalations_v2_list_updated_at import EscalationsV2ListUpdatedAt
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    escalation_path: EscalationsV2ListEscalationPath | Unset = UNSET,
    status: EscalationsV2ListStatus | Unset = UNSET,
    alert: EscalationsV2ListAlert | Unset = UNSET,
    incident: EscalationsV2ListIncident | Unset = UNSET,
    created_at: EscalationsV2ListCreatedAt | Unset = UNSET,
    updated_at: EscalationsV2ListUpdatedAt | Unset = UNSET,
    idempotency_key: EscalationsV2ListIdempotencyKey | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_escalation_path: dict[str, Any] | Unset = UNSET
    if not isinstance(escalation_path, Unset):
        json_escalation_path = escalation_path.to_dict()
    if not isinstance(json_escalation_path, Unset):
        params.update(json_escalation_path)

    json_status: dict[str, Any] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.to_dict()
    if not isinstance(json_status, Unset):
        params.update(json_status)

    json_alert: dict[str, Any] | Unset = UNSET
    if not isinstance(alert, Unset):
        json_alert = alert.to_dict()
    if not isinstance(json_alert, Unset):
        params.update(json_alert)

    json_incident: dict[str, Any] | Unset = UNSET
    if not isinstance(incident, Unset):
        json_incident = incident.to_dict()
    if not isinstance(json_incident, Unset):
        params.update(json_incident)

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

    json_idempotency_key: dict[str, Any] | Unset = UNSET
    if not isinstance(idempotency_key, Unset):
        json_idempotency_key = idempotency_key.to_dict()
    if not isinstance(json_idempotency_key, Unset):
        params.update(json_idempotency_key)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/escalations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EscalationsListResultV2 | None:
    if response.status_code == 200:
        response_200 = EscalationsListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | EscalationsListResultV2]:
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
    escalation_path: EscalationsV2ListEscalationPath | Unset = UNSET,
    status: EscalationsV2ListStatus | Unset = UNSET,
    alert: EscalationsV2ListAlert | Unset = UNSET,
    incident: EscalationsV2ListIncident | Unset = UNSET,
    created_at: EscalationsV2ListCreatedAt | Unset = UNSET,
    updated_at: EscalationsV2ListUpdatedAt | Unset = UNSET,
    idempotency_key: EscalationsV2ListIdempotencyKey | Unset = UNSET,
) -> Response[ErrorResponse | EscalationsListResultV2]:
    """ List Escalations V2

     List all escalations for your account.

    This endpoint supports a number of filters, which can help find escalations matching certain
    criteria.

    Note that:
    - Filters may be used together, and the result will be escalations that match all filters.
    - All query parameters must be URI encoded.

    To use this API, you will need an API key with the "View data" or "Create and manage on-call
    resources" permission.

    ### By escalation_path

    Find all escalations that escalated to escalation path with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'escalation_path[one_of]=ABC'

    ### By status

    Find all escalations with a current status of "triggered":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'status[one_of]=triggered'

    Possible values are "pending", "triggered", "acked", "resolved", "expired" and "cancelled".
    Escalations are in "pending" when they are in a grace period when the related alert has
    been grouped in an incident.

    ### By alert

    Find all escalations that were created by alert with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'alert[one_of]=ABC'

    ### By incident

    Find all escalations related to incident with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[one_of]=ABC'

    An escalation is related to an incident if it is linked to that incident directly, if it is
    attached to one of the incident's alerts, or if it triggered one of those alerts (which is
    what happens when someone pages by calling in, and that call raises the alert).

    To find everything that is not related to an incident, use "not_in":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[not_in]=ABC'

    ### By created_at and updated_at
    Find all escalations that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates).
    For example, to find all escalations updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'updated_at[gte]=2025-01-01'

    To find all escalations created between 2025-01-01 and 2025-01-31:

    		curl --get 'https://api.incident.io/v2/escalations' \\
                --data 'created_at[date_range]=2025-01-01~2025-01-31'

    Args:
        page_size (int | Unset): Number of escalations to return per page Default: 25. Example:
            25.
        after (str | Unset): An escalation's ID. This endpoint will return a list of escalations
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        escalation_path (EscalationsV2ListEscalationPath | Unset): Filter on the escalation path
            for which the escalation was triggered. Accepted operators are 'one_of' and 'not_in'.
            Example: {'one_of': ['01J479052SSQAA4531ASFPR3BF']}.
        status (EscalationsV2ListStatus | Unset): Filter on the status of the escalation. Accepted
            operators are 'one_of' and 'not_in'. Example: {'one_of': ['triggered']}.
        alert (EscalationsV2ListAlert | Unset): Filter on the alert that created an escalation.
            Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        incident (EscalationsV2ListIncident | Unset): Filter on the incident that the escalation
            is connected to. Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        created_at (EscalationsV2ListCreatedAt | Unset): Filter on the created_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        updated_at (EscalationsV2ListUpdatedAt | Unset): Filter on the updated_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        idempotency_key (EscalationsV2ListIdempotencyKey | Unset): Filter on the idempotency key
            of the escalation. This is the key set when creating escalations via the API, and is
            distinct from alert deduplication keys. Accepted operators are 'is' for exact matches and
            'starts_with' for prefix matching. Example: {'starts_with': ['team-a:']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsListResultV2]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        escalation_path=escalation_path,
        status=status,
        alert=alert,
        incident=incident,
        created_at=created_at,
        updated_at=updated_at,
        idempotency_key=idempotency_key,
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
    escalation_path: EscalationsV2ListEscalationPath | Unset = UNSET,
    status: EscalationsV2ListStatus | Unset = UNSET,
    alert: EscalationsV2ListAlert | Unset = UNSET,
    incident: EscalationsV2ListIncident | Unset = UNSET,
    created_at: EscalationsV2ListCreatedAt | Unset = UNSET,
    updated_at: EscalationsV2ListUpdatedAt | Unset = UNSET,
    idempotency_key: EscalationsV2ListIdempotencyKey | Unset = UNSET,
) -> ErrorResponse | EscalationsListResultV2 | None:
    """ List Escalations V2

     List all escalations for your account.

    This endpoint supports a number of filters, which can help find escalations matching certain
    criteria.

    Note that:
    - Filters may be used together, and the result will be escalations that match all filters.
    - All query parameters must be URI encoded.

    To use this API, you will need an API key with the "View data" or "Create and manage on-call
    resources" permission.

    ### By escalation_path

    Find all escalations that escalated to escalation path with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'escalation_path[one_of]=ABC'

    ### By status

    Find all escalations with a current status of "triggered":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'status[one_of]=triggered'

    Possible values are "pending", "triggered", "acked", "resolved", "expired" and "cancelled".
    Escalations are in "pending" when they are in a grace period when the related alert has
    been grouped in an incident.

    ### By alert

    Find all escalations that were created by alert with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'alert[one_of]=ABC'

    ### By incident

    Find all escalations related to incident with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[one_of]=ABC'

    An escalation is related to an incident if it is linked to that incident directly, if it is
    attached to one of the incident's alerts, or if it triggered one of those alerts (which is
    what happens when someone pages by calling in, and that call raises the alert).

    To find everything that is not related to an incident, use "not_in":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[not_in]=ABC'

    ### By created_at and updated_at
    Find all escalations that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates).
    For example, to find all escalations updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'updated_at[gte]=2025-01-01'

    To find all escalations created between 2025-01-01 and 2025-01-31:

    		curl --get 'https://api.incident.io/v2/escalations' \\
                --data 'created_at[date_range]=2025-01-01~2025-01-31'

    Args:
        page_size (int | Unset): Number of escalations to return per page Default: 25. Example:
            25.
        after (str | Unset): An escalation's ID. This endpoint will return a list of escalations
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        escalation_path (EscalationsV2ListEscalationPath | Unset): Filter on the escalation path
            for which the escalation was triggered. Accepted operators are 'one_of' and 'not_in'.
            Example: {'one_of': ['01J479052SSQAA4531ASFPR3BF']}.
        status (EscalationsV2ListStatus | Unset): Filter on the status of the escalation. Accepted
            operators are 'one_of' and 'not_in'. Example: {'one_of': ['triggered']}.
        alert (EscalationsV2ListAlert | Unset): Filter on the alert that created an escalation.
            Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        incident (EscalationsV2ListIncident | Unset): Filter on the incident that the escalation
            is connected to. Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        created_at (EscalationsV2ListCreatedAt | Unset): Filter on the created_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        updated_at (EscalationsV2ListUpdatedAt | Unset): Filter on the updated_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        idempotency_key (EscalationsV2ListIdempotencyKey | Unset): Filter on the idempotency key
            of the escalation. This is the key set when creating escalations via the API, and is
            distinct from alert deduplication keys. Accepted operators are 'is' for exact matches and
            'starts_with' for prefix matching. Example: {'starts_with': ['team-a:']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsListResultV2
     """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        escalation_path=escalation_path,
        status=status,
        alert=alert,
        incident=incident,
        created_at=created_at,
        updated_at=updated_at,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    escalation_path: EscalationsV2ListEscalationPath | Unset = UNSET,
    status: EscalationsV2ListStatus | Unset = UNSET,
    alert: EscalationsV2ListAlert | Unset = UNSET,
    incident: EscalationsV2ListIncident | Unset = UNSET,
    created_at: EscalationsV2ListCreatedAt | Unset = UNSET,
    updated_at: EscalationsV2ListUpdatedAt | Unset = UNSET,
    idempotency_key: EscalationsV2ListIdempotencyKey | Unset = UNSET,
) -> Response[ErrorResponse | EscalationsListResultV2]:
    """ List Escalations V2

     List all escalations for your account.

    This endpoint supports a number of filters, which can help find escalations matching certain
    criteria.

    Note that:
    - Filters may be used together, and the result will be escalations that match all filters.
    - All query parameters must be URI encoded.

    To use this API, you will need an API key with the "View data" or "Create and manage on-call
    resources" permission.

    ### By escalation_path

    Find all escalations that escalated to escalation path with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'escalation_path[one_of]=ABC'

    ### By status

    Find all escalations with a current status of "triggered":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'status[one_of]=triggered'

    Possible values are "pending", "triggered", "acked", "resolved", "expired" and "cancelled".
    Escalations are in "pending" when they are in a grace period when the related alert has
    been grouped in an incident.

    ### By alert

    Find all escalations that were created by alert with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'alert[one_of]=ABC'

    ### By incident

    Find all escalations related to incident with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[one_of]=ABC'

    An escalation is related to an incident if it is linked to that incident directly, if it is
    attached to one of the incident's alerts, or if it triggered one of those alerts (which is
    what happens when someone pages by calling in, and that call raises the alert).

    To find everything that is not related to an incident, use "not_in":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[not_in]=ABC'

    ### By created_at and updated_at
    Find all escalations that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates).
    For example, to find all escalations updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'updated_at[gte]=2025-01-01'

    To find all escalations created between 2025-01-01 and 2025-01-31:

    		curl --get 'https://api.incident.io/v2/escalations' \\
                --data 'created_at[date_range]=2025-01-01~2025-01-31'

    Args:
        page_size (int | Unset): Number of escalations to return per page Default: 25. Example:
            25.
        after (str | Unset): An escalation's ID. This endpoint will return a list of escalations
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        escalation_path (EscalationsV2ListEscalationPath | Unset): Filter on the escalation path
            for which the escalation was triggered. Accepted operators are 'one_of' and 'not_in'.
            Example: {'one_of': ['01J479052SSQAA4531ASFPR3BF']}.
        status (EscalationsV2ListStatus | Unset): Filter on the status of the escalation. Accepted
            operators are 'one_of' and 'not_in'. Example: {'one_of': ['triggered']}.
        alert (EscalationsV2ListAlert | Unset): Filter on the alert that created an escalation.
            Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        incident (EscalationsV2ListIncident | Unset): Filter on the incident that the escalation
            is connected to. Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        created_at (EscalationsV2ListCreatedAt | Unset): Filter on the created_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        updated_at (EscalationsV2ListUpdatedAt | Unset): Filter on the updated_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        idempotency_key (EscalationsV2ListIdempotencyKey | Unset): Filter on the idempotency key
            of the escalation. This is the key set when creating escalations via the API, and is
            distinct from alert deduplication keys. Accepted operators are 'is' for exact matches and
            'starts_with' for prefix matching. Example: {'starts_with': ['team-a:']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | EscalationsListResultV2]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        escalation_path=escalation_path,
        status=status,
        alert=alert,
        incident=incident,
        created_at=created_at,
        updated_at=updated_at,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    escalation_path: EscalationsV2ListEscalationPath | Unset = UNSET,
    status: EscalationsV2ListStatus | Unset = UNSET,
    alert: EscalationsV2ListAlert | Unset = UNSET,
    incident: EscalationsV2ListIncident | Unset = UNSET,
    created_at: EscalationsV2ListCreatedAt | Unset = UNSET,
    updated_at: EscalationsV2ListUpdatedAt | Unset = UNSET,
    idempotency_key: EscalationsV2ListIdempotencyKey | Unset = UNSET,
) -> ErrorResponse | EscalationsListResultV2 | None:
    """ List Escalations V2

     List all escalations for your account.

    This endpoint supports a number of filters, which can help find escalations matching certain
    criteria.

    Note that:
    - Filters may be used together, and the result will be escalations that match all filters.
    - All query parameters must be URI encoded.

    To use this API, you will need an API key with the "View data" or "Create and manage on-call
    resources" permission.

    ### By escalation_path

    Find all escalations that escalated to escalation path with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'escalation_path[one_of]=ABC'

    ### By status

    Find all escalations with a current status of "triggered":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'status[one_of]=triggered'

    Possible values are "pending", "triggered", "acked", "resolved", "expired" and "cancelled".
    Escalations are in "pending" when they are in a grace period when the related alert has
    been grouped in an incident.

    ### By alert

    Find all escalations that were created by alert with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'alert[one_of]=ABC'

    ### By incident

    Find all escalations related to incident with id=ABC:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[one_of]=ABC'

    An escalation is related to an incident if it is linked to that incident directly, if it is
    attached to one of the incident's alerts, or if it triggered one of those alerts (which is
    what happens when someone pages by calling in, and that call raises the alert).

    To find everything that is not related to an incident, use "not_in":

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'incident[not_in]=ABC'

    ### By created_at and updated_at
    Find all escalations that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates).
    For example, to find all escalations updated after 2025-01-01:

    		curl --get 'https://api.incident.io/v2/escalations' \\
    			--data 'updated_at[gte]=2025-01-01'

    To find all escalations created between 2025-01-01 and 2025-01-31:

    		curl --get 'https://api.incident.io/v2/escalations' \\
                --data 'created_at[date_range]=2025-01-01~2025-01-31'

    Args:
        page_size (int | Unset): Number of escalations to return per page Default: 25. Example:
            25.
        after (str | Unset): An escalation's ID. This endpoint will return a list of escalations
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        escalation_path (EscalationsV2ListEscalationPath | Unset): Filter on the escalation path
            for which the escalation was triggered. Accepted operators are 'one_of' and 'not_in'.
            Example: {'one_of': ['01J479052SSQAA4531ASFPR3BF']}.
        status (EscalationsV2ListStatus | Unset): Filter on the status of the escalation. Accepted
            operators are 'one_of' and 'not_in'. Example: {'one_of': ['triggered']}.
        alert (EscalationsV2ListAlert | Unset): Filter on the alert that created an escalation.
            Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        incident (EscalationsV2ListIncident | Unset): Filter on the incident that the escalation
            is connected to. Accepted operators are 'one_of' and 'not_in'. Example: {'one_of':
            ['01J479052SSQAA4531ASFPR3BF']}.
        created_at (EscalationsV2ListCreatedAt | Unset): Filter on the created_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        updated_at (EscalationsV2ListUpdatedAt | Unset): Filter on the updated_at timestamp of the
            escalation. Accepted operators are 'gte', 'lte' and 'date_range'. Example: {'gte':
            ['2021-08-17']}.
        idempotency_key (EscalationsV2ListIdempotencyKey | Unset): Filter on the idempotency key
            of the escalation. This is the key set when creating escalations via the API, and is
            distinct from alert deduplication keys. Accepted operators are 'is' for exact matches and
            'starts_with' for prefix matching. Example: {'starts_with': ['team-a:']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | EscalationsListResultV2
     """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            escalation_path=escalation_path,
            status=status,
            alert=alert,
            incident=incident,
            created_at=created_at,
            updated_at=updated_at,
            idempotency_key=idempotency_key,
        )
    ).parsed
