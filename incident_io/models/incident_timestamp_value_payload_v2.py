from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampValuePayloadV2")


@_attrs_define
class IncidentTimestampValuePayloadV2:
    """
    Example:
        {'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        incident_timestamp_id (str): The id of the incident timestamp that this incident timestamp value is associated
            with. Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        value (datetime.datetime | Unset): The current value of this timestamp, for this incident Example:
            2021-08-17T13:28:57.801578Z.
    """

    incident_timestamp_id: str
    value: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_timestamp_id = self.incident_timestamp_id

        value: str | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timestamp_id": incident_timestamp_id,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incident_timestamp_id = d.pop("incident_timestamp_id")

        _value = d.pop("value", UNSET)
        value: datetime.datetime | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = datetime.datetime.fromisoformat(_value)

        incident_timestamp_value_payload_v2 = cls(
            incident_timestamp_id=incident_timestamp_id,
            value=value,
        )

        incident_timestamp_value_payload_v2.additional_properties = d
        return incident_timestamp_value_payload_v2

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
