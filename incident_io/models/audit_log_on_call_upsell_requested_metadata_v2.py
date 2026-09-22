from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogOnCallUpsellRequestedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogOnCallUpsellRequestedMetadataV2:
    """
    Example:
        {'gate_count_after': '15', 'gate_count_before': '10', 'requested_by_user_id': '01JV9EMFCFRGCFVNDWTBKT2EBR',
            'seats_added': '5'}

    Attributes:
        gate_count_after (str): The on-call seat allowance after the upsell Example: 15.
        gate_count_before (str): The on-call seat allowance before the upsell Example: 10.
        requested_by_user_id (str): The ID of the user who requested the upsell Example: 01JV9EMFCFRGCFVNDWTBKT2EBR.
        seats_added (str): The number of on-call seats added by this upsell Example: 5.
    """

    gate_count_after: str
    gate_count_before: str
    requested_by_user_id: str
    seats_added: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gate_count_after = self.gate_count_after

        gate_count_before = self.gate_count_before

        requested_by_user_id = self.requested_by_user_id

        seats_added = self.seats_added

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gate_count_after": gate_count_after,
                "gate_count_before": gate_count_before,
                "requested_by_user_id": requested_by_user_id,
                "seats_added": seats_added,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gate_count_after = d.pop("gate_count_after")

        gate_count_before = d.pop("gate_count_before")

        requested_by_user_id = d.pop("requested_by_user_id")

        seats_added = d.pop("seats_added")

        audit_log_on_call_upsell_requested_metadata_v2 = cls(
            gate_count_after=gate_count_after,
            gate_count_before=gate_count_before,
            requested_by_user_id=requested_by_user_id,
            seats_added=seats_added,
        )

        audit_log_on_call_upsell_requested_metadata_v2.additional_properties = d
        return audit_log_on_call_upsell_requested_metadata_v2

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
