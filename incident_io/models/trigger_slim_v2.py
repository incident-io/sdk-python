from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TriggerSlimV2")


@_attrs_define(kw_only=True)
class TriggerSlimV2:
    """
    Example:
        {'label': 'Incident Updated', 'name': 'incident.updated'}

    Attributes:
        label (str): Human readable identifier for this trigger Example: Incident Updated.
        name (str): Unique name of the trigger Example: incident.updated.
    """

    label: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        label = d.pop("label")

        name = d.pop("name")

        trigger_slim_v2 = cls(
            label=label,
            name=name,
        )

        trigger_slim_v2.additional_properties = d
        return trigger_slim_v2

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
