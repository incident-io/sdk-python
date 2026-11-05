from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogTelemetryDataSourceAccessInheritanceChangedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogTelemetryDataSourceAccessInheritanceChangedMetadataV2:
    """
    Example:
        {'inherits_access': 'true'}

    Attributes:
        inherits_access (str): Whether the data source takes its access mode and teams from its parent after the change
            (true, false) Example: true.
    """

    inherits_access: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inherits_access = self.inherits_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inherits_access": inherits_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        inherits_access = d.pop("inherits_access")

        audit_log_telemetry_data_source_access_inheritance_changed_metadata_v2 = cls(
            inherits_access=inherits_access,
        )

        audit_log_telemetry_data_source_access_inheritance_changed_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_access_inheritance_changed_metadata_v2

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
