from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowUpPriorityV2")


@_attrs_define
class FollowUpPriorityV2:
    """
    Example:
        {'description': 'A follow-up that requires immediate attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name':
            'Urgent', 'rank': 10}

    Attributes:
        id (str): Unique identifier for the follow-up priority option Example: 01GNW4BAQ7XRMFF6FHKNXDFPRW.
        name (str): Name of the follow-up priority option Example: Urgent.
        rank (int): Rank is used to order the follow-up priority options correctly Example: 10.
        description (str | Unset): Description of the follow-up priority option Example: A follow-up that requires
            immediate attention..
    """

    id: str
    name: str
    rank: int
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rank = self.rank

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "rank": rank,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        description = d.pop("description", UNSET)

        follow_up_priority_v2 = cls(
            id=id,
            name=name,
            rank=rank,
            description=description,
        )

        follow_up_priority_v2.additional_properties = d
        return follow_up_priority_v2

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
