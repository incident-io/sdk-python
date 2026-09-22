from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogScheduleOverrideMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogScheduleOverrideMetadataV2:
    """
    Example:
        {'after_user_ids': '01FCNDV6P870EA6S7TK1DSYDG2', 'after_user_names': 'Nicole C', 'before_user_ids':
            '01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG1', 'before_user_names': 'Nicole A,Nicole B', 'end_at':
            '2026-03-02T08:00:00Z', 'start_at': '2026-03-01T18:00:00Z'}

    Attributes:
        after_user_ids (str): User IDs of users on-call after the override change, comma separated Example:
            01FCNDV6P870EA6S7TK1DSYDG2.
        after_user_names (str): Names of users on-call after the override change, comma separated Example: Nicole C.
        before_user_ids (str): User IDs of users on-call before the override change, comma separated Example:
            01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG1.
        before_user_names (str): Names of users on-call before the override change, comma separated Example: Nicole
            A,Nicole B.
        end_at (str): Override end time in the schedule's local timezone Example: 2026-03-02T08:00:00Z.
        start_at (str): Override start time in the schedule's local timezone Example: 2026-03-01T18:00:00Z.
    """

    after_user_ids: str
    after_user_names: str
    before_user_ids: str
    before_user_names: str
    end_at: str
    start_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_user_ids = self.after_user_ids

        after_user_names = self.after_user_names

        before_user_ids = self.before_user_ids

        before_user_names = self.before_user_names

        end_at = self.end_at

        start_at = self.start_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_user_ids": after_user_ids,
                "after_user_names": after_user_names,
                "before_user_ids": before_user_ids,
                "before_user_names": before_user_names,
                "end_at": end_at,
                "start_at": start_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_user_ids = d.pop("after_user_ids")

        after_user_names = d.pop("after_user_names")

        before_user_ids = d.pop("before_user_ids")

        before_user_names = d.pop("before_user_names")

        end_at = d.pop("end_at")

        start_at = d.pop("start_at")

        audit_log_schedule_override_metadata_v2 = cls(
            after_user_ids=after_user_ids,
            after_user_names=after_user_names,
            before_user_ids=before_user_ids,
            before_user_names=before_user_names,
            end_at=end_at,
            start_at=start_at,
        )

        audit_log_schedule_override_metadata_v2.additional_properties = d
        return audit_log_schedule_override_metadata_v2

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
