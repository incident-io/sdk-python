from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTelemetryDataSourceQueriedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogTelemetryDataSourceQueriedMetadataV2:
    """
    Example:
        {'access_mode': 'restricted', 'investigation_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'outcome': 'granted', 'surface':
            'chat'}

    Attributes:
        access_mode (str): The data source's access mode at query time (default, restricted) Example: restricted.
        outcome (str): Whether the query was granted or denied Example: granted.
        surface (str): The product surface the query ran from (chat, investigation, explore, mcp_client, verify), or
            internal for system paths with no surface Example: chat.
        investigation_id (str | Unset): The investigation the query ran for, when investigation-driven Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    access_mode: str
    outcome: str
    surface: str
    investigation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_mode = self.access_mode

        outcome = self.outcome

        surface = self.surface

        investigation_id = self.investigation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_mode": access_mode,
                "outcome": outcome,
                "surface": surface,
            }
        )
        if investigation_id is not UNSET:
            field_dict["investigation_id"] = investigation_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_mode = d.pop("access_mode")

        outcome = d.pop("outcome")

        surface = d.pop("surface")

        investigation_id = d.pop("investigation_id", UNSET)

        audit_log_telemetry_data_source_queried_metadata_v2 = cls(
            access_mode=access_mode,
            outcome=outcome,
            surface=surface,
            investigation_id=investigation_id,
        )

        audit_log_telemetry_data_source_queried_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_queried_metadata_v2

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
