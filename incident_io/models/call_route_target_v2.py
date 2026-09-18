from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_route_target_v2_schedule_mode import CallRouteTargetV2ScheduleMode
from ..models.call_route_target_v2_type import CallRouteTargetV2Type
from ..models.call_route_target_v2_urgency import CallRouteTargetV2Urgency
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallRouteTargetV2")


@_attrs_define
class CallRouteTargetV2:
    """Someone a call route pages when a call comes in.

    Example:
        {'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}

    Attributes:
        id (str): Uniquely identifies an entity of this type Example: lawrencejones.
        type_ (CallRouteTargetV2Type): Whether a call route target is a user or a schedule Example: schedule.
        urgency (CallRouteTargetV2Urgency): The urgency of this escalation path target Example: high.
        schedule_mode (CallRouteTargetV2ScheduleMode | Unset): Only set for schedule targets, this specifies which users
            to fetch from the schedule. Use currently_on_call to notify whoever is on call right now across the schedule,
            all_users to notify every user attached to the schedule, or all_users_for_rota / currently_on_call_for_rota /
            next_on_call_for_rota to scope to a specific rota (in which case selected_rota_id is required). next_on_call
            notifies whoever is next on call across the schedule. Example: currently_on_call.
        selected_rota_id (str | Unset): For schedule targets, identifies which rota on the schedule the schedule_mode
            applies to. Required when schedule_mode is all_users_for_rota, currently_on_call_for_rota, or
            next_on_call_for_rota; must be omitted for other schedule_mode values. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    id: str
    type_: CallRouteTargetV2Type
    urgency: CallRouteTargetV2Urgency
    schedule_mode: CallRouteTargetV2ScheduleMode | Unset = UNSET
    selected_rota_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        urgency = self.urgency.value

        schedule_mode: str | Unset = UNSET
        if not isinstance(self.schedule_mode, Unset):
            schedule_mode = self.schedule_mode.value

        selected_rota_id = self.selected_rota_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "urgency": urgency,
            }
        )
        if schedule_mode is not UNSET:
            field_dict["schedule_mode"] = schedule_mode
        if selected_rota_id is not UNSET:
            field_dict["selected_rota_id"] = selected_rota_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = CallRouteTargetV2Type(d.pop("type"))

        urgency = CallRouteTargetV2Urgency(d.pop("urgency"))

        _schedule_mode = d.pop("schedule_mode", UNSET)
        schedule_mode: CallRouteTargetV2ScheduleMode | Unset
        if isinstance(_schedule_mode, Unset):
            schedule_mode = UNSET
        else:
            schedule_mode = CallRouteTargetV2ScheduleMode(_schedule_mode)

        selected_rota_id = d.pop("selected_rota_id", UNSET)

        call_route_target_v2 = cls(
            id=id,
            type_=type_,
            urgency=urgency,
            schedule_mode=schedule_mode,
            selected_rota_id=selected_rota_id,
        )

        call_route_target_v2.additional_properties = d
        return call_route_target_v2

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
