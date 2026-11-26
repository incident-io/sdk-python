from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_grouping_preference_v3 import AlertGroupingPreferenceV3
    from ..models.pagination_meta_result_v3 import PaginationMetaResultV3


T = TypeVar("T", bound="AlertGroupingPreferencesListResultV3")


@_attrs_define(kw_only=True)
class AlertGroupingPreferencesListResultV3:
    """
    Example:
        {'alert_grouping_preferences': [{'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new
            clusters describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}], 'created_at':
            '2021-08-17T13:28:57.801578Z', 'default': {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the
            old and new clusters describe the same outage, so group them together.', 'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'team', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25}}

    Attributes:
        alert_grouping_preferences (list[AlertGroupingPreferenceV3]):  Example: [{'branches': [{'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'settings': {'ai_enabled': False, 'ai_instructions':
            'Alerts from the old and new clusters describe the same outage, so group them together.', 'enabled': True,
            'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}],
            'created_at': '2021-08-17T13:28:57.801578Z', 'default': {'settings': {'ai_enabled': False, 'ai_instructions':
            'Alerts from the old and new clusters describe the same outage, so group them together.', 'enabled': True,
            'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}},
            'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns':
            {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'team', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}].
        pagination_meta (PaginationMetaResultV3):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    alert_grouping_preferences: list[AlertGroupingPreferenceV3]
    pagination_meta: PaginationMetaResultV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_grouping_preferences = []
        for alert_grouping_preferences_item_data in self.alert_grouping_preferences:
            alert_grouping_preferences_item = (
                alert_grouping_preferences_item_data.to_dict()
            )
            alert_grouping_preferences.append(alert_grouping_preferences_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_grouping_preferences": alert_grouping_preferences,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_preference_v3 import (
            AlertGroupingPreferenceV3,
        )
        from ..models.pagination_meta_result_v3 import (
            PaginationMetaResultV3,
        )

        d = dict(src_dict)
        alert_grouping_preferences = []
        _alert_grouping_preferences = d.pop("alert_grouping_preferences")
        for alert_grouping_preferences_item_data in _alert_grouping_preferences:
            alert_grouping_preferences_item = AlertGroupingPreferenceV3.from_dict(
                alert_grouping_preferences_item_data
            )

            alert_grouping_preferences.append(alert_grouping_preferences_item)

        pagination_meta = PaginationMetaResultV3.from_dict(d.pop("pagination_meta"))

        alert_grouping_preferences_list_result_v3 = cls(
            alert_grouping_preferences=alert_grouping_preferences,
            pagination_meta=pagination_meta,
        )

        alert_grouping_preferences_list_result_v3.additional_properties = d
        return alert_grouping_preferences_list_result_v3

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
