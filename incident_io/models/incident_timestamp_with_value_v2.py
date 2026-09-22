from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_timestamp_v2 import IncidentTimestampV2
    from ..models.incident_timestamp_value_v2 import IncidentTimestampValueV2


T = TypeVar("T", bound="IncidentTimestampWithValueV2")


@_attrs_define(kw_only=True)
class IncidentTimestampWithValueV2:
    """
    Example:
        {'incident_timestamp': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'value':
            {'value': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_timestamp (IncidentTimestampV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact
            started', 'rank': 1}.
        value (IncidentTimestampValueV2 | Unset):  Example: {'value': '2021-08-17T13:28:57.801578Z'}.
    """

    incident_timestamp: IncidentTimestampV2
    value: IncidentTimestampValueV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_timestamp = self.incident_timestamp.to_dict()

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timestamp": incident_timestamp,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_timestamp_v2 import IncidentTimestampV2
        from ..models.incident_timestamp_value_v2 import (
            IncidentTimestampValueV2,
        )

        d = dict(src_dict)
        incident_timestamp = IncidentTimestampV2.from_dict(d.pop("incident_timestamp"))

        _value = d.pop("value", UNSET)
        value: IncidentTimestampValueV2 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IncidentTimestampValueV2.from_dict(_value)

        incident_timestamp_with_value_v2 = cls(
            incident_timestamp=incident_timestamp,
            value=value,
        )

        incident_timestamp_with_value_v2.additional_properties = d
        return incident_timestamp_with_value_v2

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
