from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogOnCallNotificationPauseMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogOnCallNotificationPauseMetadataV2:
    """
    Example:
        {'before_ends_at': '2021-08-17T13:28:57Z', 'before_reason': 'Sick leave', 'before_starts_at':
            '2021-08-10T13:28:57Z', 'ends_at': '2021-08-24T13:28:57Z', 'reason': 'Annual leave', 'starts_at':
            '2021-08-17T13:28:57Z'}

    Attributes:
        ends_at (str): When the notification pause ends Example: 2021-08-24T13:28:57Z.
        reason (str): Why notifications are paused. Empty when no reason was given Example: Annual leave.
        starts_at (str): When the notification pause starts Example: 2021-08-17T13:28:57Z.
        before_ends_at (str | Unset): When the pause ended before this update. Set on update entries only Example:
            2021-08-17T13:28:57Z.
        before_reason (str | Unset): Why notifications were paused before this update. Set on update entries only. Empty
            when no reason was given Example: Sick leave.
        before_starts_at (str | Unset): When the pause started before this update. Set on update entries only Example:
            2021-08-10T13:28:57Z.
    """

    ends_at: str
    reason: str
    starts_at: str
    before_ends_at: str | Unset = UNSET
    before_reason: str | Unset = UNSET
    before_starts_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ends_at = self.ends_at

        reason = self.reason

        starts_at = self.starts_at

        before_ends_at = self.before_ends_at

        before_reason = self.before_reason

        before_starts_at = self.before_starts_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ends_at": ends_at,
                "reason": reason,
                "starts_at": starts_at,
            }
        )
        if before_ends_at is not UNSET:
            field_dict["before_ends_at"] = before_ends_at
        if before_reason is not UNSET:
            field_dict["before_reason"] = before_reason
        if before_starts_at is not UNSET:
            field_dict["before_starts_at"] = before_starts_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ends_at = d.pop("ends_at")

        reason = d.pop("reason")

        starts_at = d.pop("starts_at")

        before_ends_at = d.pop("before_ends_at", UNSET)

        before_reason = d.pop("before_reason", UNSET)

        before_starts_at = d.pop("before_starts_at", UNSET)

        audit_log_on_call_notification_pause_metadata_v2 = cls(
            ends_at=ends_at,
            reason=reason,
            starts_at=starts_at,
            before_ends_at=before_ends_at,
            before_reason=before_reason,
            before_starts_at=before_starts_at,
        )

        audit_log_on_call_notification_pause_metadata_v2.additional_properties = d
        return audit_log_on_call_notification_pause_metadata_v2

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
