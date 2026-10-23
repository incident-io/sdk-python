from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.glossary_entry_v2 import GlossaryEntryV2


T = TypeVar("T", bound="GlossaryEntriesUpdateRanksResultV2")


@_attrs_define(kw_only=True)
class GlossaryEntriesUpdateRanksResultV2:
    """
    Example:
        {'glossary_entries': [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Payment service provider
            that handles card authorisations', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'item': 'PSP', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        glossary_entries (list[GlossaryEntryV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Payment service provider that handles card authorisations', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'item': 'PSP', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}].
    """

    glossary_entries: list[GlossaryEntryV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        glossary_entries = []
        for glossary_entries_item_data in self.glossary_entries:
            glossary_entries_item = glossary_entries_item_data.to_dict()
            glossary_entries.append(glossary_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "glossary_entries": glossary_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.glossary_entry_v2 import GlossaryEntryV2

        d = dict(src_dict)
        glossary_entries = []
        _glossary_entries = d.pop("glossary_entries")
        for glossary_entries_item_data in _glossary_entries:
            glossary_entries_item = GlossaryEntryV2.from_dict(
                glossary_entries_item_data
            )

            glossary_entries.append(glossary_entries_item)

        glossary_entries_update_ranks_result_v2 = cls(
            glossary_entries=glossary_entries,
        )

        glossary_entries_update_ranks_result_v2.additional_properties = d
        return glossary_entries_update_ranks_result_v2

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
