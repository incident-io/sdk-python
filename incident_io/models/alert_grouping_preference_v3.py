from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_grouping_preference_v3_kind import AlertGroupingPreferenceV3Kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_grouping_conditional_branch_v3 import (
        AlertGroupingConditionalBranchV3,
    )
    from ..models.alert_grouping_default_branch_v3 import AlertGroupingDefaultBranchV3
    from ..models.expression_payload_v3 import ExpressionPayloadV3


T = TypeVar("T", bound="AlertGroupingPreferenceV3")


@_attrs_define(kw_only=True)
class AlertGroupingPreferenceV3:
    """An alert grouping preference: one team's, or the organisation's default

    Example:
        {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so
            group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}], 'created_at': '2021-08-17T13:28:57.801578Z', 'default': {'settings': {'ai_enabled':
            False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so group them
            together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}, 'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind': 'team', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}

    Attributes:
        branches (list[AlertGroupingConditionalBranchV3]): Grouping branches in order. Alert rules group an alert by the
            first branch whose conditions hold, else by the default. Alert routes only use the default. Example:
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so
            group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}].
        created_at (datetime.datetime): When this preference was created Example: 2021-08-17T13:28:57.801578Z.
        default (AlertGroupingDefaultBranchV3): The fallback branch: how to group the alerts that no conditional branch
            matches Example: {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters
            describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
        expressions (list[ExpressionPayloadV3]): Expressions the branches' conditions test or compare against, as
            expressions["reference"] Example: [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        id (str): Unique identifier for this preference Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        kind (AlertGroupingPreferenceV3Kind): Which preference this is. A team's preference groups the alerts of its
            team. The organisation's default groups alerts that no team's preference groups, and is used only by alert
            rules. Example: team.
        updated_at (datetime.datetime): When this preference was last updated Example: 2021-08-17T13:28:57.801578Z.
        version (int): The current version number. Every update writes the next version. Example: 3.
        team_id (str | Unset): The catalog entry ID of the team, set only for a team's preference Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    branches: list[AlertGroupingConditionalBranchV3]
    created_at: datetime.datetime
    default: AlertGroupingDefaultBranchV3
    expressions: list[ExpressionPayloadV3]
    id: str
    kind: AlertGroupingPreferenceV3Kind
    updated_at: datetime.datetime
    version: int
    team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        created_at = self.created_at.isoformat()

        default = self.default.to_dict()

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        id = self.id

        kind = self.kind.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branches": branches,
                "created_at": created_at,
                "default": default,
                "expressions": expressions,
                "id": id,
                "kind": kind,
                "updated_at": updated_at,
                "version": version,
            }
        )
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_conditional_branch_v3 import (
            AlertGroupingConditionalBranchV3,
        )
        from ..models.alert_grouping_default_branch_v3 import (
            AlertGroupingDefaultBranchV3,
        )
        from ..models.expression_payload_v3 import ExpressionPayloadV3

        d = dict(src_dict)
        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = AlertGroupingConditionalBranchV3.from_dict(
                branches_item_data
            )

            branches.append(branches_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        default = AlertGroupingDefaultBranchV3.from_dict(d.pop("default"))

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        id = d.pop("id")

        kind = AlertGroupingPreferenceV3Kind(d.pop("kind"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        team_id = d.pop("team_id", UNSET)

        alert_grouping_preference_v3 = cls(
            branches=branches,
            created_at=created_at,
            default=default,
            expressions=expressions,
            id=id,
            kind=kind,
            updated_at=updated_at,
            version=version,
            team_id=team_id,
        )

        alert_grouping_preference_v3.additional_properties = d
        return alert_grouping_preference_v3

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
