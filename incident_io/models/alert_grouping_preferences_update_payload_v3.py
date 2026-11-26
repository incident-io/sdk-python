from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_grouping_conditional_branch_v3 import (
        AlertGroupingConditionalBranchV3,
    )
    from ..models.alert_grouping_default_branch_v3 import AlertGroupingDefaultBranchV3
    from ..models.expression_payload_v3 import ExpressionPayloadV3


T = TypeVar("T", bound="AlertGroupingPreferencesUpdatePayloadV3")


@_attrs_define(kw_only=True)
class AlertGroupingPreferencesUpdatePayloadV3:
    """
    Example:
        {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'settings':
            {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same outage, so
            group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}], 'default': {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the
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
            'version': 4}

    Attributes:
        default (AlertGroupingDefaultBranchV3): The fallback branch: how to group the alerts that no conditional branch
            matches Example: {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters
            describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
        branches (list[AlertGroupingConditionalBranchV3] | Unset): Grouping branches in order. Alert rules group an
            alert by the first branch whose conditions hold, else by the default. Alert routes only use the default. Omit it
            on an update to keep the current branches and expressions. Only organisations that use alert rules can add or
            change branches. Example: [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe the same
            outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}}].
        expressions (list[ExpressionPayloadV3] | Unset): Expressions the branches' conditions test or compare against,
            as expressions["reference"]. Omit it on an update to keep the current expressions, which are also kept when
            branches are omitted. Example: [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
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
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        version (int | Unset): The version this update writes. When set, it must be one more than the preference's
            current version, so two editors can't overwrite each other. When omitted, the update applies to the current
            version. Example: 4.
    """

    default: AlertGroupingDefaultBranchV3
    branches: list[AlertGroupingConditionalBranchV3] | Unset = UNSET
    expressions: list[ExpressionPayloadV3] | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default.to_dict()

        branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        expressions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
            }
        )
        if branches is not UNSET:
            field_dict["branches"] = branches
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if version is not UNSET:
            field_dict["version"] = version

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
        default = AlertGroupingDefaultBranchV3.from_dict(d.pop("default"))

        _branches = d.pop("branches", UNSET)
        branches: list[AlertGroupingConditionalBranchV3] | Unset = UNSET
        if _branches is not UNSET:
            branches = []
            for branches_item_data in _branches:
                branches_item = AlertGroupingConditionalBranchV3.from_dict(
                    branches_item_data
                )

                branches.append(branches_item)

        _expressions = d.pop("expressions", UNSET)
        expressions: list[ExpressionPayloadV3] | Unset = UNSET
        if _expressions is not UNSET:
            expressions = []
            for expressions_item_data in _expressions:
                expressions_item = ExpressionPayloadV3.from_dict(expressions_item_data)

                expressions.append(expressions_item)

        version = d.pop("version", UNSET)

        alert_grouping_preferences_update_payload_v3 = cls(
            default=default,
            branches=branches,
            expressions=expressions,
            version=version,
        )

        alert_grouping_preferences_update_payload_v3.additional_properties = d
        return alert_grouping_preferences_update_payload_v3

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
