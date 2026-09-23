from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogTwilioConnectionMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogTwilioConnectionMetadataV2:
    """
    Example:
        {'account_sid': 'AC11111111111111111111111111111111'}

    Attributes:
        account_sid (str): The Twilio account SID for the connection Example: AC11111111111111111111111111111111.
    """

    account_sid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_sid = self.account_sid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_sid": account_sid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account_sid = d.pop("account_sid")

        audit_log_twilio_connection_metadata_v2 = cls(
            account_sid=account_sid,
        )

        audit_log_twilio_connection_metadata_v2.additional_properties = d
        return audit_log_twilio_connection_metadata_v2

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
