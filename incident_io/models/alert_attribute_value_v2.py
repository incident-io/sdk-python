from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attribute_catalog_entry_v2 import AlertAttributeCatalogEntryV2


T = TypeVar("T", bound="AlertAttributeValueV2")


@_attrs_define
class AlertAttributeValueV2:
    """
    Example:
        {'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}

    Attributes:
        catalog_entry (AlertAttributeCatalogEntryV2 | Unset):  Example: {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}.
        label (str | Unset): The human readable label of this value for convenience. Will match the literal if this is a
            primitive type, or be the name of the catalog entry if this is a catalog entry Example: Payments Team.
        literal (str | Unset): If set, this is the literal value of the step parameter Example: SEV123.
    """

    catalog_entry: AlertAttributeCatalogEntryV2 | Unset = UNSET
    label: str | Unset = UNSET
    literal: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catalog_entry, Unset):
            catalog_entry = self.catalog_entry.to_dict()

        label = self.label

        literal = self.literal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_entry is not UNSET:
            field_dict["catalog_entry"] = catalog_entry
        if label is not UNSET:
            field_dict["label"] = label
        if literal is not UNSET:
            field_dict["literal"] = literal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attribute_catalog_entry_v2 import (
            AlertAttributeCatalogEntryV2,
        )

        d = dict(src_dict)
        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: AlertAttributeCatalogEntryV2 | Unset
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = AlertAttributeCatalogEntryV2.from_dict(_catalog_entry)

        label = d.pop("label", UNSET)

        literal = d.pop("literal", UNSET)

        alert_attribute_value_v2 = cls(
            catalog_entry=catalog_entry,
            label=label,
            literal=literal,
        )

        alert_attribute_value_v2.additional_properties = d
        return alert_attribute_value_v2

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
