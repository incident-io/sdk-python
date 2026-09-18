from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attribute_v2 import AlertAttributeV2
    from ..models.alert_attribute_value_v2 import AlertAttributeValueV2


T = TypeVar("T", bound="AlertAttributeEntryV2")


@_attrs_define
class AlertAttributeEntryV2:
    """
    Example:
        {'array_value': [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}],
            'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}

    Attributes:
        attribute (AlertAttributeV2):  Example: {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66',
            'name': 'service', 'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}.
        array_value (list[AlertAttributeValueV2] | Unset): The value of the attribute if it is an array Example:
            [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}].
        value (AlertAttributeValueV2 | Unset):  Example: {'catalog_entry': {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments
            Team', 'literal': 'SEV123'}.
    """

    attribute: AlertAttributeV2
    array_value: list[AlertAttributeValueV2] | Unset = UNSET
    value: AlertAttributeValueV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute = self.attribute.to_dict()

        array_value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.array_value, Unset):
            array_value = []
            for array_value_item_data in self.array_value:
                array_value_item = array_value_item_data.to_dict()
                array_value.append(array_value_item)

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute": attribute,
            }
        )
        if array_value is not UNSET:
            field_dict["array_value"] = array_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attribute_v2 import AlertAttributeV2
        from ..models.alert_attribute_value_v2 import (
            AlertAttributeValueV2,
        )

        d = dict(src_dict)
        attribute = AlertAttributeV2.from_dict(d.pop("attribute"))

        _array_value = d.pop("array_value", UNSET)
        array_value: list[AlertAttributeValueV2] | Unset = UNSET
        if _array_value is not UNSET:
            array_value = []
            for array_value_item_data in _array_value:
                array_value_item = AlertAttributeValueV2.from_dict(
                    array_value_item_data
                )

                array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: AlertAttributeValueV2 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = AlertAttributeValueV2.from_dict(_value)

        alert_attribute_entry_v2 = cls(
            attribute=attribute,
            array_value=array_value,
            value=value,
        )

        alert_attribute_entry_v2.additional_properties = d
        return alert_attribute_entry_v2

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
