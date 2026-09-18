from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeveritiesUpdatePayloadV1")


@_attrs_define
class SeveritiesUpdatePayloadV1:
    """
    Example:
        {'description': 'Issues with **low impact**.', 'name': 'Minor', 'rank': 1}

    Attributes:
        description (str): Description of the severity Example: Issues with **low impact**..
        name (str): Human readable name of the severity Example: Minor.
        rank (int | Unset): Rank to help sort severities (lower numbers are less severe) Example: 1.
    """

    description: str
    name: str
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        rank = d.pop("rank", UNSET)

        severities_update_payload_v1 = cls(
            description=description,
            name=name,
            rank=rank,
        )

        severities_update_payload_v1.additional_properties = d
        return severities_update_payload_v1

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
