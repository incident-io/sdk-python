from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_schedule_shift_change_v1_response_body_event_type import (
    WebhooksScheduleShiftChangeV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.schedule_shift_change_v2 import ScheduleShiftChangeV2


T = TypeVar("T", bound="WebhooksScheduleShiftChangeV1ResponseBody")


@_attrs_define
class WebhooksScheduleShiftChangeV1ResponseBody:
    """
    Example:
        {'event_type': 'schedule.shift_change_v1', 'schedule.shift_change_v1': {'current_users': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}], 'previous_users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}],
            'schedule': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary
            On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}}

    Attributes:
        event_type (WebhooksScheduleShiftChangeV1ResponseBodyEventType): What type of event is this webhook for?
            Example: schedule.shift_change_v1.
        schedule_shift_change_v1 (ScheduleShiftChangeV2):  Example: {'current_users': [{'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}], 'previous_users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'schedule': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule',
            'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'timezone': 'Europe/London', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}.
    """

    event_type: WebhooksScheduleShiftChangeV1ResponseBodyEventType
    schedule_shift_change_v1: ScheduleShiftChangeV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        schedule_shift_change_v1 = self.schedule_shift_change_v1.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "schedule.shift_change_v1": schedule_shift_change_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_shift_change_v2 import (
            ScheduleShiftChangeV2,
        )

        d = dict(src_dict)
        event_type = WebhooksScheduleShiftChangeV1ResponseBodyEventType(
            d.pop("event_type")
        )

        schedule_shift_change_v1 = ScheduleShiftChangeV2.from_dict(
            d.pop("schedule.shift_change_v1")
        )

        webhooks_schedule_shift_change_v1_response_body = cls(
            event_type=event_type,
            schedule_shift_change_v1=schedule_shift_change_v1,
        )

        webhooks_schedule_shift_change_v1_response_body.additional_properties = d
        return webhooks_schedule_shift_change_v1_response_body

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
