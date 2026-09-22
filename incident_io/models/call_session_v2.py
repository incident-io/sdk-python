from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallSessionV2")


@_attrs_define(kw_only=True)
class CallSessionV2:
    """A call session is a single occurrence of a call that Scribe attended,
    for example one Zoom or Google Meet meeting. Several call sessions can exist for
    the same context: one for each time a call was started.

    Use the Call Transcript Entries endpoint to page through what Scribe transcribed
    during a session.

        Example:
            {'ended_at': '2021-08-17T14:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
                '01G0J1EXE7AXZ2C93K61WBPYEH', 'started_at': '2021-08-17T13:28:57.801578Z'}

        Attributes:
            id (str): Unique identifier for this call session Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            incident_id (str): The incident this call session belongs to Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            started_at (datetime.datetime): When the call session started Example: 2021-08-17T13:28:57.801578Z.
            ended_at (datetime.datetime | Unset): When the call session ended. Absent while the call is still in progress.
                Example: 2021-08-17T14:28:57.801578Z.
    """

    id: str
    incident_id: str
    started_at: datetime.datetime
    ended_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        incident_id = self.incident_id

        started_at = self.started_at.isoformat()

        ended_at: str | Unset = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "incident_id": incident_id,
                "started_at": started_at,
            }
        )
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        incident_id = d.pop("incident_id")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        _ended_at = d.pop("ended_at", UNSET)
        ended_at: datetime.datetime | Unset
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = datetime.datetime.fromisoformat(_ended_at)

        call_session_v2 = cls(
            id=id,
            incident_id=incident_id,
            started_at=started_at,
            ended_at=ended_at,
        )

        call_session_v2.additional_properties = d
        return call_session_v2

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
