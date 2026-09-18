from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_event_v2_event import EscalationEventV2Event
from ..models.escalation_event_v2_urgency import EscalationEventV2Urgency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_channel_slim_v2 import ChatChannelSlimV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="EscalationEventV2")


@_attrs_define
class EscalationEventV2:
    """
    Example:
        {'channels': [{'microsoft_teams_channel_id': 'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id':
            'abc123', 'slack_team_id': 'abc123'}], 'event': 'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'occurred_at': '2021-08-17T13:28:57.801578Z', 'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}

    Attributes:
        event (EscalationEventV2Event): The type of event that occured. Example: entered_grace_period.
        id (str): The unique ID for this escalation event Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        occurred_at (datetime.datetime): The time when this escalation event was processed Example:
            2021-08-17T13:28:57.801578Z.
        channels (list[ChatChannelSlimV2] | Unset): This field will be populated for notified_channels events. Example:
            [{'microsoft_teams_channel_id': 'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123',
            'slack_team_id': 'abc123'}].
        urgency (EscalationEventV2Urgency | Unset): The urgency at which we tried to notify users. This field will be
            populated for notified_users events. Example: high.
        users (list[UserV2] | Unset): This field will be populated for notified_users and acked events. Example:
            [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}].
    """

    event: EscalationEventV2Event
    id: str
    occurred_at: datetime.datetime
    channels: list[ChatChannelSlimV2] | Unset = UNSET
    urgency: EscalationEventV2Urgency | Unset = UNSET
    users: list[UserV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event.value

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        urgency: str | Unset = UNSET
        if not isinstance(self.urgency, Unset):
            urgency = self.urgency.value

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "id": id,
                "occurred_at": occurred_at,
            }
        )
        if channels is not UNSET:
            field_dict["channels"] = channels
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.chat_channel_slim_v2 import ChatChannelSlimV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        event = EscalationEventV2Event(d.pop("event"))

        id = d.pop("id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        _channels = d.pop("channels", UNSET)
        channels: list[ChatChannelSlimV2] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ChatChannelSlimV2.from_dict(channels_item_data)

                channels.append(channels_item)

        _urgency = d.pop("urgency", UNSET)
        urgency: EscalationEventV2Urgency | Unset
        if isinstance(_urgency, Unset):
            urgency = UNSET
        else:
            urgency = EscalationEventV2Urgency(_urgency)

        _users = d.pop("users", UNSET)
        users: list[UserV2] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserV2.from_dict(users_item_data)

                users.append(users_item)

        escalation_event_v2 = cls(
            event=event,
            id=id,
            occurred_at=occurred_at,
            channels=channels,
            urgency=urgency,
            users=users,
        )

        escalation_event_v2.additional_properties = d
        return escalation_event_v2

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
