from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnCallNotificationPauseV2")


@_attrs_define(kw_only=True)
class OnCallNotificationPauseV2:
    """A window in which a user's on-call notifications are paused: while it's active, escalations skip the user instead of
    paging them.

        Example:
            {'created_at': '2021-08-17T13:28:57.801578Z', 'ends_at': '2021-08-24T13:28:57.801578Z', 'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'reason': 'Annual leave', 'starts_at': '2021-08-17T13:28:57.801578Z',
                'updated_at': '2021-08-17T13:28:57.801578Z', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

        Attributes:
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            ends_at (datetime.datetime): When notifications resume Example: 2021-08-24T13:28:57.801578Z.
            id (str): Unique identifier for this notification pause Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            starts_at (datetime.datetime): When notifications stop being sent to the user Example:
                2021-08-17T13:28:57.801578Z.
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            user_id (str): The user whose on-call notifications are paused in this time window Example:
                01FCNDV6P870EA6S7TK1DSYDG0.
            reason (str | Unset): Free text reason for why notifications are paused, shown to teammates Example: Annual
                leave.
    """

    created_at: datetime.datetime
    ends_at: datetime.datetime
    id: str
    starts_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: str
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        ends_at = self.ends_at.isoformat()

        id = self.id

        starts_at = self.starts_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "ends_at": ends_at,
                "id": id,
                "starts_at": starts_at,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        id = d.pop("id")

        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_id = d.pop("user_id")

        reason = d.pop("reason", UNSET)

        on_call_notification_pause_v2 = cls(
            created_at=created_at,
            ends_at=ends_at,
            id=id,
            starts_at=starts_at,
            updated_at=updated_at,
            user_id=user_id,
            reason=reason,
        )

        on_call_notification_pause_v2.additional_properties = d
        return on_call_notification_pause_v2

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
