from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_transcript_entry_v2_medium import CallTranscriptEntryV2Medium

T = TypeVar("T", bound="CallTranscriptEntryV2")


@_attrs_define
class CallTranscriptEntryV2:
    """A single entry of a Scribe call transcript: one contiguous run of
    speech, or one in-call chat message, from one participant.

        Example:
            {'content': 'I think we should roll back the deploy.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'medium': 'spoken',
                'participant_name': 'Alice Smith', 'timestamp': '2021-08-17T13:28:57.801578Z'}

        Attributes:
            content (str): What was said Example: I think we should roll back the deploy..
            id (str): Unique identifier for this transcript entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            medium (CallTranscriptEntryV2Medium): Whether this entry was spoken aloud or sent as an in-call chat message
                Example: spoken.
            participant_name (str): Name of the participant who spoke or sent the message, as reported by the call provider
                Example: Alice Smith.
            timestamp (datetime.datetime): When the participant started speaking Example: 2021-08-17T13:28:57.801578Z.
    """

    content: str
    id: str
    medium: CallTranscriptEntryV2Medium
    participant_name: str
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        id = self.id

        medium = self.medium.value

        participant_name = self.participant_name

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "id": id,
                "medium": medium,
                "participant_name": participant_name,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content = d.pop("content")

        id = d.pop("id")

        medium = CallTranscriptEntryV2Medium(d.pop("medium"))

        participant_name = d.pop("participant_name")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        call_transcript_entry_v2 = cls(
            content=content,
            id=id,
            medium=medium,
            participant_name=participant_name,
            timestamp=timestamp,
        )

        call_transcript_entry_v2.additional_properties = d
        return call_transcript_entry_v2

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
