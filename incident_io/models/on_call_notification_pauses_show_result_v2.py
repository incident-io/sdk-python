from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.on_call_notification_pause_v2 import OnCallNotificationPauseV2


T = TypeVar("T", bound="OnCallNotificationPausesShowResultV2")


@_attrs_define(kw_only=True)
class OnCallNotificationPausesShowResultV2:
    """
    Example:
        {'on_call_notification_pause': {'created_at': '2021-08-17T13:28:57.801578Z', 'ends_at':
            '2021-08-24T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'reason': 'Annual leave', 'starts_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}}

    Attributes:
        on_call_notification_pause (OnCallNotificationPauseV2): A window in which a user's on-call notifications are
            paused: while it's active, escalations skip the user instead of paging them. Example: {'created_at':
            '2021-08-17T13:28:57.801578Z', 'ends_at': '2021-08-24T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'reason': 'Annual leave', 'starts_at': '2021-08-17T13:28:57.801578Z', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    on_call_notification_pause: OnCallNotificationPauseV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_call_notification_pause = self.on_call_notification_pause.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "on_call_notification_pause": on_call_notification_pause,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.on_call_notification_pause_v2 import (
            OnCallNotificationPauseV2,
        )

        d = dict(src_dict)
        on_call_notification_pause = OnCallNotificationPauseV2.from_dict(
            d.pop("on_call_notification_pause")
        )

        on_call_notification_pauses_show_result_v2 = cls(
            on_call_notification_pause=on_call_notification_pause,
        )

        on_call_notification_pauses_show_result_v2.additional_properties = d
        return on_call_notification_pauses_show_result_v2

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
