from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlossaryEntriesUpdatePayloadV2")


@_attrs_define(kw_only=True)
class GlossaryEntriesUpdatePayloadV2:
    """
    Example:
        {'description': 'Payment service provider that handles card authorisations', 'item': 'PSP'}

    Attributes:
        description (str): What the term means Example: Payment service provider that handles card authorisations.
        item (str): The term, e.g. an acronym or service name Example: PSP.
    """

    description: str
    item: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        item = self.item

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "item": item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        item = d.pop("item")

        glossary_entries_update_payload_v2 = cls(
            description=description,
            item=item,
        )

        glossary_entries_update_payload_v2.additional_properties = d
        return glossary_entries_update_payload_v2

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
