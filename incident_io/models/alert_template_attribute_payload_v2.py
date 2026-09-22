from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_template_attribute_binding_payload_v2 import (
        AlertTemplateAttributeBindingPayloadV2,
    )


T = TypeVar("T", bound="AlertTemplateAttributePayloadV2")


@_attrs_define(kw_only=True)
class AlertTemplateAttributePayloadV2:
    """
    Example:
        {'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}

    Attributes:
        alert_attribute_id (str): ID of the alert attribute to set with this binding Example: abc123.
        binding (AlertTemplateAttributeBindingPayloadV2):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}.
    """

    alert_attribute_id: str
    binding: AlertTemplateAttributeBindingPayloadV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_attribute_id = self.alert_attribute_id

        binding = self.binding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_attribute_id": alert_attribute_id,
                "binding": binding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_template_attribute_binding_payload_v2 import (
            AlertTemplateAttributeBindingPayloadV2,
        )

        d = dict(src_dict)
        alert_attribute_id = d.pop("alert_attribute_id")

        binding = AlertTemplateAttributeBindingPayloadV2.from_dict(d.pop("binding"))

        alert_template_attribute_payload_v2 = cls(
            alert_attribute_id=alert_attribute_id,
            binding=binding,
        )

        alert_template_attribute_payload_v2.additional_properties = d
        return alert_template_attribute_payload_v2

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
