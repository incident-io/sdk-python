from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.glossary_entry_rank_update_v2 import GlossaryEntryRankUpdateV2


T = TypeVar("T", bound="GlossaryEntriesUpdateRanksPayloadV2")


@_attrs_define(kw_only=True)
class GlossaryEntriesUpdateRanksPayloadV2:
    """
    Example:
        {'rank_updates': [{'rank': 3, 'resource_id': '01FCNDV6P870EA6S7TK1DSYDG0'}]}

    Attributes:
        rank_updates (list[GlossaryEntryRankUpdateV2]): The new rank of every live glossary entry Example: [{'rank': 3,
            'resource_id': '01FCNDV6P870EA6S7TK1DSYDG0'}].
    """

    rank_updates: list[GlossaryEntryRankUpdateV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank_updates = []
        for rank_updates_item_data in self.rank_updates:
            rank_updates_item = rank_updates_item_data.to_dict()
            rank_updates.append(rank_updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank_updates": rank_updates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.glossary_entry_rank_update_v2 import (
            GlossaryEntryRankUpdateV2,
        )

        d = dict(src_dict)
        rank_updates = []
        _rank_updates = d.pop("rank_updates")
        for rank_updates_item_data in _rank_updates:
            rank_updates_item = GlossaryEntryRankUpdateV2.from_dict(
                rank_updates_item_data
            )

            rank_updates.append(rank_updates_item)

        glossary_entries_update_ranks_payload_v2 = cls(
            rank_updates=rank_updates,
        )

        glossary_entries_update_ranks_payload_v2.additional_properties = d
        return glossary_entries_update_ranks_payload_v2

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
