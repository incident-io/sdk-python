from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlossaryEntriesCreatePayloadV2")


@_attrs_define(kw_only=True)
class GlossaryEntriesCreatePayloadV2:
    """
    Example:
        {'after': '01G0J1EXE7AXZ2C93K61WBPYEH', 'description': 'Payment service provider that handles card
            authorisations', 'item': 'PSP'}

    Attributes:
        description (str): What the term means Example: Payment service provider that handles card authorisations.
        item (str): The term, for example an acronym or service name. Unique among live entries, ignoring case. Example:
            PSP.
        after (str | Unset): ID of a live glossary entry. The new entry is inserted immediately after it. Omit to append
            the entry to the end. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    description: str
    item: str
    after: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        item = self.item

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "item": item,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        item = d.pop("item")

        after = d.pop("after", UNSET)

        glossary_entries_create_payload_v2 = cls(
            description=description,
            item=item,
            after=after,
        )

        glossary_entries_create_payload_v2.additional_properties = d
        return glossary_entries_create_payload_v2

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
