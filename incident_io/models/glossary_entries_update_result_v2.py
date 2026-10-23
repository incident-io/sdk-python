from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.glossary_entry_v2 import GlossaryEntryV2


T = TypeVar("T", bound="GlossaryEntriesUpdateResultV2")


@_attrs_define(kw_only=True)
class GlossaryEntriesUpdateResultV2:
    """
    Example:
        {'glossary_entry': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Payment service provider that
            handles card authorisations', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'item': 'PSP', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        glossary_entry (GlossaryEntryV2): A glossary entry is one term an organisation has coined — an acronym, a
            service name, or a piece of internal jargon — and the description of what it means.

            AI features use the glossary, in rank order, so they understand those terms. Lower
            ranks come first. Deleting an entry archives it, which frees the term so it can be
            coined again as a new entry. Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Payment
            service provider that handles card authorisations', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'item': 'PSP', 'rank':
            1, 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    glossary_entry: GlossaryEntryV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        glossary_entry = self.glossary_entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "glossary_entry": glossary_entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.glossary_entry_v2 import GlossaryEntryV2

        d = dict(src_dict)
        glossary_entry = GlossaryEntryV2.from_dict(d.pop("glossary_entry"))

        glossary_entries_update_result_v2 = cls(
            glossary_entry=glossary_entry,
        )

        glossary_entries_update_result_v2.additional_properties = d
        return glossary_entries_update_result_v2

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
