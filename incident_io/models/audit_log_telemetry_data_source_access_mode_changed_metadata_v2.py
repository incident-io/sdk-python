from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogTelemetryDataSourceAccessModeChangedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogTelemetryDataSourceAccessModeChangedMetadataV2:
    """
    Example:
        {'from': 'default', 'to': 'restricted'}

    Attributes:
        from_ (str): The access mode before the change Example: default.
        to (str): The access mode after the change Example: restricted.
    """

    from_: str
    to: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        audit_log_telemetry_data_source_access_mode_changed_metadata_v2 = cls(
            from_=from_,
            to=to,
        )

        audit_log_telemetry_data_source_access_mode_changed_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_access_mode_changed_metadata_v2

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
