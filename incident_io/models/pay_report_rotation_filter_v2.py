from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PayReportRotationFilterV2")


@_attrs_define
class PayReportRotationFilterV2:
    """Narrows one of a report's schedules to some of its rotations.

    Example:
        {'rotation_ids': ['primary'], 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        rotation_ids (list[str]): Which of the schedule's rotations to include. To include all of them, leave this
            schedule out of rotation_filters rather than listing every rotation here. Example: ['primary'].
        schedule_id (str): The schedule to narrow. Must also appear in schedule_ids. Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    rotation_ids: list[str]
    schedule_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rotation_ids = self.rotation_ids

        schedule_id = self.schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rotation_ids": rotation_ids,
                "schedule_id": schedule_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rotation_ids = cast(list[str], d.pop("rotation_ids"))

        schedule_id = d.pop("schedule_id")

        pay_report_rotation_filter_v2 = cls(
            rotation_ids=rotation_ids,
            schedule_id=schedule_id,
        )

        pay_report_rotation_filter_v2.additional_properties = d
        return pay_report_rotation_filter_v2

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
