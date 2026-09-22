from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_routes_update_payload_v2_custom_language import (
    CallRoutesUpdatePayloadV2CustomLanguage,
)
from ..models.call_routes_update_payload_v2_responder_caller_id import (
    CallRoutesUpdatePayloadV2ResponderCallerId,
)

if TYPE_CHECKING:
    from ..models.call_route_path_node_payload_v2 import CallRoutePathNodePayloadV2


T = TypeVar("T", bound="CallRoutesUpdatePayloadV2")


@_attrs_define(kw_only=True)
class CallRoutesUpdatePayloadV2:
    """
    Example:
        {'custom_language': 'en-US', 'name': 'Regulator urgent request', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail':
            {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}}], 'responder_caller_id': 'route_number', 'use_caller_allowlist': True}

    Attributes:
        custom_language (CallRoutesUpdatePayloadV2CustomLanguage): The language we speak voice prompts in, via text-to-
            speech Example: en-US.
        name (str): Name for this call route Example: Regulator urgent request.
        path (list[CallRoutePathNodePayloadV2]): Who to page when a call comes in. Retires any phone-tree menu on the
            route; send an empty list to keep the menu. Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}]}, 'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is
            available to take your call. Please leave a message after the tone. This call will be recorded.'}}].
        responder_caller_id (CallRoutesUpdatePayloadV2ResponderCallerId): Which number responders see when we call them:
            * route_number: this route's own number
            * oncall_number: an incident.io on-call number Example: route_number.
        use_caller_allowlist (bool): Whether to only answer calls from this route's allowed callers. Needs at least one
            allowed caller. Example: True.
    """

    custom_language: CallRoutesUpdatePayloadV2CustomLanguage
    name: str
    path: list[CallRoutePathNodePayloadV2]
    responder_caller_id: CallRoutesUpdatePayloadV2ResponderCallerId
    use_caller_allowlist: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_language = self.custom_language.value

        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        responder_caller_id = self.responder_caller_id.value

        use_caller_allowlist = self.use_caller_allowlist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_language": custom_language,
                "name": name,
                "path": path,
                "responder_caller_id": responder_caller_id,
                "use_caller_allowlist": use_caller_allowlist,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_path_node_payload_v2 import (
            CallRoutePathNodePayloadV2,
        )

        d = dict(src_dict)
        custom_language = CallRoutesUpdatePayloadV2CustomLanguage(
            d.pop("custom_language")
        )

        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = CallRoutePathNodePayloadV2.from_dict(path_item_data)

            path.append(path_item)

        responder_caller_id = CallRoutesUpdatePayloadV2ResponderCallerId(
            d.pop("responder_caller_id")
        )

        use_caller_allowlist = d.pop("use_caller_allowlist")

        call_routes_update_payload_v2 = cls(
            custom_language=custom_language,
            name=name,
            path=path,
            responder_caller_id=responder_caller_id,
            use_caller_allowlist=use_caller_allowlist,
        )

        call_routes_update_payload_v2.additional_properties = d
        return call_routes_update_payload_v2

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
