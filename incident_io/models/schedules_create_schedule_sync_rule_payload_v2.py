from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_sync_rule_create_payload_v2 import (
        ScheduleSyncRuleCreatePayloadV2,
    )


T = TypeVar("T", bound="SchedulesCreateScheduleSyncRulePayloadV2")


@_attrs_define
class SchedulesCreateScheduleSyncRulePayloadV2:
    """
    Example:
        {'schedule_sync_rule': {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT', 'schedule_sync_target_id':
            '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}}

    Attributes:
        schedule_sync_rule (ScheduleSyncRuleCreatePayloadV2):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'rotation_id': '01JXYZ000000000000000000RT', 'schedule_sync_target_id': '01JXYZ000000000000000000AB',
            'sync_type': 'on_call'}.
    """

    schedule_sync_rule: ScheduleSyncRuleCreatePayloadV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_sync_rule = self.schedule_sync_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_rule": schedule_sync_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_sync_rule_create_payload_v2 import (
            ScheduleSyncRuleCreatePayloadV2,
        )

        d = dict(src_dict)
        schedule_sync_rule = ScheduleSyncRuleCreatePayloadV2.from_dict(
            d.pop("schedule_sync_rule")
        )

        schedules_create_schedule_sync_rule_payload_v2 = cls(
            schedule_sync_rule=schedule_sync_rule,
        )

        schedules_create_schedule_sync_rule_payload_v2.additional_properties = d
        return schedules_create_schedule_sync_rule_payload_v2

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
