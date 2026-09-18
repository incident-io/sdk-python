from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_route_v2 import CallRouteV2


T = TypeVar("T", bound="CallRoutesShowResultV2")


@_attrs_define
class CallRoutesShowResultV2:
    """
    Example:
        {'call_route': {'allowed_callers': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk',
            'phone_number': '+15551234567'}], 'country_code': 'US', 'created_at': '2021-08-17T13:28:57.801578Z',
            'current_state': 'active', 'custom_language': 'en-US', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator
            urgent request', 'options': [{'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
            'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
            message after the tone. This call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}],
            'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
            'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
            message after the tone. This call will be recorded.'}}], 'phone_number': '+15551234567', 'phone_number_type':
            'toll_free', 'responder_caller_id': 'route_number', 'updated_at': '2021-08-17T13:28:57.801578Z',
            'use_caller_allowlist': True}}

    Attributes:
        call_route (CallRouteV2): A call route is a phone number your customers can call to reach whoever is
            on call, for an urgent support line or a regulator hotline.

            When a call comes in we work down the route's path, ringing each level's targets
            in turn until someone answers, then connect them to the caller. A trailing
            voicemail node records a message instead. Every call raises an alert, so calls
            can open incidents through an alert route.

            List and edit call routes here. Create and delete them in the dashboard. Example: {'allowed_callers': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk', 'phone_number': '+15551234567'}], 'country_code':
            'US', 'created_at': '2021-08-17T13:28:57.801578Z', 'current_state': 'active', 'custom_language': 'en-US', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator urgent request', 'options': [{'digit': '1', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to
            take your call. Please leave a message after the tone. This call will be recorded.'}}], 'prompt': 'For an urgent
            production outage, press 1'}], 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to
            take your call. Please leave a message after the tone. This call will be recorded.'}}], 'phone_number':
            '+15551234567', 'phone_number_type': 'toll_free', 'responder_caller_id': 'route_number', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'use_caller_allowlist': True}.
    """

    call_route: CallRouteV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_route = self.call_route.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_route": call_route,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_v2 import CallRouteV2

        d = dict(src_dict)
        call_route = CallRouteV2.from_dict(d.pop("call_route"))

        call_routes_show_result_v2 = cls(
            call_route=call_route,
        )

        call_routes_show_result_v2.additional_properties = d
        return call_routes_show_result_v2

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
