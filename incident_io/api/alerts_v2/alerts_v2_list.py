from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ..._query import flatten_deep_object
from ...client import AuthenticatedClient, Client
from ...models.alerts_list_result_v2 import AlertsListResultV2
from ...models.alerts_v2_list_alert_group_id import AlertsV2ListAlertGroupId
from ...models.alerts_v2_list_alert_source import AlertsV2ListAlertSource
from ...models.alerts_v2_list_attributes import AlertsV2ListAttributes
from ...models.alerts_v2_list_created_at import AlertsV2ListCreatedAt
from ...models.alerts_v2_list_deduplication_key import AlertsV2ListDeduplicationKey
from ...models.alerts_v2_list_has_notes import AlertsV2ListHasNotes
from ...models.alerts_v2_list_include_maintenance_window import (
    AlertsV2ListIncludeMaintenanceWindow,
)
from ...models.alerts_v2_list_status import AlertsV2ListStatus
from ...models.alerts_v2_list_tags import AlertsV2ListTags
from ...models.alerts_v2_list_updated_at import AlertsV2ListUpdatedAt
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int = 25,
    after: str | Unset = UNSET,
    deduplication_key: AlertsV2ListDeduplicationKey | Unset = UNSET,
    status: AlertsV2ListStatus | Unset = UNSET,
    alert_source: AlertsV2ListAlertSource | Unset = UNSET,
    alert_group_id: AlertsV2ListAlertGroupId | Unset = UNSET,
    created_at: AlertsV2ListCreatedAt | Unset = UNSET,
    updated_at: AlertsV2ListUpdatedAt | Unset = UNSET,
    attributes: AlertsV2ListAttributes | Unset = UNSET,
    has_notes: AlertsV2ListHasNotes | Unset = UNSET,
    tags: AlertsV2ListTags | Unset = UNSET,
    include_maintenance_window: AlertsV2ListIncludeMaintenanceWindow | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_deduplication_key: dict[str, Any] | Unset = UNSET
    if not isinstance(deduplication_key, Unset):
        json_deduplication_key = deduplication_key.to_dict()
    if not isinstance(json_deduplication_key, Unset):
        params.update(flatten_deep_object("deduplication_key", json_deduplication_key))

    json_status: dict[str, Any] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.to_dict()
    if not isinstance(json_status, Unset):
        params.update(flatten_deep_object("status", json_status))

    json_alert_source: dict[str, Any] | Unset = UNSET
    if not isinstance(alert_source, Unset):
        json_alert_source = alert_source.to_dict()
    if not isinstance(json_alert_source, Unset):
        params.update(flatten_deep_object("alert_source", json_alert_source))

    json_alert_group_id: dict[str, Any] | Unset = UNSET
    if not isinstance(alert_group_id, Unset):
        json_alert_group_id = alert_group_id.to_dict()
    if not isinstance(json_alert_group_id, Unset):
        params.update(flatten_deep_object("alert_group_id", json_alert_group_id))

    json_created_at: dict[str, Any] | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.to_dict()
    if not isinstance(json_created_at, Unset):
        params.update(flatten_deep_object("created_at", json_created_at))

    json_updated_at: dict[str, Any] | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.to_dict()
    if not isinstance(json_updated_at, Unset):
        params.update(flatten_deep_object("updated_at", json_updated_at))

    json_attributes: dict[str, Any] | Unset = UNSET
    if not isinstance(attributes, Unset):
        json_attributes = attributes.to_dict()
    if not isinstance(json_attributes, Unset):
        params.update(flatten_deep_object("attributes", json_attributes))

    json_has_notes: dict[str, Any] | Unset = UNSET
    if not isinstance(has_notes, Unset):
        json_has_notes = has_notes.to_dict()
    if not isinstance(json_has_notes, Unset):
        params.update(flatten_deep_object("has_notes", json_has_notes))

    json_tags: dict[str, Any] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags.to_dict()
    if not isinstance(json_tags, Unset):
        params.update(flatten_deep_object("tags", json_tags))

    json_include_maintenance_window: dict[str, Any] | Unset = UNSET
    if not isinstance(include_maintenance_window, Unset):
        json_include_maintenance_window = include_maintenance_window.to_dict()
    if not isinstance(json_include_maintenance_window, Unset):
        params.update(
            flatten_deep_object(
                "include_maintenance_window", json_include_maintenance_window
            )
        )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertsListResultV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlertsListResultV2.from_dict(response.json())

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
) -> Response[AlertsListResultV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int = 25,
    after: str | Unset = UNSET,
    deduplication_key: AlertsV2ListDeduplicationKey | Unset = UNSET,
    status: AlertsV2ListStatus | Unset = UNSET,
    alert_source: AlertsV2ListAlertSource | Unset = UNSET,
    alert_group_id: AlertsV2ListAlertGroupId | Unset = UNSET,
    created_at: AlertsV2ListCreatedAt | Unset = UNSET,
    updated_at: AlertsV2ListUpdatedAt | Unset = UNSET,
    attributes: AlertsV2ListAttributes | Unset = UNSET,
    has_notes: AlertsV2ListHasNotes | Unset = UNSET,
    tags: AlertsV2ListTags | Unset = UNSET,
    include_maintenance_window: AlertsV2ListIncludeMaintenanceWindow | Unset = UNSET,
) -> Response[AlertsListResultV2 | ErrorResponse]:
    """ List Alerts V2

     List all alerts for your account.

    This endpoint supports a number of filters, which can help find alerts matching certain
    criteria. These filters work similarly to the filters on the incidents endpoint, where
    a field is specified alongside a comparison operator in the query string.

    Note that:
    - Filters may be used together, and the result will be alerts that match all filters.
    - All query parameters must be URI encoded.

    ### By deduplication_key

    Find all alerts with deduplication_key ABC:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'deduplication_key[is]=ABC'

    ### By status

    Find all alerts in a firing state:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'status[one_of]=firing'

    ### By alert_source

    Find all alerts from a specific alert source (by alert source ID):

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    Find all alerts not from a specific alert source:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[not_in]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By alert_group_id

    Find all alerts in a specific alert group:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_group_id[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By created_at
    Find all alerts that follow specified date parameters for created_at field.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all alerts created after
    2025-01-01:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[gte]=2025-01-01'

    To find alerts created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By updated_at
    Find all alerts that follow specified date parameters for updated_at field, using the same
    "gte", "lte" and "date_range" operators as created_at. This is useful for incrementally
    syncing alerts: poll with updated_at[gte] set to your last sync time instead of re-fetching
    the full history. Note that updated_at moves whenever the alert row is written, which can
    happen without a visible change to the alert payload, so treat matches as candidates to
    re-fetch rather than guaranteed changes — and overlap your sync window by a few minutes to
    allow for writes that commit out of timestamp order:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    ### By has_notes

    Find all alerts that have notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=true'

    Find all alerts that have no notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=false'

    ### By tags

    Filter by tag name, matched case-insensitively.

    Find all alerts that have any of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[one_of]=known issue'

    Find all alerts that have all of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[all_of]=known issue' \\
    			--data 'tags[all_of]=customer impacting'

    Find all alerts that do not have any of the given tags. Untagged alerts are included:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[not_in]=known issue'

    ### By attributes

    Alerts can be filtered by their attribute values. Each filter is keyed by the alert
    attribute ID, followed by an operator and the values to match. The accepted operators
    depend on the attribute's type.

    Find all alerts where attribute 01GBSQF3FHF7FWZQNWGHAVQ804 is one of two catalog entries:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01GBSQF3FHF7FWZQNWGHAVQ804' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01ET65M7ZARSFZ6TFDFVQDN9AA'

    You can filter on multiple attributes at once, and the result will be alerts that match
    all of them.

    ### Maintenance windows
    By default, all alerts are returned including those held by a maintenance window.
    To exclude alerts that are held by a maintenance window:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'include_maintenance_window[is]=false'


    Args:
        page_size (int): Number of alerts to return per page Default: 25. Example: 25.
        after (str | Unset): If provided, pass this as the 'after' param to load the next page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        deduplication_key (AlertsV2ListDeduplicationKey | Unset): Filter on alert deduplication
            key. The accepted operator is 'is'. Example: {'is': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status (AlertsV2ListStatus | Unset): Filter on alert status. The accepted operators are
            'one_of', or 'not_in'. Example: {'one_of': ['firing']}.
        alert_source (AlertsV2ListAlertSource | Unset): Filter on alert source by ID. The accepted
            operators are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        alert_group_id (AlertsV2ListAlertGroupId | Unset): Filter on alert group ID. Returns
            alerts that belong to any of the specified groups. The accepted operator is 'one_of'.
            Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        created_at (AlertsV2ListCreatedAt | Unset): Filter on alert created at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (AlertsV2ListUpdatedAt | Unset): Filter on alert updated at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        attributes (AlertsV2ListAttributes | Unset): Filter on an alerts attributes. Alert
            attribute ID should be sent, followed by the operator and values. Accepted operator will
            depend on the attribute type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        has_notes (AlertsV2ListHasNotes | Unset): Filter on whether an alert has notes. The
            accepted operator is 'is'. Example: {'is': ['true']}.
        tags (AlertsV2ListTags | Unset): Filter on the tags applied to an alert, by tag name. The
            accepted operators are 'one_of', 'all_of' and 'not_in'. Example: {'one_of': ['known
            issue']}.
        include_maintenance_window (AlertsV2ListIncludeMaintenanceWindow | Unset): Filter on
            whether to include maintenance window alerts. The accepted operator is 'is'. Example:
            {'is': ['true']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsListResultV2 | ErrorResponse]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        deduplication_key=deduplication_key,
        status=status,
        alert_source=alert_source,
        alert_group_id=alert_group_id,
        created_at=created_at,
        updated_at=updated_at,
        attributes=attributes,
        has_notes=has_notes,
        tags=tags,
        include_maintenance_window=include_maintenance_window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int = 25,
    after: str | Unset = UNSET,
    deduplication_key: AlertsV2ListDeduplicationKey | Unset = UNSET,
    status: AlertsV2ListStatus | Unset = UNSET,
    alert_source: AlertsV2ListAlertSource | Unset = UNSET,
    alert_group_id: AlertsV2ListAlertGroupId | Unset = UNSET,
    created_at: AlertsV2ListCreatedAt | Unset = UNSET,
    updated_at: AlertsV2ListUpdatedAt | Unset = UNSET,
    attributes: AlertsV2ListAttributes | Unset = UNSET,
    has_notes: AlertsV2ListHasNotes | Unset = UNSET,
    tags: AlertsV2ListTags | Unset = UNSET,
    include_maintenance_window: AlertsV2ListIncludeMaintenanceWindow | Unset = UNSET,
) -> AlertsListResultV2 | ErrorResponse | None:
    """ List Alerts V2

     List all alerts for your account.

    This endpoint supports a number of filters, which can help find alerts matching certain
    criteria. These filters work similarly to the filters on the incidents endpoint, where
    a field is specified alongside a comparison operator in the query string.

    Note that:
    - Filters may be used together, and the result will be alerts that match all filters.
    - All query parameters must be URI encoded.

    ### By deduplication_key

    Find all alerts with deduplication_key ABC:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'deduplication_key[is]=ABC'

    ### By status

    Find all alerts in a firing state:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'status[one_of]=firing'

    ### By alert_source

    Find all alerts from a specific alert source (by alert source ID):

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    Find all alerts not from a specific alert source:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[not_in]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By alert_group_id

    Find all alerts in a specific alert group:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_group_id[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By created_at
    Find all alerts that follow specified date parameters for created_at field.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all alerts created after
    2025-01-01:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[gte]=2025-01-01'

    To find alerts created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By updated_at
    Find all alerts that follow specified date parameters for updated_at field, using the same
    "gte", "lte" and "date_range" operators as created_at. This is useful for incrementally
    syncing alerts: poll with updated_at[gte] set to your last sync time instead of re-fetching
    the full history. Note that updated_at moves whenever the alert row is written, which can
    happen without a visible change to the alert payload, so treat matches as candidates to
    re-fetch rather than guaranteed changes — and overlap your sync window by a few minutes to
    allow for writes that commit out of timestamp order:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    ### By has_notes

    Find all alerts that have notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=true'

    Find all alerts that have no notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=false'

    ### By tags

    Filter by tag name, matched case-insensitively.

    Find all alerts that have any of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[one_of]=known issue'

    Find all alerts that have all of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[all_of]=known issue' \\
    			--data 'tags[all_of]=customer impacting'

    Find all alerts that do not have any of the given tags. Untagged alerts are included:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[not_in]=known issue'

    ### By attributes

    Alerts can be filtered by their attribute values. Each filter is keyed by the alert
    attribute ID, followed by an operator and the values to match. The accepted operators
    depend on the attribute's type.

    Find all alerts where attribute 01GBSQF3FHF7FWZQNWGHAVQ804 is one of two catalog entries:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01GBSQF3FHF7FWZQNWGHAVQ804' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01ET65M7ZARSFZ6TFDFVQDN9AA'

    You can filter on multiple attributes at once, and the result will be alerts that match
    all of them.

    ### Maintenance windows
    By default, all alerts are returned including those held by a maintenance window.
    To exclude alerts that are held by a maintenance window:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'include_maintenance_window[is]=false'


    Args:
        page_size (int): Number of alerts to return per page Default: 25. Example: 25.
        after (str | Unset): If provided, pass this as the 'after' param to load the next page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        deduplication_key (AlertsV2ListDeduplicationKey | Unset): Filter on alert deduplication
            key. The accepted operator is 'is'. Example: {'is': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status (AlertsV2ListStatus | Unset): Filter on alert status. The accepted operators are
            'one_of', or 'not_in'. Example: {'one_of': ['firing']}.
        alert_source (AlertsV2ListAlertSource | Unset): Filter on alert source by ID. The accepted
            operators are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        alert_group_id (AlertsV2ListAlertGroupId | Unset): Filter on alert group ID. Returns
            alerts that belong to any of the specified groups. The accepted operator is 'one_of'.
            Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        created_at (AlertsV2ListCreatedAt | Unset): Filter on alert created at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (AlertsV2ListUpdatedAt | Unset): Filter on alert updated at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        attributes (AlertsV2ListAttributes | Unset): Filter on an alerts attributes. Alert
            attribute ID should be sent, followed by the operator and values. Accepted operator will
            depend on the attribute type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        has_notes (AlertsV2ListHasNotes | Unset): Filter on whether an alert has notes. The
            accepted operator is 'is'. Example: {'is': ['true']}.
        tags (AlertsV2ListTags | Unset): Filter on the tags applied to an alert, by tag name. The
            accepted operators are 'one_of', 'all_of' and 'not_in'. Example: {'one_of': ['known
            issue']}.
        include_maintenance_window (AlertsV2ListIncludeMaintenanceWindow | Unset): Filter on
            whether to include maintenance window alerts. The accepted operator is 'is'. Example:
            {'is': ['true']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsListResultV2 | ErrorResponse
     """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        deduplication_key=deduplication_key,
        status=status,
        alert_source=alert_source,
        alert_group_id=alert_group_id,
        created_at=created_at,
        updated_at=updated_at,
        attributes=attributes,
        has_notes=has_notes,
        tags=tags,
        include_maintenance_window=include_maintenance_window,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int = 25,
    after: str | Unset = UNSET,
    deduplication_key: AlertsV2ListDeduplicationKey | Unset = UNSET,
    status: AlertsV2ListStatus | Unset = UNSET,
    alert_source: AlertsV2ListAlertSource | Unset = UNSET,
    alert_group_id: AlertsV2ListAlertGroupId | Unset = UNSET,
    created_at: AlertsV2ListCreatedAt | Unset = UNSET,
    updated_at: AlertsV2ListUpdatedAt | Unset = UNSET,
    attributes: AlertsV2ListAttributes | Unset = UNSET,
    has_notes: AlertsV2ListHasNotes | Unset = UNSET,
    tags: AlertsV2ListTags | Unset = UNSET,
    include_maintenance_window: AlertsV2ListIncludeMaintenanceWindow | Unset = UNSET,
) -> Response[AlertsListResultV2 | ErrorResponse]:
    """ List Alerts V2

     List all alerts for your account.

    This endpoint supports a number of filters, which can help find alerts matching certain
    criteria. These filters work similarly to the filters on the incidents endpoint, where
    a field is specified alongside a comparison operator in the query string.

    Note that:
    - Filters may be used together, and the result will be alerts that match all filters.
    - All query parameters must be URI encoded.

    ### By deduplication_key

    Find all alerts with deduplication_key ABC:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'deduplication_key[is]=ABC'

    ### By status

    Find all alerts in a firing state:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'status[one_of]=firing'

    ### By alert_source

    Find all alerts from a specific alert source (by alert source ID):

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    Find all alerts not from a specific alert source:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[not_in]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By alert_group_id

    Find all alerts in a specific alert group:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_group_id[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By created_at
    Find all alerts that follow specified date parameters for created_at field.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all alerts created after
    2025-01-01:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[gte]=2025-01-01'

    To find alerts created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By updated_at
    Find all alerts that follow specified date parameters for updated_at field, using the same
    "gte", "lte" and "date_range" operators as created_at. This is useful for incrementally
    syncing alerts: poll with updated_at[gte] set to your last sync time instead of re-fetching
    the full history. Note that updated_at moves whenever the alert row is written, which can
    happen without a visible change to the alert payload, so treat matches as candidates to
    re-fetch rather than guaranteed changes — and overlap your sync window by a few minutes to
    allow for writes that commit out of timestamp order:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    ### By has_notes

    Find all alerts that have notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=true'

    Find all alerts that have no notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=false'

    ### By tags

    Filter by tag name, matched case-insensitively.

    Find all alerts that have any of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[one_of]=known issue'

    Find all alerts that have all of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[all_of]=known issue' \\
    			--data 'tags[all_of]=customer impacting'

    Find all alerts that do not have any of the given tags. Untagged alerts are included:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[not_in]=known issue'

    ### By attributes

    Alerts can be filtered by their attribute values. Each filter is keyed by the alert
    attribute ID, followed by an operator and the values to match. The accepted operators
    depend on the attribute's type.

    Find all alerts where attribute 01GBSQF3FHF7FWZQNWGHAVQ804 is one of two catalog entries:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01GBSQF3FHF7FWZQNWGHAVQ804' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01ET65M7ZARSFZ6TFDFVQDN9AA'

    You can filter on multiple attributes at once, and the result will be alerts that match
    all of them.

    ### Maintenance windows
    By default, all alerts are returned including those held by a maintenance window.
    To exclude alerts that are held by a maintenance window:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'include_maintenance_window[is]=false'


    Args:
        page_size (int): Number of alerts to return per page Default: 25. Example: 25.
        after (str | Unset): If provided, pass this as the 'after' param to load the next page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        deduplication_key (AlertsV2ListDeduplicationKey | Unset): Filter on alert deduplication
            key. The accepted operator is 'is'. Example: {'is': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status (AlertsV2ListStatus | Unset): Filter on alert status. The accepted operators are
            'one_of', or 'not_in'. Example: {'one_of': ['firing']}.
        alert_source (AlertsV2ListAlertSource | Unset): Filter on alert source by ID. The accepted
            operators are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        alert_group_id (AlertsV2ListAlertGroupId | Unset): Filter on alert group ID. Returns
            alerts that belong to any of the specified groups. The accepted operator is 'one_of'.
            Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        created_at (AlertsV2ListCreatedAt | Unset): Filter on alert created at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (AlertsV2ListUpdatedAt | Unset): Filter on alert updated at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        attributes (AlertsV2ListAttributes | Unset): Filter on an alerts attributes. Alert
            attribute ID should be sent, followed by the operator and values. Accepted operator will
            depend on the attribute type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        has_notes (AlertsV2ListHasNotes | Unset): Filter on whether an alert has notes. The
            accepted operator is 'is'. Example: {'is': ['true']}.
        tags (AlertsV2ListTags | Unset): Filter on the tags applied to an alert, by tag name. The
            accepted operators are 'one_of', 'all_of' and 'not_in'. Example: {'one_of': ['known
            issue']}.
        include_maintenance_window (AlertsV2ListIncludeMaintenanceWindow | Unset): Filter on
            whether to include maintenance window alerts. The accepted operator is 'is'. Example:
            {'is': ['true']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsListResultV2 | ErrorResponse]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        deduplication_key=deduplication_key,
        status=status,
        alert_source=alert_source,
        alert_group_id=alert_group_id,
        created_at=created_at,
        updated_at=updated_at,
        attributes=attributes,
        has_notes=has_notes,
        tags=tags,
        include_maintenance_window=include_maintenance_window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int = 25,
    after: str | Unset = UNSET,
    deduplication_key: AlertsV2ListDeduplicationKey | Unset = UNSET,
    status: AlertsV2ListStatus | Unset = UNSET,
    alert_source: AlertsV2ListAlertSource | Unset = UNSET,
    alert_group_id: AlertsV2ListAlertGroupId | Unset = UNSET,
    created_at: AlertsV2ListCreatedAt | Unset = UNSET,
    updated_at: AlertsV2ListUpdatedAt | Unset = UNSET,
    attributes: AlertsV2ListAttributes | Unset = UNSET,
    has_notes: AlertsV2ListHasNotes | Unset = UNSET,
    tags: AlertsV2ListTags | Unset = UNSET,
    include_maintenance_window: AlertsV2ListIncludeMaintenanceWindow | Unset = UNSET,
) -> AlertsListResultV2 | ErrorResponse | None:
    """ List Alerts V2

     List all alerts for your account.

    This endpoint supports a number of filters, which can help find alerts matching certain
    criteria. These filters work similarly to the filters on the incidents endpoint, where
    a field is specified alongside a comparison operator in the query string.

    Note that:
    - Filters may be used together, and the result will be alerts that match all filters.
    - All query parameters must be URI encoded.

    ### By deduplication_key

    Find all alerts with deduplication_key ABC:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'deduplication_key[is]=ABC'

    ### By status

    Find all alerts in a firing state:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'status[one_of]=firing'

    ### By alert_source

    Find all alerts from a specific alert source (by alert source ID):

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    Find all alerts not from a specific alert source:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_source[not_in]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By alert_group_id

    Find all alerts in a specific alert group:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'alert_group_id[one_of]=01GBSQF3FHF7FWZQNWGHAVQ804'

    ### By created_at
    Find all alerts that follow specified date parameters for created_at field.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all alerts created after
    2025-01-01:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[gte]=2025-01-01'

    To find alerts created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By updated_at
    Find all alerts that follow specified date parameters for updated_at field, using the same
    "gte", "lte" and "date_range" operators as created_at. This is useful for incrementally
    syncing alerts: poll with updated_at[gte] set to your last sync time instead of re-fetching
    the full history. Note that updated_at moves whenever the alert row is written, which can
    happen without a visible change to the alert payload, so treat matches as candidates to
    re-fetch rather than guaranteed changes — and overlap your sync window by a few minutes to
    allow for writes that commit out of timestamp order:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'updated_at[gte]=2025-01-01T00:00:00Z'

    ### By has_notes

    Find all alerts that have notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=true'

    Find all alerts that have no notes attached:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'has_notes[is]=false'

    ### By tags

    Filter by tag name, matched case-insensitively.

    Find all alerts that have any of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[one_of]=known issue'

    Find all alerts that have all of the given tags:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[all_of]=known issue' \\
    			--data 'tags[all_of]=customer impacting'

    Find all alerts that do not have any of the given tags. Untagged alerts are included:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'tags[not_in]=known issue'

    ### By attributes

    Alerts can be filtered by their attribute values. Each filter is keyed by the alert
    attribute ID, followed by an operator and the values to match. The accepted operators
    depend on the attribute's type.

    Find all alerts where attribute 01GBSQF3FHF7FWZQNWGHAVQ804 is one of two catalog entries:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01GBSQF3FHF7FWZQNWGHAVQ804' \\
    			--data 'attributes[01GBSQF3FHF7FWZQNWGHAVQ804][one_of]=01ET65M7ZARSFZ6TFDFVQDN9AA'

    You can filter on multiple attributes at once, and the result will be alerts that match
    all of them.

    ### Maintenance windows
    By default, all alerts are returned including those held by a maintenance window.
    To exclude alerts that are held by a maintenance window:

    		curl --get 'https://api.incident.io/v2/alerts' \\
    			--data 'include_maintenance_window[is]=false'


    Args:
        page_size (int): Number of alerts to return per page Default: 25. Example: 25.
        after (str | Unset): If provided, pass this as the 'after' param to load the next page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        deduplication_key (AlertsV2ListDeduplicationKey | Unset): Filter on alert deduplication
            key. The accepted operator is 'is'. Example: {'is': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status (AlertsV2ListStatus | Unset): Filter on alert status. The accepted operators are
            'one_of', or 'not_in'. Example: {'one_of': ['firing']}.
        alert_source (AlertsV2ListAlertSource | Unset): Filter on alert source by ID. The accepted
            operators are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        alert_group_id (AlertsV2ListAlertGroupId | Unset): Filter on alert group ID. Returns
            alerts that belong to any of the specified groups. The accepted operator is 'one_of'.
            Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        created_at (AlertsV2ListCreatedAt | Unset): Filter on alert created at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        updated_at (AlertsV2ListUpdatedAt | Unset): Filter on alert updated at timestamp. Accepted
            operators are 'gte', 'lte' and 'date_range'. Example: {'gte': ['2025-01-01']}.
        attributes (AlertsV2ListAttributes | Unset): Filter on an alerts attributes. Alert
            attribute ID should be sent, followed by the operator and values. Accepted operator will
            depend on the attribute type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        has_notes (AlertsV2ListHasNotes | Unset): Filter on whether an alert has notes. The
            accepted operator is 'is'. Example: {'is': ['true']}.
        tags (AlertsV2ListTags | Unset): Filter on the tags applied to an alert, by tag name. The
            accepted operators are 'one_of', 'all_of' and 'not_in'. Example: {'one_of': ['known
            issue']}.
        include_maintenance_window (AlertsV2ListIncludeMaintenanceWindow | Unset): Filter on
            whether to include maintenance window alerts. The accepted operator is 'is'. Example:
            {'is': ['true']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsListResultV2 | ErrorResponse
     """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            deduplication_key=deduplication_key,
            status=status,
            alert_source=alert_source,
            alert_group_id=alert_group_id,
            created_at=created_at,
            updated_at=updated_at,
            attributes=attributes,
            has_notes=has_notes,
            tags=tags,
            include_maintenance_window=include_maintenance_window,
        )
    ).parsed
