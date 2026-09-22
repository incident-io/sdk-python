from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_route_v2 import CallRouteV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="CallRoutesListResultV2")


@_attrs_define(kw_only=True)
class CallRoutesListResultV2:
    """
    Example:
        {'call_routes': [{'allowed_callers': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk',
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
            'use_caller_allowlist': True}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        call_routes (list[CallRouteV2]):  Example: [{'allowed_callers': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Regulator duty desk', 'phone_number': '+15551234567'}], 'country_code': 'US', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'current_state': 'active', 'custom_language': 'en-US', 'id':
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
            '2021-08-17T13:28:57.801578Z', 'use_caller_allowlist': True}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    call_routes: list[CallRouteV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_routes = []
        for call_routes_item_data in self.call_routes:
            call_routes_item = call_routes_item_data.to_dict()
            call_routes.append(call_routes_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_routes": call_routes,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_v2 import CallRouteV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        call_routes = []
        _call_routes = d.pop("call_routes")
        for call_routes_item_data in _call_routes:
            call_routes_item = CallRouteV2.from_dict(call_routes_item_data)

            call_routes.append(call_routes_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        call_routes_list_result_v2 = cls(
            call_routes=call_routes,
            pagination_meta=pagination_meta,
        )

        call_routes_list_result_v2.additional_properties = d
        return call_routes_list_result_v2

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
