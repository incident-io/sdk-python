from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_route_path_node_payload_v2_type import CallRoutePathNodePayloadV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_route_path_node_level_v2 import CallRoutePathNodeLevelV2
    from ..models.call_route_path_node_voicemail_v2 import CallRoutePathNodeVoicemailV2


T = TypeVar("T", bound="CallRoutePathNodePayloadV2")


@_attrs_define(kw_only=True)
class CallRoutePathNodePayloadV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'level': {'targets': [{'id': 'lawrencejones', 'schedule_mode':
            'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]},
            'type': 'level', 'voicemail': {'greeting_text': 'Sorry, no one is available to take your call. Please leave a
            message after the tone. This call will be recorded.'}}

    Attributes:
        type_ (CallRoutePathNodePayloadV2Type): The type of this node. Available types are:
            * level: page a set of targets, rotating between them
            * voicemail: record a message from the caller Example: level.
        id (str | Unset): Unique identifier for this node. Omit it and we'll generate one. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        level (CallRoutePathNodeLevelV2 | Unset): The targets a level pages.

            We call each target for 30 seconds, rotating to the next after 60 seconds, and
            move to the next node if nobody acknowledges within 5 minutes. Those timings are
            fixed for call routes. Example: {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}.
        voicemail (CallRoutePathNodeVoicemailV2 | Unset): Records a message from the caller, and enriches the resulting
            alert with the transcript. Example: {'greeting_text': 'Sorry, no one is available to take your call. Please
            leave a message after the tone. This call will be recorded.'}.
    """

    type_: CallRoutePathNodePayloadV2Type
    id: str | Unset = UNSET
    level: CallRoutePathNodeLevelV2 | Unset = UNSET
    voicemail: CallRoutePathNodeVoicemailV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        voicemail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voicemail, Unset):
            voicemail = self.voicemail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if voicemail is not UNSET:
            field_dict["voicemail"] = voicemail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_path_node_level_v2 import (
            CallRoutePathNodeLevelV2,
        )
        from ..models.call_route_path_node_voicemail_v2 import (
            CallRoutePathNodeVoicemailV2,
        )

        d = dict(src_dict)
        type_ = CallRoutePathNodePayloadV2Type(d.pop("type"))

        id = d.pop("id", UNSET)

        _level = d.pop("level", UNSET)
        level: CallRoutePathNodeLevelV2 | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = CallRoutePathNodeLevelV2.from_dict(_level)

        _voicemail = d.pop("voicemail", UNSET)
        voicemail: CallRoutePathNodeVoicemailV2 | Unset
        if isinstance(_voicemail, Unset):
            voicemail = UNSET
        else:
            voicemail = CallRoutePathNodeVoicemailV2.from_dict(_voicemail)

        call_route_path_node_payload_v2 = cls(
            type_=type_,
            id=id,
            level=level,
            voicemail=voicemail,
        )

        call_route_path_node_payload_v2.additional_properties = d
        return call_route_path_node_payload_v2

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
