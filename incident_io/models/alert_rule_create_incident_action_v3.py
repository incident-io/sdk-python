from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRuleCreateIncidentActionV3")


@_attrs_define(kw_only=True)
class AlertRuleCreateIncidentActionV3:
    """Create an incident from the alert, or attach it to the incident its group already has

    Example:
        {'auto_decline': False, 'incident_template': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'is_private': False,
            'membership_teams': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        auto_decline (bool | Unset): Decline the incident if its alerts resolve before anyone accepts it. Defaults to
            false. Example: False.
        incident_template (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        is_private (bool | Unset): Create the incident as private. A private alert, or a template whose incident type
            allows only private incidents, makes it private anyway. Defaults to false. Example: False.
        membership_teams (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    auto_decline: bool | Unset = UNSET
    incident_template: EngineParamBindingPayloadV3 | Unset = UNSET
    is_private: bool | Unset = UNSET
    membership_teams: EngineParamBindingPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_decline = self.auto_decline

        incident_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_template, Unset):
            incident_template = self.incident_template.to_dict()

        is_private = self.is_private

        membership_teams: dict[str, Any] | Unset = UNSET
        if not isinstance(self.membership_teams, Unset):
            membership_teams = self.membership_teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_decline is not UNSET:
            field_dict["auto_decline"] = auto_decline
        if incident_template is not UNSET:
            field_dict["incident_template"] = incident_template
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if membership_teams is not UNSET:
            field_dict["membership_teams"] = membership_teams

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        auto_decline = d.pop("auto_decline", UNSET)

        _incident_template = d.pop("incident_template", UNSET)
        incident_template: EngineParamBindingPayloadV3 | Unset
        if isinstance(_incident_template, Unset):
            incident_template = UNSET
        else:
            incident_template = EngineParamBindingPayloadV3.from_dict(
                _incident_template
            )

        is_private = d.pop("is_private", UNSET)

        _membership_teams = d.pop("membership_teams", UNSET)
        membership_teams: EngineParamBindingPayloadV3 | Unset
        if isinstance(_membership_teams, Unset):
            membership_teams = UNSET
        else:
            membership_teams = EngineParamBindingPayloadV3.from_dict(_membership_teams)

        alert_rule_create_incident_action_v3 = cls(
            auto_decline=auto_decline,
            incident_template=incident_template,
            is_private=is_private,
            membership_teams=membership_teams,
        )

        alert_rule_create_incident_action_v3.additional_properties = d
        return alert_rule_create_incident_action_v3

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
