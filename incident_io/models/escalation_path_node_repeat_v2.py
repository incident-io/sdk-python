from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationPathNodeRepeatV2")


@_attrs_define(kw_only=True)
class EscalationPathNodeRepeatV2:
    """
    Example:
        {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        repeat_times (int): How many times to repeat these nodes Example: 3.
        to_node (str): Which node ID we begin repeating from. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    repeat_times: int
    to_node: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repeat_times = self.repeat_times

        to_node = self.to_node

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repeat_times": repeat_times,
                "to_node": to_node,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        repeat_times = d.pop("repeat_times")

        to_node = d.pop("to_node")

        escalation_path_node_repeat_v2 = cls(
            repeat_times=repeat_times,
            to_node=to_node,
        )

        escalation_path_node_repeat_v2.additional_properties = d
        return escalation_path_node_repeat_v2

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
