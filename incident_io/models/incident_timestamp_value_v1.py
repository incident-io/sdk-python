from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampValueV1")


@_attrs_define
class IncidentTimestampValueV1:
    """
    Example:
        {'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}

    Attributes:
        name (str): Name of the lifecycle event Example: last_activity.
        last_occurred_at (datetime.datetime | Unset): When this last occurred, if it did Example:
            2021-08-17T13:28:57.801578Z.
    """

    name: str
    last_occurred_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        last_occurred_at: str | Unset = UNSET
        if not isinstance(self.last_occurred_at, Unset):
            last_occurred_at = self.last_occurred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if last_occurred_at is not UNSET:
            field_dict["last_occurred_at"] = last_occurred_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        _last_occurred_at = d.pop("last_occurred_at", UNSET)
        last_occurred_at: datetime.datetime | Unset
        if isinstance(_last_occurred_at, Unset):
            last_occurred_at = UNSET
        else:
            last_occurred_at = datetime.datetime.fromisoformat(_last_occurred_at)

        incident_timestamp_value_v1 = cls(
            name=name,
            last_occurred_at=last_occurred_at,
        )

        incident_timestamp_value_v1.additional_properties = d
        return incident_timestamp_value_v1

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
