from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_route_v3 import AlertRouteV3


T = TypeVar("T", bound="AlertRoutesCreateResultV3")


@_attrs_define(kw_only=True)
class AlertRoutesCreateResultV3:
    """
    Example:
        {'alert_route': {'alert_sources': [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference':
            'alert.priority'}}]}]}], 'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'created_at': '2021-08-17T13:28:57.801578Z', 'enabled': False,
            'escalation_config': {'auto_cancel_escalations': False, 'escalation_targets': [{'escalation_paths':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'when_alert_joins_group': {'grace_period_seconds': 60, 'mode': 'on_each_new_alert'}}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}, 'navigate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}, 'returns': {'array':
            True, 'type': 'IncidentStatus'}}], 'reference': 'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'},
            'root_reference': 'incident.status'}], 'grouping_config': {'default': {'enabled': True, 'grouping_keys':
            [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_config': {'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference':
            'alert.priority'}}]}], 'enabled': False, 'incident_template': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'template': {'custom_fields': [{'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-
            wins'}], 'incident_mode': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_type': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'membership_teams': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'name':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'severity': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'merge_strategy': 'first-wins'}, 'start_in_triage': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'summary': {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}}},
            'is_private': False, 'message_config': {'destinations': [{'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}], 'ms_teams_targets':
            {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'abc123', 'group_alerts_summary': False},
            'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'abc123',
            'group_alerts_summary': False}}], 'template': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'name': 'Production
            incidents', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z',
            'version': 1}}

    Attributes:
        alert_route (AlertRouteV3):  Example: {'alert_sources': [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}]}], 'condition_groups': [{'conditions': [{'operation': {'label':
            'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}], 'created_at':
            '2021-08-17T13:28:57.801578Z', 'enabled': False, 'escalation_config': {'auto_cancel_escalations': False,
            'escalation_targets': [{'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'when_alert_joins_group': {'grace_period_seconds': 60, 'mode':
            'on_each_new_alert'}}, 'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}],
            'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast':
            {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference': '1235', 'reference_label':
            'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'grouping_config': {'default': {'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_config':
            {'auto_decline_enabled': False, 'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'enabled': False, 'incident_template': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'template':
            {'custom_fields': [{'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'merge_strategy': 'first-wins'}], 'incident_mode': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'incident_type': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'membership_teams':
            {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'name': {'autogenerated': False, 'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'severity': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy':
            'first-wins'}, 'start_in_triage': {'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'summary':
            {'autogenerated': False, 'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}}}, 'is_private': False, 'message_config':
            {'destinations': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'ms_teams_targets': {'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'channel_visibility': 'abc123', 'group_alerts_summary': False}, 'slack_targets': {'binding': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'channel_visibility': 'abc123', 'group_alerts_summary': False}}], 'template':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'name': 'Production incidents', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 1}.
    """

    alert_route: AlertRouteV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_route = self.alert_route.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_route": alert_route,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_route_v3 import AlertRouteV3

        d = dict(src_dict)
        alert_route = AlertRouteV3.from_dict(d.pop("alert_route"))

        alert_routes_create_result_v3 = cls(
            alert_route=alert_route,
        )

        alert_routes_create_result_v3.additional_properties = d
        return alert_routes_create_result_v3

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
