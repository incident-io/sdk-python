from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogMicrosoftEntraTenantLinkedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogMicrosoftEntraTenantLinkedMetadataV2:
    """
    Example:
        {'tenant_domain': 'acme.com', 'tenant_id': 'f339c180-eee9-4e7d-95eb-d19a69b9a922'}

    Attributes:
        tenant_domain (str | Unset): The email domain we verified the tenant owns Example: acme.com.
        tenant_id (str | Unset): The Microsoft Entra tenant that was linked Example:
            f339c180-eee9-4e7d-95eb-d19a69b9a922.
    """

    tenant_domain: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_domain = self.tenant_domain

        tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_domain is not UNSET:
            field_dict["tenant_domain"] = tenant_domain
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tenant_domain = d.pop("tenant_domain", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        audit_log_microsoft_entra_tenant_linked_metadata_v2 = cls(
            tenant_domain=tenant_domain,
            tenant_id=tenant_id,
        )

        audit_log_microsoft_entra_tenant_linked_metadata_v2.additional_properties = d
        return audit_log_microsoft_entra_tenant_linked_metadata_v2

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
