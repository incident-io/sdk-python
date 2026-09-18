from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CallRoutePathNodeVoicemailV2")


@_attrs_define
class CallRoutePathNodeVoicemailV2:
    """Records a message from the caller, and enriches the resulting alert with the transcript.

    Example:
        {'greeting_text': 'Sorry, no one is available to take your call. Please leave a message after the tone. This
            call will be recorded.'}

    Attributes:
        greeting_text (str): What we read to the caller before recording, via text-to-speech in the route's language,
            exactly as written Example: Sorry, no one is available to take your call. Please leave a message after the tone.
            This call will be recorded..
    """

    greeting_text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        greeting_text = self.greeting_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "greeting_text": greeting_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        greeting_text = d.pop("greeting_text")

        call_route_path_node_voicemail_v2 = cls(
            greeting_text=greeting_text,
        )

        call_route_path_node_voicemail_v2.additional_properties = d
        return call_route_path_node_voicemail_v2

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
