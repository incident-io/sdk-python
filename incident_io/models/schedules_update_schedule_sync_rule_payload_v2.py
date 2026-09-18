from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedules_update_schedule_sync_rule_payload_v2_sync_type import (
    SchedulesUpdateScheduleSyncRulePayloadV2SyncType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedules_update_schedule_sync_rule_payload_v2_annotations import (
        SchedulesUpdateScheduleSyncRulePayloadV2Annotations,
    )


T = TypeVar("T", bound="SchedulesUpdateScheduleSyncRulePayloadV2")


@_attrs_define
class SchedulesUpdateScheduleSyncRulePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'sync_type': 'on_call'}

    Attributes:
        sync_type (SchedulesUpdateScheduleSyncRulePayloadV2SyncType): Which schedule members sync to the user group
            Example: on_call.
        annotations (SchedulesUpdateScheduleSyncRulePayloadV2Annotations | Unset): Annotations that track metadata about
            this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        permanent_member_user_ids (list[str] | Unset): IDs of users to always keep in the Slack user group, regardless
            of who is on call. Each must be an active user in your organisation. Replaces the rule's current permanent
            members: pass an empty array to remove them all, or omit the field to leave them unchanged. Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    sync_type: SchedulesUpdateScheduleSyncRulePayloadV2SyncType
    annotations: SchedulesUpdateScheduleSyncRulePayloadV2Annotations | Unset = UNSET
    permanent_member_user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_type = self.sync_type.value

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        permanent_member_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.permanent_member_user_ids, Unset):
            permanent_member_user_ids = self.permanent_member_user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_type": sync_type,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if permanent_member_user_ids is not UNSET:
            field_dict["permanent_member_user_ids"] = permanent_member_user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedules_update_schedule_sync_rule_payload_v2_annotations import (
            SchedulesUpdateScheduleSyncRulePayloadV2Annotations,
        )

        d = dict(src_dict)
        sync_type = SchedulesUpdateScheduleSyncRulePayloadV2SyncType(d.pop("sync_type"))

        _annotations = d.pop("annotations", UNSET)
        annotations: SchedulesUpdateScheduleSyncRulePayloadV2Annotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = SchedulesUpdateScheduleSyncRulePayloadV2Annotations.from_dict(
                _annotations
            )

        permanent_member_user_ids = cast(
            list[str], d.pop("permanent_member_user_ids", UNSET)
        )

        schedules_update_schedule_sync_rule_payload_v2 = cls(
            sync_type=sync_type,
            annotations=annotations,
            permanent_member_user_ids=permanent_member_user_ids,
        )

        schedules_update_schedule_sync_rule_payload_v2.additional_properties = d
        return schedules_update_schedule_sync_rule_payload_v2

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
