from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogPolicyMetadataV2")


@_attrs_define
class AuditLogPolicyMetadataV2:
    """
    Example:
        {'run_on_private_incidents': 'true'}

    Attributes:
        run_on_private_incidents (str | Unset): Whether the policy evaluates private incidents Example: true.
    """

    run_on_private_incidents: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_on_private_incidents = self.run_on_private_incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_on_private_incidents is not UNSET:
            field_dict["run_on_private_incidents"] = run_on_private_incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        run_on_private_incidents = d.pop("run_on_private_incidents", UNSET)

        audit_log_policy_metadata_v2 = cls(
            run_on_private_incidents=run_on_private_incidents,
        )

        audit_log_policy_metadata_v2.additional_properties = d
        return audit_log_policy_metadata_v2

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
