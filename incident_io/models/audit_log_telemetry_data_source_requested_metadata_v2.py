from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTelemetryDataSourceRequestedMetadataV2")


@_attrs_define
class AuditLogTelemetryDataSourceRequestedMetadataV2:
    """
    Example:
        {'host': 'grafana.example.com', 'method': 'GET', 'origin': 'dashboard_sync', 'response_status': '200',
            'surface': 'internal', 'telemetry_query_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        host (str): The data source host the request was sent to Example: grafana.example.com.
        method (str): The HTTP method of the request Example: GET.
        surface (str): The product surface the request served (chat, investigation, explore, mcp_client, verify), or
            internal for system paths with no surface Example: internal.
        origin (str | Unset): The system job that made the request, when known (query, guidance, dashboard_sync, probe,
            unfurl, staff_cli, staff_workbench) Example: dashboard_sync.
        response_status (str | Unset): The HTTP status code of the response, absent when the request never completed
            Example: 200.
        telemetry_query_id (str | Unset): ID of the recorded query this request served, when one was in flight Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    host: str
    method: str
    surface: str
    origin: str | Unset = UNSET
    response_status: str | Unset = UNSET
    telemetry_query_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        method = self.method

        surface = self.surface

        origin = self.origin

        response_status = self.response_status

        telemetry_query_id = self.telemetry_query_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "method": method,
                "surface": surface,
            }
        )
        if origin is not UNSET:
            field_dict["origin"] = origin
        if response_status is not UNSET:
            field_dict["response_status"] = response_status
        if telemetry_query_id is not UNSET:
            field_dict["telemetry_query_id"] = telemetry_query_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        host = d.pop("host")

        method = d.pop("method")

        surface = d.pop("surface")

        origin = d.pop("origin", UNSET)

        response_status = d.pop("response_status", UNSET)

        telemetry_query_id = d.pop("telemetry_query_id", UNSET)

        audit_log_telemetry_data_source_requested_metadata_v2 = cls(
            host=host,
            method=method,
            surface=surface,
            origin=origin,
            response_status=response_status,
            telemetry_query_id=telemetry_query_id,
        )

        audit_log_telemetry_data_source_requested_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_requested_metadata_v2

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
