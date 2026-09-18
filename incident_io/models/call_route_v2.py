from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_route_v2_current_state import CallRouteV2CurrentState
from ..models.call_route_v2_custom_language import CallRouteV2CustomLanguage
from ..models.call_route_v2_phone_number_type import CallRouteV2PhoneNumberType
from ..models.call_route_v2_responder_caller_id import CallRouteV2ResponderCallerId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_route_allowed_caller_v2 import CallRouteAllowedCallerV2
    from ..models.call_route_option_v2 import CallRouteOptionV2
    from ..models.call_route_path_node_v2 import CallRoutePathNodeV2


T = TypeVar("T", bound="CallRouteV2")


@_attrs_define
class CallRouteV2:
    """A call route is a phone number your customers can call to reach whoever is
    on call, for an urgent support line or a regulator hotline.

    When a call comes in we work down the route's path, ringing each level's targets
    in turn until someone answers, then connect them to the caller. A trailing
    voicemail node records a message instead. Every call raises an alert, so calls
    can open incidents through an alert route.

    List and edit call routes here. Create and delete them in the dashboard.

        Example:
            {'allowed_callers': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk', 'phone_number':
                '+15551234567'}], 'country_code': 'US', 'created_at': '2021-08-17T13:28:57.801578Z', 'current_state': 'active',
                'custom_language': 'en-US', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator urgent request', 'options':
                [{'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level':
                {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail':
                {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
                call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}], 'path': [{'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
                'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
                'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
                message after the tone. This call will be recorded.'}}], 'phone_number': '+15551234567', 'phone_number_type':
                'toll_free', 'responder_caller_id': 'route_number', 'updated_at': '2021-08-17T13:28:57.801578Z',
                'use_caller_allowlist': True}

        Attributes:
            allowed_callers (list[CallRouteAllowedCallerV2]): The numbers allowed to call this route. Only enforced when
                use_caller_allowlist is true. Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk',
                'phone_number': '+15551234567'}].
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            current_state (CallRouteV2CurrentState): Where this route is in provisioning. Only an active route answers
                calls:
                * pending: created, and awaiting manual work from us
                * pending_regulatory_information: awaiting regulatory compliance information, collected in the dashboard
                * pending_number: compliance is settled, and we're provisioning a number
                * active: fully provisioned, and answering calls Example: active.
            custom_language (CallRouteV2CustomLanguage): The language we speak voice prompts in, via text-to-speech Example:
                en-US.
            id (str): Unique identifier for this call route Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            name (str): Name for this call route Example: Regulator urgent request.
            options (list[CallRouteOptionV2]): The phone-tree menu this route presents. Empty when callers are routed down
                the route's path. Example: [{'digit': '1', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'path': [{'id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
                'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
                'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
                message after the tone. This call will be recorded.'}}], 'prompt': 'For an urgent production outage, press 1'}].
            path (list[CallRoutePathNodeV2]): Who we page when a call comes in. Empty when this route presents a phone-tree
                menu, in which case each menu option carries its own path. Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail':
                {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
                call will be recorded.'}}].
            responder_caller_id (CallRouteV2ResponderCallerId): Which number responders see when we call them:
                * route_number: this route's own number
                * oncall_number: an incident.io on-call number Example: route_number.
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            use_caller_allowlist (bool): Whether this route only answers calls from its allowed callers Example: True.
            country_code (str | Unset): The country this route's number belongs to Example: US.
            phone_number (str | Unset): The number your customers call to reach this route, once one has been provisioned
                Example: +15551234567.
            phone_number_type (CallRouteV2PhoneNumberType | Unset): The type of phone number, which determines the
                regulatory requirements for provisioning it Example: toll_free.
    """

    allowed_callers: list[CallRouteAllowedCallerV2]
    created_at: datetime.datetime
    current_state: CallRouteV2CurrentState
    custom_language: CallRouteV2CustomLanguage
    id: str
    name: str
    options: list[CallRouteOptionV2]
    path: list[CallRoutePathNodeV2]
    responder_caller_id: CallRouteV2ResponderCallerId
    updated_at: datetime.datetime
    use_caller_allowlist: bool
    country_code: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    phone_number_type: CallRouteV2PhoneNumberType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_callers = []
        for allowed_callers_item_data in self.allowed_callers:
            allowed_callers_item = allowed_callers_item_data.to_dict()
            allowed_callers.append(allowed_callers_item)

        created_at = self.created_at.isoformat()

        current_state = self.current_state.value

        custom_language = self.custom_language.value

        id = self.id

        name = self.name

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        responder_caller_id = self.responder_caller_id.value

        updated_at = self.updated_at.isoformat()

        use_caller_allowlist = self.use_caller_allowlist

        country_code = self.country_code

        phone_number = self.phone_number

        phone_number_type: str | Unset = UNSET
        if not isinstance(self.phone_number_type, Unset):
            phone_number_type = self.phone_number_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_callers": allowed_callers,
                "created_at": created_at,
                "current_state": current_state,
                "custom_language": custom_language,
                "id": id,
                "name": name,
                "options": options,
                "path": path,
                "responder_caller_id": responder_caller_id,
                "updated_at": updated_at,
                "use_caller_allowlist": use_caller_allowlist,
            }
        )
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if phone_number_type is not UNSET:
            field_dict["phone_number_type"] = phone_number_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_allowed_caller_v2 import (
            CallRouteAllowedCallerV2,
        )
        from ..models.call_route_option_v2 import CallRouteOptionV2
        from ..models.call_route_path_node_v2 import (
            CallRoutePathNodeV2,
        )

        d = dict(src_dict)
        allowed_callers = []
        _allowed_callers = d.pop("allowed_callers")
        for allowed_callers_item_data in _allowed_callers:
            allowed_callers_item = CallRouteAllowedCallerV2.from_dict(
                allowed_callers_item_data
            )

            allowed_callers.append(allowed_callers_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        current_state = CallRouteV2CurrentState(d.pop("current_state"))

        custom_language = CallRouteV2CustomLanguage(d.pop("custom_language"))

        id = d.pop("id")

        name = d.pop("name")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CallRouteOptionV2.from_dict(options_item_data)

            options.append(options_item)

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = CallRoutePathNodeV2.from_dict(path_item_data)

            path.append(path_item)

        responder_caller_id = CallRouteV2ResponderCallerId(d.pop("responder_caller_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        use_caller_allowlist = d.pop("use_caller_allowlist")

        country_code = d.pop("country_code", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        _phone_number_type = d.pop("phone_number_type", UNSET)
        phone_number_type: CallRouteV2PhoneNumberType | Unset
        if isinstance(_phone_number_type, Unset):
            phone_number_type = UNSET
        else:
            phone_number_type = CallRouteV2PhoneNumberType(_phone_number_type)

        call_route_v2 = cls(
            allowed_callers=allowed_callers,
            created_at=created_at,
            current_state=current_state,
            custom_language=custom_language,
            id=id,
            name=name,
            options=options,
            path=path,
            responder_caller_id=responder_caller_id,
            updated_at=updated_at,
            use_caller_allowlist=use_caller_allowlist,
            country_code=country_code,
            phone_number=phone_number,
            phone_number_type=phone_number_type,
        )

        call_route_v2.additional_properties = d
        return call_route_v2

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
