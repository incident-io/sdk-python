from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogTelemetryDataSourceToolAccessChangedMetadataV2")


@_attrs_define
class AuditLogTelemetryDataSourceToolAccessChangedMetadataV2:
    """
    Example:
        {'after': '{"type":"allow"}', 'before': '{"type":"deny"}', 'change_id': '01JD8ZQK9X0000000000000000', 'source':
            'override', 'surface': 'chat', 'tool': 'restart_service'}

    Attributes:
        after (str): The rule in force after the change, as the stored rule JSON, or the switch's new value Example:
            {"type":"allow"}.
        before (str): The rule in force before the change, as the stored rule JSON, or the switch's previous value;
            empty when the connector had no access policy before Example: {"type":"deny"}.
        change_id (str): Shared by every entry the same save produced, so the decision that changed and the access it
            reached can be read together Example: 01JD8ZQK9X0000000000000000.
        source (str): What decides it now: the connector's access policy, or a decision pinned on this tool (policy,
            override) Example: override.
        surface (str): The surface whose rule changed (chat, mcp_client, investigation), or enabled when it was the
            tool's own switch Example: chat.
        tool (str): The name of the tool whose access changed Example: restart_service.
    """

    after: str
    before: str
    change_id: str
    source: str
    surface: str
    tool: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        change_id = self.change_id

        source = self.source

        surface = self.surface

        tool = self.tool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "before": before,
                "change_id": change_id,
                "source": source,
                "surface": surface,
                "tool": tool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after = d.pop("after")

        before = d.pop("before")

        change_id = d.pop("change_id")

        source = d.pop("source")

        surface = d.pop("surface")

        tool = d.pop("tool")

        audit_log_telemetry_data_source_tool_access_changed_metadata_v2 = cls(
            after=after,
            before=before,
            change_id=change_id,
            source=source,
            surface=surface,
            tool=tool,
        )

        audit_log_telemetry_data_source_tool_access_changed_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_tool_access_changed_metadata_v2

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
