from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_route_option_v2_digit import CallRouteOptionV2Digit

if TYPE_CHECKING:
    from ..models.call_route_path_node_v2 import CallRoutePathNodeV2


T = TypeVar("T", bound="CallRouteOptionV2")


@_attrs_define
class CallRouteOptionV2:
    """One entry in a call route's phone-tree menu: the digit a caller presses, the
    prompt we read out to offer it, and who we page when they choose it.

        Example:
            {'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level':
                {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail':
                {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
                call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}

        Attributes:
            digit (CallRouteOptionV2Digit): The keypad digit a caller presses to choose this option Example: 1.
            id (str): Unique identifier for this option Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            path (list[CallRoutePathNodeV2]): Who we page when a caller chooses this option Example: [{'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
                'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
                'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
                message after the tone. This call will be recorded.'}}].
            prompt (str): What we read out to offer this option, via text-to-speech in the route's language, exactly as
                written Example: For an urgent production outage, press 1.
    """

    digit: CallRouteOptionV2Digit
    id: str
    path: list[CallRoutePathNodeV2]
    prompt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digit = self.digit.value

        id = self.id

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        prompt = self.prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "digit": digit,
                "id": id,
                "path": path,
                "prompt": prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_path_node_v2 import (
            CallRoutePathNodeV2,
        )

        d = dict(src_dict)
        digit = CallRouteOptionV2Digit(d.pop("digit"))

        id = d.pop("id")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = CallRoutePathNodeV2.from_dict(path_item_data)

            path.append(path_item)

        prompt = d.pop("prompt")

        call_route_option_v2 = cls(
            digit=digit,
            id=id,
            path=path,
            prompt=prompt,
        )

        call_route_option_v2.additional_properties = d
        return call_route_option_v2

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
