from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.maintenance_window_v1 import MaintenanceWindowV1


T = TypeVar("T", bound="MaintenanceWindowsShowResultV1")


@_attrs_define(kw_only=True)
class MaintenanceWindowsShowResultV1:
    """
    Example:
        {'maintenance_window': {'alert_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'archived_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T14:28:57.801578Z', 'escalation_targets':
            [{'escalation_paths': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'users': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'lead': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for database
            migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name': 'general', 'channel_type':
            'public', 'is_private': False}], 'notify_end_minutes_before': 5, 'notify_start_minutes_before': 15,
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'reroute_on_end': False, 'resolve_on_end': False,
            'show_in_sidebar': True, 'start_at': '2021-08-17T13:28:57.801578Z', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        maintenance_window (MaintenanceWindowV1):  Example: {'alert_condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}]}], 'archived_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T14:28:57.801578Z', 'escalation_targets':
            [{'escalation_paths': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'users': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'lead': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for database
            migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name': 'general', 'channel_type':
            'public', 'is_private': False}], 'notify_end_minutes_before': 5, 'notify_start_minutes_before': 15,
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'reroute_on_end': False, 'resolve_on_end': False,
            'show_in_sidebar': True, 'start_at': '2021-08-17T13:28:57.801578Z', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    maintenance_window: MaintenanceWindowV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_window = self.maintenance_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maintenance_window": maintenance_window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.maintenance_window_v1 import MaintenanceWindowV1

        d = dict(src_dict)
        maintenance_window = MaintenanceWindowV1.from_dict(d.pop("maintenance_window"))

        maintenance_windows_show_result_v1 = cls(
            maintenance_window=maintenance_window,
        )

        maintenance_windows_show_result_v1.additional_properties = d
        return maintenance_windows_show_result_v1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
