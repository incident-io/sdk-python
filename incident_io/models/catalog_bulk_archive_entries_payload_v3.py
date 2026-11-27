from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogBulkArchiveEntriesPayloadV3")


@_attrs_define(kw_only=True)
class CatalogBulkArchiveEntriesPayloadV3:
    """
    Example:
        {'catalog_type_id': '01GW2G3V0S59R238FAHPDS1R66', 'entry_ids': ['01GW2G3V0S59R238FAHPDS1R67',
            '01GW2G3V0S59R238FAHPDS1R68']}

    Attributes:
        catalog_type_id (str): The ID of the catalog type that the entries belong to Example:
            01GW2G3V0S59R238FAHPDS1R66.
        entry_ids (list[str]): The IDs of the entries to archive. Maximum 250 entries per request. Example:
            ['01GW2G3V0S59R238FAHPDS1R67', '01GW2G3V0S59R238FAHPDS1R68'].
    """

    catalog_type_id: str
    entry_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_type_id = self.catalog_type_id

        entry_ids = self.entry_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_type_id": catalog_type_id,
                "entry_ids": entry_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        catalog_type_id = d.pop("catalog_type_id")

        entry_ids = cast(list[str], d.pop("entry_ids"))

        catalog_bulk_archive_entries_payload_v3 = cls(
            catalog_type_id=catalog_type_id,
            entry_ids=entry_ids,
        )

        catalog_bulk_archive_entries_payload_v3.additional_properties = d
        return catalog_bulk_archive_entries_payload_v3

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
