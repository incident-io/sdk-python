from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleReplicaSourceV2")


@_attrs_define(kw_only=True)
class ScheduleReplicaSourceV2:
    """
    Example:
        {'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        layer_id (str): The ID of the layer within the rotation to replicate. Rotations can have multiple layers that
            stack on top of each other, and you must specify which layer to replicate. Example: 01G0J1EXE7AXZ2C93K61WBPYNH.
        rotation_id (str): The ID of the rotation within the schedule to replicate. Each schedule can have multiple
            rotations, and you can choose which ones to include in the replica. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    layer_id: str
    rotation_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layer_id = self.layer_id

        rotation_id = self.rotation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layer_id": layer_id,
                "rotation_id": rotation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        layer_id = d.pop("layer_id")

        rotation_id = d.pop("rotation_id")

        schedule_replica_source_v2 = cls(
            layer_id=layer_id,
            rotation_id=rotation_id,
        )

        schedule_replica_source_v2.additional_properties = d
        return schedule_replica_source_v2

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
