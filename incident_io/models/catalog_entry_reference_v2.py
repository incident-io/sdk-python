from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogEntryReferenceV2")


@_attrs_define(kw_only=True)
class CatalogEntryReferenceV2:
    """
    Example:
        {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'catalog_entry_name': 'Primary escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        catalog_entry_id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        catalog_entry_name (str): The name of this entry Example: Primary escalation.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        archived_at (datetime.datetime | Unset): When this entry was archived Example: 2021-08-17T14:28:57.801578Z.
    """

    catalog_entry_id: str
    catalog_entry_name: str
    catalog_type_id: str
    archived_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entry_id = self.catalog_entry_id

        catalog_entry_name = self.catalog_entry_name

        catalog_type_id = self.catalog_type_id

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entry_id": catalog_entry_id,
                "catalog_entry_name": catalog_entry_name,
                "catalog_type_id": catalog_type_id,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        catalog_entry_id = d.pop("catalog_entry_id")

        catalog_entry_name = d.pop("catalog_entry_name")

        catalog_type_id = d.pop("catalog_type_id")

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        catalog_entry_reference_v2 = cls(
            catalog_entry_id=catalog_entry_id,
            catalog_entry_name=catalog_entry_name,
            catalog_type_id=catalog_type_id,
            archived_at=archived_at,
        )

        catalog_entry_reference_v2.additional_properties = d
        return catalog_entry_reference_v2

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
