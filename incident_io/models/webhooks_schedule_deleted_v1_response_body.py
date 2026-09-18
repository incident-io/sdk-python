from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_schedule_deleted_v1_response_body_event_type import (
    WebhooksScheduleDeletedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.schedule_slim_v2 import ScheduleSlimV2


T = TypeVar("T", bound="WebhooksScheduleDeletedV1ResponseBody")


@_attrs_define
class WebhooksScheduleDeletedV1ResponseBody:
    """
    Example:
        {'event_type': 'schedule.deleted_v1', 'schedule.deleted_v1': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        event_type (WebhooksScheduleDeletedV1ResponseBodyEventType): What type of event is this webhook for? Example:
            schedule.deleted_v1.
        schedule_deleted_v1 (ScheduleSlimV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary On-Call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    event_type: WebhooksScheduleDeletedV1ResponseBodyEventType
    schedule_deleted_v1: ScheduleSlimV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        schedule_deleted_v1 = self.schedule_deleted_v1.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "schedule.deleted_v1": schedule_deleted_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_slim_v2 import ScheduleSlimV2

        d = dict(src_dict)
        event_type = WebhooksScheduleDeletedV1ResponseBodyEventType(d.pop("event_type"))

        schedule_deleted_v1 = ScheduleSlimV2.from_dict(d.pop("schedule.deleted_v1"))

        webhooks_schedule_deleted_v1_response_body = cls(
            event_type=event_type,
            schedule_deleted_v1=schedule_deleted_v1,
        )

        webhooks_schedule_deleted_v1_response_body.additional_properties = d
        return webhooks_schedule_deleted_v1_response_body

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
