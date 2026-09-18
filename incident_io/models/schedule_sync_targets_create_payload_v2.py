from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_sync_target_create_payload_v2 import (
        ScheduleSyncTargetCreatePayloadV2,
    )


T = TypeVar("T", bound="ScheduleSyncTargetsCreatePayloadV2")


@_attrs_define
class ScheduleSyncTargetsCreatePayloadV2:
    """
    Example:
        {'schedule_sync_target': {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'},
            'new_slack_user_group': {'description': 'The team responsible for Project A', 'handle': 'project-team-a',
            'name': 'Project Team A', 'slack_team_id': 'T01234567'}, 'slack_user_group_id': 'S06MNNU5BMK'}}

    Attributes:
        schedule_sync_target (ScheduleSyncTargetCreatePayloadV2):  Example: {'add_bot_to_group': True, 'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'new_slack_user_group': {'description': 'The team responsible for
            Project A', 'handle': 'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'},
            'slack_user_group_id': 'S06MNNU5BMK'}.
    """

    schedule_sync_target: ScheduleSyncTargetCreatePayloadV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_sync_target = self.schedule_sync_target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_target": schedule_sync_target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_sync_target_create_payload_v2 import (
            ScheduleSyncTargetCreatePayloadV2,
        )

        d = dict(src_dict)
        schedule_sync_target = ScheduleSyncTargetCreatePayloadV2.from_dict(
            d.pop("schedule_sync_target")
        )

        schedule_sync_targets_create_payload_v2 = cls(
            schedule_sync_target=schedule_sync_target,
        )

        schedule_sync_targets_create_payload_v2.additional_properties = d
        return schedule_sync_targets_create_payload_v2

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
