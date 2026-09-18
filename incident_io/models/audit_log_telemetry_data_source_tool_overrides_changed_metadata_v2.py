from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2")


@_attrs_define
class AuditLogTelemetryDataSourceToolOverridesChangedMetadataV2:
    """
    Example:
        {'after': '{"surfaces":{"chat":{"value":{"type":"deny"},"set_at":"2026-01-
            02T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'before': '{"surfaces":{"chat":{"value":{"type":"allow"
            },"set_at":"2026-01-01T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}', 'change_id':
            '01JD8ZQK9X0000000000000000', 'tool': 'restart_service'}

    Attributes:
        after (str): The tool's pins after the change, as JSON; empty when the change removed the last one Example: {"su
            rfaces":{"chat":{"value":{"type":"deny"},"set_at":"2026-01-
            02T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}.
        before (str): The tool's pins before the change, as JSON; empty when nothing was pinned on it Example: {"surface
            s":{"chat":{"value":{"type":"allow"},"set_at":"2026-01-01T00:00:00Z","set_by":"01FCNDV6P870EA6S7TK1DSYDG0"}}}.
        change_id (str): Shared by every entry the same save produced, so the decision that changed and the access it
            reached can be read together Example: 01JD8ZQK9X0000000000000000.
        tool (str): The name of the tool whose pinned decisions changed Example: restart_service.
    """

    after: str
    before: str
    change_id: str
    tool: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        change_id = self.change_id

        tool = self.tool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "before": before,
                "change_id": change_id,
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

        tool = d.pop("tool")

        audit_log_telemetry_data_source_tool_overrides_changed_metadata_v2 = cls(
            after=after,
            before=before,
            change_id=change_id,
            tool=tool,
        )

        audit_log_telemetry_data_source_tool_overrides_changed_metadata_v2.additional_properties = d
        return audit_log_telemetry_data_source_tool_overrides_changed_metadata_v2

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
