from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_user_response_options_v2_available_actions_item import (
    EscalationUserResponseOptionsV2AvailableActionsItem,
)

T = TypeVar("T", bound="EscalationUserResponseOptionsV2")


@_attrs_define
class EscalationUserResponseOptionsV2:
    """
    Example:
        {'available_actions': ['ack', 'nack', 'snooze'], 'user_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        available_actions (list[EscalationUserResponseOptionsV2AvailableActionsItem]): The response actions this user
            can currently take on the escalation. Empty if the user can't respond to it at all. Example: ['ack', 'nack',
            'snooze'].
        user_id (str): The ID of the user these response options are for Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    available_actions: list[EscalationUserResponseOptionsV2AvailableActionsItem]
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_actions = []
        for available_actions_item_data in self.available_actions:
            available_actions_item = available_actions_item_data.value
            available_actions.append(available_actions_item)

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_actions": available_actions,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_actions = []
        _available_actions = d.pop("available_actions")
        for available_actions_item_data in _available_actions:
            available_actions_item = (
                EscalationUserResponseOptionsV2AvailableActionsItem(
                    available_actions_item_data
                )
            )

            available_actions.append(available_actions_item)

        user_id = d.pop("user_id")

        escalation_user_response_options_v2 = cls(
            available_actions=available_actions,
            user_id=user_id,
        )

        escalation_user_response_options_v2.additional_properties = d
        return escalation_user_response_options_v2

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
