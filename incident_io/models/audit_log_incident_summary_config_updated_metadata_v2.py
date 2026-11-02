from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogIncidentSummaryConfigUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogIncidentSummaryConfigUpdatedMetadataV2:
    """
    Example:
        {'after_structure_type': 'custom', 'before_structure_type': 'narrative', 'changed':
            'structure_type,custom_instructions'}

    Attributes:
        changed (str): What the update changed, comma separated (structure_type, custom_instructions) Example:
            structure_type,custom_instructions.
        after_structure_type (str | Unset): The format of suggested summaries after the change (narrative, stakeholder,
            custom) Example: custom.
        before_structure_type (str | Unset): The format of suggested summaries before the change (narrative,
            stakeholder, custom) Example: narrative.
    """

    changed: str
    after_structure_type: str | Unset = UNSET
    before_structure_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        after_structure_type = self.after_structure_type

        before_structure_type = self.before_structure_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
            }
        )
        if after_structure_type is not UNSET:
            field_dict["after_structure_type"] = after_structure_type
        if before_structure_type is not UNSET:
            field_dict["before_structure_type"] = before_structure_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed = d.pop("changed")

        after_structure_type = d.pop("after_structure_type", UNSET)

        before_structure_type = d.pop("before_structure_type", UNSET)

        audit_log_incident_summary_config_updated_metadata_v2 = cls(
            changed=changed,
            after_structure_type=after_structure_type,
            before_structure_type=before_structure_type,
        )

        audit_log_incident_summary_config_updated_metadata_v2.additional_properties = d
        return audit_log_incident_summary_config_updated_metadata_v2

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
