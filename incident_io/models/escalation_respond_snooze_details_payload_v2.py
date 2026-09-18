from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationRespondSnoozeDetailsPayloadV2")


@_attrs_define
class EscalationRespondSnoozeDetailsPayloadV2:
    """
    Example:
        {'reason': 'Waiting for deployment to complete', 'snooze_until': '2025-01-01T12:00:00Z'}

    Attributes:
        snooze_until (datetime.datetime): The time at which the snooze should end Example: 2025-01-01T12:00:00Z.
        reason (str | Unset): Optional reason for snoozing the escalation Example: Waiting for deployment to complete.
    """

    snooze_until: datetime.datetime
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snooze_until = self.snooze_until.isoformat()

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snooze_until": snooze_until,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snooze_until = datetime.datetime.fromisoformat(d.pop("snooze_until"))

        reason = d.pop("reason", UNSET)

        escalation_respond_snooze_details_payload_v2 = cls(
            snooze_until=snooze_until,
            reason=reason,
        )

        escalation_respond_snooze_details_payload_v2.additional_properties = d
        return escalation_respond_snooze_details_payload_v2

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
