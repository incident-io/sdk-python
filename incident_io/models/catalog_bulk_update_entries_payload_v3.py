from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_entry_payload_v3 import PartialEntryPayloadV3


T = TypeVar("T", bound="CatalogBulkUpdateEntriesPayloadV3")


@_attrs_define(kw_only=True)
class CatalogBulkUpdateEntriesPayloadV3:
    """
    Example:
        {'catalog_type_id': '01GW2G3V0S59R238FAHPDS1R66', 'entries': [{'aliases': ['abc123'], 'attribute_values':
            {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'entry_id': 'abc123',
            'external_id': 'abc123', 'name': 'abc123', 'rank': 1}, {'aliases': ['abc123'], 'attribute_values': {'abc123':
            {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'entry_id': 'abc123', 'external_id':
            'abc123', 'name': 'abc123', 'rank': 1}], 'update_attributes': ['01GW2G3V0S59R238FAHPDS1R66',
            '01GW2G3V0S59R238FAHPDS1R67']}

    Attributes:
        catalog_type_id (str): The unique identifier of the catalog type containing the entries Example:
            01GW2G3V0S59R238FAHPDS1R66.
        entries (list[PartialEntryPayloadV3]): A list of entries to update with their new values. Maximum 250 entries
            per request. Example: [{'aliases': ['abc123'], 'attribute_values': {'abc123': {'array_value': [{'literal':
            'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'entry_id': 'abc123', 'external_id': 'abc123', 'name': 'abc123',
            'rank': 1}, {'aliases': ['abc123'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123'}],
            'value': {'literal': 'SEV123'}}}, 'entry_id': 'abc123', 'external_id': 'abc123', 'name': 'abc123', 'rank': 1}].
        update_attributes (list[str] | Unset): Optional list of specific attribute IDs to update across all entries.
            When provided, only these attributes in attribute_values will be updated and all other attributes will be
            preserved. This parameter only affects attribute_values - it does not affect core entry fields like name, rank,
            aliases, or external_id, which follow their individual omission rules. Example: ['01GW2G3V0S59R238FAHPDS1R66',
            '01GW2G3V0S59R238FAHPDS1R67'].
    """

    catalog_type_id: str
    entries: list[PartialEntryPayloadV3]
    update_attributes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_type_id = self.catalog_type_id

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        update_attributes: list[str] | Unset = UNSET
        if not isinstance(self.update_attributes, Unset):
            update_attributes = self.update_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_type_id": catalog_type_id,
                "entries": entries,
            }
        )
        if update_attributes is not UNSET:
            field_dict["update_attributes"] = update_attributes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.partial_entry_payload_v3 import (
            PartialEntryPayloadV3,
        )

        d = dict(src_dict)
        catalog_type_id = d.pop("catalog_type_id")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = PartialEntryPayloadV3.from_dict(entries_item_data)

            entries.append(entries_item)

        update_attributes = cast(list[str], d.pop("update_attributes", UNSET))

        catalog_bulk_update_entries_payload_v3 = cls(
            catalog_type_id=catalog_type_id,
            entries=entries,
            update_attributes=update_attributes,
        )

        catalog_bulk_update_entries_payload_v3.additional_properties = d
        return catalog_bulk_update_entries_payload_v3

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
