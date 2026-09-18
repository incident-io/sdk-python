from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_attribute_v2 import AlertAttributeV2


T = TypeVar("T", bound="AlertAttributesUpdateResultV2")


@_attrs_define
class AlertAttributesUpdateResultV2:
    """
    Example:
        {'alert_attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}}

    Attributes:
        alert_attribute (AlertAttributeV2):  Example: {'array': False, 'emoji': 'fire', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service', 'required': False, 'type':
            'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}.
    """

    alert_attribute: AlertAttributeV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_attribute = self.alert_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_attribute": alert_attribute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attribute_v2 import AlertAttributeV2

        d = dict(src_dict)
        alert_attribute = AlertAttributeV2.from_dict(d.pop("alert_attribute"))

        alert_attributes_update_result_v2 = cls(
            alert_attribute=alert_attribute,
        )

        alert_attributes_update_result_v2.additional_properties = d
        return alert_attributes_update_result_v2

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
