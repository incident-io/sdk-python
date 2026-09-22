from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.schedule_override_v2 import ScheduleOverrideV2


T = TypeVar("T", bound="SchedulesListOverridesResultV2")


@_attrs_define(kw_only=True)
class SchedulesListOverridesResultV2:
    """
    Example:
        {'overrides': [{'created_at': '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        overrides (list[ScheduleOverrideV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'end_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'rotation_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    overrides: list[ScheduleOverrideV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overrides = []
        for overrides_item_data in self.overrides:
            overrides_item = overrides_item_data.to_dict()
            overrides.append(overrides_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overrides": overrides,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.schedule_override_v2 import ScheduleOverrideV2

        d = dict(src_dict)
        overrides = []
        _overrides = d.pop("overrides")
        for overrides_item_data in _overrides:
            overrides_item = ScheduleOverrideV2.from_dict(overrides_item_data)

            overrides.append(overrides_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        schedules_list_overrides_result_v2 = cls(
            overrides=overrides,
            pagination_meta=pagination_meta,
        )

        schedules_list_overrides_result_v2.additional_properties = d
        return schedules_list_overrides_result_v2

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
