from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlossaryEntryV2")


@_attrs_define(kw_only=True)
class GlossaryEntryV2:
    """A glossary entry is one term an organisation has coined — an acronym, a
    service name, or a piece of internal jargon — and the description of what it means.

    AI features use the glossary, in rank order, so they understand those terms. Lower
    ranks come first. Deleting an entry archives it, which frees the term so it can be
    coined again as a new entry.

        Example:
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Payment service provider that handles card
                authorisations', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'item': 'PSP', 'rank': 1, 'updated_at':
                '2021-08-17T13:28:57.801578Z'}

        Attributes:
            created_at (datetime.datetime): When the entry was created Example: 2021-08-17T13:28:57.801578Z.
            description (str): What the term means Example: Payment service provider that handles card authorisations.
            id (str): Unique identifier for this glossary entry Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            item (str): The term, e.g. an acronym or service name Example: PSP.
            rank (int): The entry's position in the glossary Example: 1.
            updated_at (datetime.datetime): When the entry was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    item: str
    rank: int
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        item = self.item

        rank = self.rank

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "item": item,
                "rank": rank,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        item = d.pop("item")

        rank = d.pop("rank")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        glossary_entry_v2 = cls(
            created_at=created_at,
            description=description,
            id=id,
            item=item,
            rank=rank,
            updated_at=updated_at,
        )

        glossary_entry_v2.additional_properties = d
        return glossary_entry_v2

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
