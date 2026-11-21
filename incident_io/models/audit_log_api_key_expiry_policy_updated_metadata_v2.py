from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogAPIKeyExpiryPolicyUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogAPIKeyExpiryPolicyUpdatedMetadataV2:
    """
    Example:
        {'expiry_required': 'true', 'max_lifetime_days': '90'}

    Attributes:
        expiry_required (str): Whether new API keys must have an expiry after the update Example: true.
        max_lifetime_days (str | Unset): The longest lifetime, in days, a new key may have after the update. Absent when
            there is no limit. Example: 90.
    """

    expiry_required: str
    max_lifetime_days: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_required = self.expiry_required

        max_lifetime_days = self.max_lifetime_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiry_required": expiry_required,
            }
        )
        if max_lifetime_days is not UNSET:
            field_dict["max_lifetime_days"] = max_lifetime_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        expiry_required = d.pop("expiry_required")

        max_lifetime_days = d.pop("max_lifetime_days", UNSET)

        audit_log_api_key_expiry_policy_updated_metadata_v2 = cls(
            expiry_required=expiry_required,
            max_lifetime_days=max_lifetime_days,
        )

        audit_log_api_key_expiry_policy_updated_metadata_v2.additional_properties = d
        return audit_log_api_key_expiry_policy_updated_metadata_v2

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
