from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_message_destination_payload_v3 import (
        AlertMessageDestinationPayloadV3,
    )
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertMessageConfigPayloadV3")


@_attrs_define(kw_only=True)
class AlertMessageConfigPayloadV3:
    """
    Example:
        {'destinations': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'ms_teams_targets': {'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'channel_visibility': 'public', 'group_alerts_summary': False},
            'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'public',
            'group_alerts_summary': False}}], 'template': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        destinations (list[AlertMessageDestinationPayloadV3]): The destinations (Slack/Teams channels) alert messages
            are sent to Example: [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'ms_teams_targets': {'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'channel_visibility': 'public', 'group_alerts_summary': False},
            'slack_targets': {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'public',
            'group_alerts_summary': False}}].
        template (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    destinations: list[AlertMessageDestinationPayloadV3]
    template: EngineParamBindingPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destinations = []
        for destinations_item_data in self.destinations:
            destinations_item = destinations_item_data.to_dict()
            destinations.append(destinations_item)

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinations": destinations,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_message_destination_payload_v3 import (
            AlertMessageDestinationPayloadV3,
        )
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        destinations = []
        _destinations = d.pop("destinations")
        for destinations_item_data in _destinations:
            destinations_item = AlertMessageDestinationPayloadV3.from_dict(
                destinations_item_data
            )

            destinations.append(destinations_item)

        _template = d.pop("template", UNSET)
        template: EngineParamBindingPayloadV3 | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = EngineParamBindingPayloadV3.from_dict(_template)

        alert_message_config_payload_v3 = cls(
            destinations=destinations,
            template=template,
        )

        alert_message_config_payload_v3.additional_properties = d
        return alert_message_config_payload_v3

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
