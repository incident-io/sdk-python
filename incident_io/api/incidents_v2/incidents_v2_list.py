from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incidents_list_result_v2 import IncidentsListResultV2
from ...models.incidents_v2_list_created_at import IncidentsV2ListCreatedAt
from ...models.incidents_v2_list_custom_field import IncidentsV2ListCustomField
from ...models.incidents_v2_list_filter_mode import IncidentsV2ListFilterMode
from ...models.incidents_v2_list_incident_role import IncidentsV2ListIncidentRole
from ...models.incidents_v2_list_incident_type import IncidentsV2ListIncidentType
from ...models.incidents_v2_list_mode import IncidentsV2ListMode
from ...models.incidents_v2_list_severity import IncidentsV2ListSeverity
from ...models.incidents_v2_list_sort_by import IncidentsV2ListSortBy
from ...models.incidents_v2_list_status import IncidentsV2ListStatus
from ...models.incidents_v2_list_status_category import IncidentsV2ListStatusCategory
from ...models.incidents_v2_list_updated_at import IncidentsV2ListUpdatedAt
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    sort_by: IncidentsV2ListSortBy
    | Unset = IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST,
    filter_mode: IncidentsV2ListFilterMode | Unset = UNSET,
    status: IncidentsV2ListStatus | Unset = UNSET,
    status_category: IncidentsV2ListStatusCategory | Unset = UNSET,
    created_at: IncidentsV2ListCreatedAt | Unset = UNSET,
    updated_at: IncidentsV2ListUpdatedAt | Unset = UNSET,
    severity: IncidentsV2ListSeverity | Unset = UNSET,
    incident_type: IncidentsV2ListIncidentType | Unset = UNSET,
    incident_role: IncidentsV2ListIncidentRole | Unset = UNSET,
    custom_field: IncidentsV2ListCustomField | Unset = UNSET,
    mode: IncidentsV2ListMode | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_filter_mode: str | Unset = UNSET
    if not isinstance(filter_mode, Unset):
        json_filter_mode = filter_mode.value

    params["filter_mode"] = json_filter_mode

    json_status: dict[str, Any] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.to_dict()
    if not isinstance(json_status, Unset):
        params.update(json_status)

    json_status_category: dict[str, Any] | Unset = UNSET
    if not isinstance(status_category, Unset):
        json_status_category = status_category.to_dict()
    if not isinstance(json_status_category, Unset):
        params.update(json_status_category)

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

    json_severity: dict[str, Any] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = severity.to_dict()
    if not isinstance(json_severity, Unset):
        params.update(json_severity)

    json_incident_type: dict[str, Any] | Unset = UNSET
    if not isinstance(incident_type, Unset):
        json_incident_type = incident_type.to_dict()
    if not isinstance(json_incident_type, Unset):
        params.update(json_incident_type)

    json_incident_role: dict[str, Any] | Unset = UNSET
    if not isinstance(incident_role, Unset):
        json_incident_role = incident_role.to_dict()
    if not isinstance(json_incident_role, Unset):
        params.update(json_incident_role)

    json_custom_field: dict[str, Any] | Unset = UNSET
    if not isinstance(custom_field, Unset):
        json_custom_field = custom_field.to_dict()
    if not isinstance(json_custom_field, Unset):
        params.update(json_custom_field)

    json_mode: dict[str, Any] | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.to_dict()
    if not isinstance(json_mode, Unset):
        params.update(json_mode)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | IncidentsListResultV2 | None:
    if response.status_code == 200:
        response_200 = IncidentsListResultV2.from_dict(response.json())

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
) -> Response[ErrorResponse | IncidentsListResultV2]:
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
    sort_by: IncidentsV2ListSortBy
    | Unset = IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST,
    filter_mode: IncidentsV2ListFilterMode | Unset = UNSET,
    status: IncidentsV2ListStatus | Unset = UNSET,
    status_category: IncidentsV2ListStatusCategory | Unset = UNSET,
    created_at: IncidentsV2ListCreatedAt | Unset = UNSET,
    updated_at: IncidentsV2ListUpdatedAt | Unset = UNSET,
    severity: IncidentsV2ListSeverity | Unset = UNSET,
    incident_type: IncidentsV2ListIncidentType | Unset = UNSET,
    incident_role: IncidentsV2ListIncidentRole | Unset = UNSET,
    custom_field: IncidentsV2ListCustomField | Unset = UNSET,
    mode: IncidentsV2ListMode | Unset = UNSET,
) -> Response[ErrorResponse | IncidentsListResultV2]:
    """ List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    The maximum page size that can be requested is 250.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be combined using the filter_mode parameter: 'all' (default) requires all filters
    to match (AND logic), while 'any' requires at least one filter to match (OR logic).
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[not_in]=ABC'

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all incidents created before
    or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[lte]=2021-01-02'

    To find incidents created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By status category

    Find all incidents that are in a status category. Some categories use a different
    name in the API than the one shown in the dashboard — most notably "live" (shown as
    "Active") and "learning" (shown as "Post-incident"). The full mapping is:

    | API value  | Shown in app as |
    | ---------- | --------------- |
    | triage     | Triage          |
    | live       | Active          |
    | learning   | Post-incident   |
    | paused     | Paused          |
    | closed     | Closed          |
    | declined   | Declined        |
    | canceled   | Canceled        |
    | merged     | Merged          |

    For example, to find all incidents the dashboard shows as "Active", filter on the
    "live" category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[not_in]=live'


    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[not_in]=ABC'

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=test'


    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][not_in]=XYZ'

    ### Sorting

    By default, results are ordered by their creation date. You can use the sort_by parameter
    to reverse this order:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'sort_by=created_at_oldest_first'

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An incident's ID. This endpoint will return a list of incidents after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        sort_by (IncidentsV2ListSortBy | Unset): What order to return results in. Default:
            IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST. Example: created_at_newest_first.
        filter_mode (IncidentsV2ListFilterMode | Unset): How to combine the filters: 'all'
            combines them with AND logic (all must match), 'any' combines them with OR logic (any can
            match). Defaults to 'all'. Example: all.
        status (IncidentsV2ListStatus | Unset): Filter on incident status. The accepted operators
            are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status_category (IncidentsV2ListStatusCategory | Unset): Filter on the category of the
            incidents status. The accepted operators are 'one_of', or 'not_in'. Example: {'one_of':
            ['active']}.
        created_at (IncidentsV2ListCreatedAt | Unset): Filter on incident created at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'created_at[gte]':
            ['2024-05-01']}.
        updated_at (IncidentsV2ListUpdatedAt | Unset): Filter on incident updated at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'updated_at[gte]':
            ['2024-05-01']}.
        severity (IncidentsV2ListSeverity | Unset): Filter on incident severity. The accepted
            operators are 'one_of', 'not_in', 'gte', 'lte'. Example: {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_type (IncidentsV2ListIncidentType | Unset): Filter on incident type. The accepted
            operators are 'one_of, or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_role (IncidentsV2ListIncidentRole | Unset): Filter on an incident role. Role ID
            should be sent, along with backlink attribute ID (if needed) followed by the operator and
            values. The accepted operators are 'one_of', 'is_blank'. Example:
            {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        custom_field (IncidentsV2ListCustomField | Unset): Filter on an incident custom field.
            Custom field ID should be sent, followed by the operator and values. Accepted operator
            will depend on the custom field type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        mode (IncidentsV2ListMode | Unset): Filter on incident mode. The accepted operator is
            'one_of'.  If this is not provided, this value defaults to `{"one_of": ["standard",
            "retrospective"] }`, meaning that test and tutorial incidents are not included. Example:
            {'one_of': ['retrospective']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsListResultV2]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        sort_by=sort_by,
        filter_mode=filter_mode,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
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
    sort_by: IncidentsV2ListSortBy
    | Unset = IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST,
    filter_mode: IncidentsV2ListFilterMode | Unset = UNSET,
    status: IncidentsV2ListStatus | Unset = UNSET,
    status_category: IncidentsV2ListStatusCategory | Unset = UNSET,
    created_at: IncidentsV2ListCreatedAt | Unset = UNSET,
    updated_at: IncidentsV2ListUpdatedAt | Unset = UNSET,
    severity: IncidentsV2ListSeverity | Unset = UNSET,
    incident_type: IncidentsV2ListIncidentType | Unset = UNSET,
    incident_role: IncidentsV2ListIncidentRole | Unset = UNSET,
    custom_field: IncidentsV2ListCustomField | Unset = UNSET,
    mode: IncidentsV2ListMode | Unset = UNSET,
) -> ErrorResponse | IncidentsListResultV2 | None:
    """ List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    The maximum page size that can be requested is 250.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be combined using the filter_mode parameter: 'all' (default) requires all filters
    to match (AND logic), while 'any' requires at least one filter to match (OR logic).
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[not_in]=ABC'

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all incidents created before
    or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[lte]=2021-01-02'

    To find incidents created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By status category

    Find all incidents that are in a status category. Some categories use a different
    name in the API than the one shown in the dashboard — most notably "live" (shown as
    "Active") and "learning" (shown as "Post-incident"). The full mapping is:

    | API value  | Shown in app as |
    | ---------- | --------------- |
    | triage     | Triage          |
    | live       | Active          |
    | learning   | Post-incident   |
    | paused     | Paused          |
    | closed     | Closed          |
    | declined   | Declined        |
    | canceled   | Canceled        |
    | merged     | Merged          |

    For example, to find all incidents the dashboard shows as "Active", filter on the
    "live" category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[not_in]=live'


    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[not_in]=ABC'

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=test'


    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][not_in]=XYZ'

    ### Sorting

    By default, results are ordered by their creation date. You can use the sort_by parameter
    to reverse this order:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'sort_by=created_at_oldest_first'

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An incident's ID. This endpoint will return a list of incidents after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        sort_by (IncidentsV2ListSortBy | Unset): What order to return results in. Default:
            IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST. Example: created_at_newest_first.
        filter_mode (IncidentsV2ListFilterMode | Unset): How to combine the filters: 'all'
            combines them with AND logic (all must match), 'any' combines them with OR logic (any can
            match). Defaults to 'all'. Example: all.
        status (IncidentsV2ListStatus | Unset): Filter on incident status. The accepted operators
            are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status_category (IncidentsV2ListStatusCategory | Unset): Filter on the category of the
            incidents status. The accepted operators are 'one_of', or 'not_in'. Example: {'one_of':
            ['active']}.
        created_at (IncidentsV2ListCreatedAt | Unset): Filter on incident created at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'created_at[gte]':
            ['2024-05-01']}.
        updated_at (IncidentsV2ListUpdatedAt | Unset): Filter on incident updated at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'updated_at[gte]':
            ['2024-05-01']}.
        severity (IncidentsV2ListSeverity | Unset): Filter on incident severity. The accepted
            operators are 'one_of', 'not_in', 'gte', 'lte'. Example: {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_type (IncidentsV2ListIncidentType | Unset): Filter on incident type. The accepted
            operators are 'one_of, or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_role (IncidentsV2ListIncidentRole | Unset): Filter on an incident role. Role ID
            should be sent, along with backlink attribute ID (if needed) followed by the operator and
            values. The accepted operators are 'one_of', 'is_blank'. Example:
            {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        custom_field (IncidentsV2ListCustomField | Unset): Filter on an incident custom field.
            Custom field ID should be sent, followed by the operator and values. Accepted operator
            will depend on the custom field type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        mode (IncidentsV2ListMode | Unset): Filter on incident mode. The accepted operator is
            'one_of'.  If this is not provided, this value defaults to `{"one_of": ["standard",
            "retrospective"] }`, meaning that test and tutorial incidents are not included. Example:
            {'one_of': ['retrospective']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsListResultV2
     """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        sort_by=sort_by,
        filter_mode=filter_mode,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    sort_by: IncidentsV2ListSortBy
    | Unset = IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST,
    filter_mode: IncidentsV2ListFilterMode | Unset = UNSET,
    status: IncidentsV2ListStatus | Unset = UNSET,
    status_category: IncidentsV2ListStatusCategory | Unset = UNSET,
    created_at: IncidentsV2ListCreatedAt | Unset = UNSET,
    updated_at: IncidentsV2ListUpdatedAt | Unset = UNSET,
    severity: IncidentsV2ListSeverity | Unset = UNSET,
    incident_type: IncidentsV2ListIncidentType | Unset = UNSET,
    incident_role: IncidentsV2ListIncidentRole | Unset = UNSET,
    custom_field: IncidentsV2ListCustomField | Unset = UNSET,
    mode: IncidentsV2ListMode | Unset = UNSET,
) -> Response[ErrorResponse | IncidentsListResultV2]:
    """ List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    The maximum page size that can be requested is 250.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be combined using the filter_mode parameter: 'all' (default) requires all filters
    to match (AND logic), while 'any' requires at least one filter to match (OR logic).
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[not_in]=ABC'

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all incidents created before
    or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[lte]=2021-01-02'

    To find incidents created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By status category

    Find all incidents that are in a status category. Some categories use a different
    name in the API than the one shown in the dashboard — most notably "live" (shown as
    "Active") and "learning" (shown as "Post-incident"). The full mapping is:

    | API value  | Shown in app as |
    | ---------- | --------------- |
    | triage     | Triage          |
    | live       | Active          |
    | learning   | Post-incident   |
    | paused     | Paused          |
    | closed     | Closed          |
    | declined   | Declined        |
    | canceled   | Canceled        |
    | merged     | Merged          |

    For example, to find all incidents the dashboard shows as "Active", filter on the
    "live" category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[not_in]=live'


    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[not_in]=ABC'

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=test'


    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][not_in]=XYZ'

    ### Sorting

    By default, results are ordered by their creation date. You can use the sort_by parameter
    to reverse this order:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'sort_by=created_at_oldest_first'

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An incident's ID. This endpoint will return a list of incidents after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        sort_by (IncidentsV2ListSortBy | Unset): What order to return results in. Default:
            IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST. Example: created_at_newest_first.
        filter_mode (IncidentsV2ListFilterMode | Unset): How to combine the filters: 'all'
            combines them with AND logic (all must match), 'any' combines them with OR logic (any can
            match). Defaults to 'all'. Example: all.
        status (IncidentsV2ListStatus | Unset): Filter on incident status. The accepted operators
            are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status_category (IncidentsV2ListStatusCategory | Unset): Filter on the category of the
            incidents status. The accepted operators are 'one_of', or 'not_in'. Example: {'one_of':
            ['active']}.
        created_at (IncidentsV2ListCreatedAt | Unset): Filter on incident created at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'created_at[gte]':
            ['2024-05-01']}.
        updated_at (IncidentsV2ListUpdatedAt | Unset): Filter on incident updated at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'updated_at[gte]':
            ['2024-05-01']}.
        severity (IncidentsV2ListSeverity | Unset): Filter on incident severity. The accepted
            operators are 'one_of', 'not_in', 'gte', 'lte'. Example: {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_type (IncidentsV2ListIncidentType | Unset): Filter on incident type. The accepted
            operators are 'one_of, or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_role (IncidentsV2ListIncidentRole | Unset): Filter on an incident role. Role ID
            should be sent, along with backlink attribute ID (if needed) followed by the operator and
            values. The accepted operators are 'one_of', 'is_blank'. Example:
            {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        custom_field (IncidentsV2ListCustomField | Unset): Filter on an incident custom field.
            Custom field ID should be sent, followed by the operator and values. Accepted operator
            will depend on the custom field type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        mode (IncidentsV2ListMode | Unset): Filter on incident mode. The accepted operator is
            'one_of'.  If this is not provided, this value defaults to `{"one_of": ["standard",
            "retrospective"] }`, meaning that test and tutorial incidents are not included. Example:
            {'one_of': ['retrospective']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | IncidentsListResultV2]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        sort_by=sort_by,
        filter_mode=filter_mode,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 25,
    after: str | Unset = UNSET,
    sort_by: IncidentsV2ListSortBy
    | Unset = IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST,
    filter_mode: IncidentsV2ListFilterMode | Unset = UNSET,
    status: IncidentsV2ListStatus | Unset = UNSET,
    status_category: IncidentsV2ListStatusCategory | Unset = UNSET,
    created_at: IncidentsV2ListCreatedAt | Unset = UNSET,
    updated_at: IncidentsV2ListUpdatedAt | Unset = UNSET,
    severity: IncidentsV2ListSeverity | Unset = UNSET,
    incident_type: IncidentsV2ListIncidentType | Unset = UNSET,
    incident_role: IncidentsV2ListIncidentRole | Unset = UNSET,
    custom_field: IncidentsV2ListCustomField | Unset = UNSET,
    mode: IncidentsV2ListMode | Unset = UNSET,
) -> ErrorResponse | IncidentsListResultV2 | None:
    """ List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    The maximum page size that can be requested is 250.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be combined using the filter_mode parameter: 'all' (default) requires all filters
    to match (AND logic), while 'any' requires at least one filter to match (OR logic).
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status[not_in]=ABC'

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are "gte" (greater than or equal to), "lte" (less than or equal to), and
    "date_range" (between two dates). The following example finds all incidents created before
    or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[lte]=2021-01-02'

    To find incidents created within a specific date range, use the date_range option with
    tilde-separated dates:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'created_at[date_range]=2024-12-02~2024-12-08'

    ### By status category

    Find all incidents that are in a status category. Some categories use a different
    name in the API than the one shown in the dashboard — most notably "live" (shown as
    "Active") and "learning" (shown as "Post-incident"). The full mapping is:

    | API value  | Shown in app as |
    | ---------- | --------------- |
    | triage     | Triage          |
    | live       | Active          |
    | learning   | Post-incident   |
    | paused     | Paused          |
    | closed     | Closed          |
    | declined   | Declined        |
    | canceled   | Canceled        |
    | merged     | Merged          |

    For example, to find all incidents the dashboard shows as "Active", filter on the
    "live" category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'status_category[not_in]=live'


    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_type[not_in]=ABC'

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'mode[one_of]=test'


    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \\
    			--data 'incident_role[ABC][is_set]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'custom_field[ABC][not_in]=XYZ'

    ### Sorting

    By default, results are ordered by their creation date. You can use the sort_by parameter
    to reverse this order:

    		curl \\
    			--get 'https://api.incident.io/v2/incidents' \\
    			--data 'sort_by=created_at_oldest_first'

    Args:
        page_size (int | Unset): Integer number of records to return Default: 25. Example: 25.
        after (str | Unset): An incident's ID. This endpoint will return a list of incidents after
            this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        sort_by (IncidentsV2ListSortBy | Unset): What order to return results in. Default:
            IncidentsV2ListSortBy.CREATED_AT_NEWEST_FIRST. Example: created_at_newest_first.
        filter_mode (IncidentsV2ListFilterMode | Unset): How to combine the filters: 'all'
            combines them with AND logic (all must match), 'any' combines them with OR logic (any can
            match). Defaults to 'all'. Example: all.
        status (IncidentsV2ListStatus | Unset): Filter on incident status. The accepted operators
            are 'one_of', or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        status_category (IncidentsV2ListStatusCategory | Unset): Filter on the category of the
            incidents status. The accepted operators are 'one_of', or 'not_in'. Example: {'one_of':
            ['active']}.
        created_at (IncidentsV2ListCreatedAt | Unset): Filter on incident created at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'created_at[gte]':
            ['2024-05-01']}.
        updated_at (IncidentsV2ListUpdatedAt | Unset): Filter on incident updated at timestamp.
            The accepted operators are 'gte', 'lte' and 'date_range'. Example: {'updated_at[gte]':
            ['2024-05-01']}.
        severity (IncidentsV2ListSeverity | Unset): Filter on incident severity. The accepted
            operators are 'one_of', 'not_in', 'gte', 'lte'. Example: {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_type (IncidentsV2ListIncidentType | Unset): Filter on incident type. The accepted
            operators are 'one_of, or 'not_in'. Example: {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804']}.
        incident_role (IncidentsV2ListIncidentRole | Unset): Filter on an incident role. Role ID
            should be sent, along with backlink attribute ID (if needed) followed by the operator and
            values. The accepted operators are 'one_of', 'is_blank'. Example:
            {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804',
            '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        custom_field (IncidentsV2ListCustomField | Unset): Filter on an incident custom field.
            Custom field ID should be sent, followed by the operator and values. Accepted operator
            will depend on the custom field type. Example: {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of':
            ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}.
        mode (IncidentsV2ListMode | Unset): Filter on incident mode. The accepted operator is
            'one_of'.  If this is not provided, this value defaults to `{"one_of": ["standard",
            "retrospective"] }`, meaning that test and tutorial incidents are not included. Example:
            {'one_of': ['retrospective']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | IncidentsListResultV2
     """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            sort_by=sort_by,
            filter_mode=filter_mode,
            status=status,
            status_category=status_category,
            created_at=created_at,
            updated_at=updated_at,
            severity=severity,
            incident_type=incident_type,
            incident_role=incident_role,
            custom_field=custom_field,
            mode=mode,
        )
    ).parsed
