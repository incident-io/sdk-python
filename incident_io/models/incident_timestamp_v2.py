from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentTimestampV2")


@_attrs_define
class IncidentTimestampV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}

    Attributes:
        id (str): Unique ID of this incident timestamp Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Unique name of this timestamp Example: Impact started.
        rank (int): Order in which this timestamp should be shown Example: 1.
    """

    id: str
    name: str
    rank: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "rank": rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        incident_timestamp_v2 = cls(
            id=id,
            name=name,
            rank=rank,
        )

        incident_timestamp_v2.additional_properties = d
        return incident_timestamp_v2

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
