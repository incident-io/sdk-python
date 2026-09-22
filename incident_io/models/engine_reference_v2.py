from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EngineReferenceV2")


@_attrs_define(kw_only=True)
class EngineReferenceV2:
    """
    Example:
        {'array': False, 'key': 'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected
            Team', 'type': 'IncidentSeverity'}

    Attributes:
        array (bool): If true, the reference can refer to 0 to many items Example: False.
        key (str): Unique identifier of field will set Example: incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"].
        label (str): Human readable label for the field (with context) Example: Incident -> Affected Team.
        type_ (str): The type of this resource in the engine Example: IncidentSeverity.
    """

    array: bool
    key: str
    label: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        key = self.key

        label = self.label

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "key": key,
                "label": label,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        array = d.pop("array")

        key = d.pop("key")

        label = d.pop("label")

        type_ = d.pop("type")

        engine_reference_v2 = cls(
            array=array,
            key=key,
            label=label,
            type_=type_,
        )

        engine_reference_v2.additional_properties = d
        return engine_reference_v2

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
