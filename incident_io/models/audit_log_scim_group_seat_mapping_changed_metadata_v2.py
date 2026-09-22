from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogSCIMGroupSeatMappingChangedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogSCIMGroupSeatMappingChangedMetadataV2:
    """
    Example:
        {'after_seat_types': '[full_access, responder_access]', 'before_seat_types': '[full_access]'}

    Attributes:
        after_seat_types (str): The seat types assigned to this SCIM group after the mapping was changed Example:
            [full_access, responder_access].
        before_seat_types (str): The seat types assigned to this SCIM group before the mapping was changed Example:
            [full_access].
    """

    after_seat_types: str
    before_seat_types: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_seat_types = self.after_seat_types

        before_seat_types = self.before_seat_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_seat_types": after_seat_types,
                "before_seat_types": before_seat_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_seat_types = d.pop("after_seat_types")

        before_seat_types = d.pop("before_seat_types")

        audit_log_scim_group_seat_mapping_changed_metadata_v2 = cls(
            after_seat_types=after_seat_types,
            before_seat_types=before_seat_types,
        )

        audit_log_scim_group_seat_mapping_changed_metadata_v2.additional_properties = d
        return audit_log_scim_group_seat_mapping_changed_metadata_v2

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
