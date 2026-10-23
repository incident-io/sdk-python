from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlossaryEntryRankUpdateV2")


@_attrs_define(kw_only=True)
class GlossaryEntryRankUpdateV2:
    """The new rank for one live glossary entry.

    Example:
        {'rank': 3, 'resource_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        rank (int): Desired rank for this resource Example: 3.
        resource_id (str): ID of the resource Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    rank: int
    resource_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        resource_id = self.resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "resource_id": resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rank = d.pop("rank")

        resource_id = d.pop("resource_id")

        glossary_entry_rank_update_v2 = cls(
            rank=rank,
            resource_id=resource_id,
        )

        glossary_entry_rank_update_v2.additional_properties = d
        return glossary_entry_rank_update_v2

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
