from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_sources_validate_payload_v2_source_type import (
    AlertSourcesValidatePayloadV2SourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_template_payload_v2 import AlertTemplatePayloadV2


T = TypeVar("T", bound="AlertSourcesValidatePayloadV2")


@_attrs_define(kw_only=True)
class AlertSourcesValidatePayloadV2:
    """
    Example:
        {'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'source_type': 'alertmanager', 'template': {'attributes':
            [{'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'description': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'expressions':
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'is_private': False, 'title': {'literal': 'SEV123', 'reference': 'incident.severity'}, 'visible_to_teams':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}}

    Attributes:
        source_type (AlertSourcesValidatePayloadV2SourceType): Type of alert source Example: alertmanager.
        template (AlertTemplatePayloadV2):  Example: {'attributes': [{'alert_attribute_id': 'abc123', 'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins',
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'description': {'literal': 'SEV123',
            'reference': 'incident.severity'}, 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'is_private': False, 'title': {'literal': 'SEV123', 'reference':
            'incident.severity'}, 'visible_to_teams': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}.
        owning_team_ids (list[str] | Unset): IDs of teams that own this alert source Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    source_type: AlertSourcesValidatePayloadV2SourceType
    template: AlertTemplatePayloadV2
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type.value

        template = self.template.to_dict()

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
                "template": template,
            }
        )
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_template_payload_v2 import (
            AlertTemplatePayloadV2,
        )

        d = dict(src_dict)
        source_type = AlertSourcesValidatePayloadV2SourceType(d.pop("source_type"))

        template = AlertTemplatePayloadV2.from_dict(d.pop("template"))

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        alert_sources_validate_payload_v2 = cls(
            source_type=source_type,
            template=template,
            owning_team_ids=owning_team_ids,
        )

        alert_sources_validate_payload_v2.additional_properties = d
        return alert_sources_validate_payload_v2

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
