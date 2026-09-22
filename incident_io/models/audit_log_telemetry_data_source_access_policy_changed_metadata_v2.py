from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTelemetryDataSourceAccessPolicyChangedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogTelemetryDataSourceAccessPolicyChangedMetadataV2:
    """
    Example:
        {'after': '{"read":{"enabled":true,"surfaces":{"chat":{"type":"deny"}}}}', 'before':
            '{"read":{"enabled":true,"surfaces":{"chat":{"type":"allow"}}}}', 'change_id': '01JD8ZQK9X0000000000000000',
            'set_by': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        after (str): The policy after the change, as JSON Example:
            {"read":{"enabled":true,"surfaces":{"chat":{"type":"deny"}}}}.
        before (str): The policy before the change, as JSON; empty when the connector had no access policy Example:
            {"read":{"enabled":true,"surfaces":{"chat":{"type":"allow"}}}}.
        change_id (str): Shared by every entry the same save produced, so the decision that changed and the access it
            reached can be read together Example: 01JD8ZQK9X0000000000000000.
        set_by (str | Unset): ID of the user who saved the policy, absent when staff tooling saved it Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    after: str
    before: str
    change_id: str
    set_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        change_id = self.change_id

        set_by = self.set_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "before": before,
                "change_id": change_id,
            }
        )
        if set_by is not UNSET:
            field_dict["set_by"] = set_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after = d.pop("after")

        before = d.pop("before")

        change_id = d.pop("change_id")

        set_by = d.pop("set_by", UNSET)

        audit_log_telemetry_data_source_access_policy_changed_metadata_v2 = cls(
            after=after,
            before=before,
            change_id=change_id,
            set_by=set_by,
        )

        audit_log_telemetry_data_source_access_policy_changed_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_access_policy_changed_metadata_v2

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
