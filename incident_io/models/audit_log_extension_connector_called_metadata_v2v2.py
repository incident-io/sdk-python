from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogExtensionConnectorCalledMetadataV2V2")


@_attrs_define
class AuditLogExtensionConnectorCalledMetadataV2V2:
    """
    Example:
        {'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'outcome': 'success', 'source_kind': 'mcp', 'surface': 'chat',
            'telemetry_query_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'write': 'true'}

    Attributes:
        outcome (str): How the call ended (success, error) Example: success.
        source_kind (str): The kind of connector that was called (mcp, http) Example: mcp.
        surface (str): The product surface the call ran from (chat, investigation, explore, mcp_client, verify), or
            internal for system paths with no surface Example: chat.
        write (str): Whether the call was permitted to change the connected system (true, false) Example: true.
        incident_id (str | Unset): The incident the call was made for, when incident-scoped Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        telemetry_query_id (str | Unset): ID of our stored record of this call Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    outcome: str
    source_kind: str
    surface: str
    write: str
    incident_id: str | Unset = UNSET
    telemetry_query_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome

        source_kind = self.source_kind

        surface = self.surface

        write = self.write

        incident_id = self.incident_id

        telemetry_query_id = self.telemetry_query_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "source_kind": source_kind,
                "surface": surface,
                "write": write,
            }
        )
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if telemetry_query_id is not UNSET:
            field_dict["telemetry_query_id"] = telemetry_query_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        outcome = d.pop("outcome")

        source_kind = d.pop("source_kind")

        surface = d.pop("surface")

        write = d.pop("write")

        incident_id = d.pop("incident_id", UNSET)

        telemetry_query_id = d.pop("telemetry_query_id", UNSET)

        audit_log_extension_connector_called_metadata_v2v2 = cls(
            outcome=outcome,
            source_kind=source_kind,
            surface=surface,
            write=write,
            incident_id=incident_id,
            telemetry_query_id=telemetry_query_id,
        )

        audit_log_extension_connector_called_metadata_v2v2.additional_properties = d
        return audit_log_extension_connector_called_metadata_v2v2

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
