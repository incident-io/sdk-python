from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalations_respond_escalation_payload_v2_response import (
    EscalationsRespondEscalationPayloadV2Response,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_respond_snooze_details_payload_v2 import (
        EscalationRespondSnoozeDetailsPayloadV2,
    )


T = TypeVar("T", bound="EscalationsRespondEscalationPayloadV2")


@_attrs_define
class EscalationsRespondEscalationPayloadV2:
    """
    Example:
        {'response': 'ack', 'snooze_details': {'reason': 'Waiting for deployment to complete', 'snooze_until':
            '2025-01-01T12:00:00Z'}}

    Attributes:
        response (EscalationsRespondEscalationPayloadV2Response): Whether to acknowledge, decline or snooze the
            escalation Example: ack.
        snooze_details (EscalationRespondSnoozeDetailsPayloadV2 | Unset):  Example: {'reason': 'Waiting for deployment
            to complete', 'snooze_until': '2025-01-01T12:00:00Z'}.
    """

    response: EscalationsRespondEscalationPayloadV2Response
    snooze_details: EscalationRespondSnoozeDetailsPayloadV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response.value

        snooze_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snooze_details, Unset):
            snooze_details = self.snooze_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
            }
        )
        if snooze_details is not UNSET:
            field_dict["snooze_details"] = snooze_details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_respond_snooze_details_payload_v2 import (
            EscalationRespondSnoozeDetailsPayloadV2,
        )

        d = dict(src_dict)
        response = EscalationsRespondEscalationPayloadV2Response(d.pop("response"))

        _snooze_details = d.pop("snooze_details", UNSET)
        snooze_details: EscalationRespondSnoozeDetailsPayloadV2 | Unset
        if isinstance(_snooze_details, Unset):
            snooze_details = UNSET
        else:
            snooze_details = EscalationRespondSnoozeDetailsPayloadV2.from_dict(
                _snooze_details
            )

        escalations_respond_escalation_payload_v2 = cls(
            response=response,
            snooze_details=snooze_details,
        )

        escalations_respond_escalation_payload_v2.additional_properties = d
        return escalations_respond_escalation_payload_v2

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
