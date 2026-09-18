from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_route_option_v2 import CallRouteOptionV2


T = TypeVar("T", bound="CallRoutesListOptionsResultV2")


@_attrs_define
class CallRoutesListOptionsResultV2:
    """
    Example:
        {'options': [{'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail':
            {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}]}

    Attributes:
        options (list[CallRouteOptionV2]):  Example: [{'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
            'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
            message after the tone. This call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}].
    """

    options: list[CallRouteOptionV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_option_v2 import CallRouteOptionV2

        d = dict(src_dict)
        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CallRouteOptionV2.from_dict(options_item_data)

            options.append(options_item)

        call_routes_list_options_result_v2 = cls(
            options=options,
        )

        call_routes_list_options_result_v2.additional_properties = d
        return call_routes_list_options_result_v2

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
