from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogCatalogAttributeUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogCatalogAttributeUpdatedMetadataV2:
    """
    Example:
        {'after_values': ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG2'], 'before_values':
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1']}

    Attributes:
        after_values (list[str]): The user IDs that are in the attribute after the change Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG2'].
        before_values (list[str]): The user IDs that were in the attribute before the change Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1'].
    """

    after_values: list[str]
    before_values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_values = self.after_values

        before_values = self.before_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_values": after_values,
                "before_values": before_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_values = cast(list[str], d.pop("after_values"))

        before_values = cast(list[str], d.pop("before_values"))

        audit_log_catalog_attribute_updated_metadata_v2 = cls(
            after_values=after_values,
            before_values=before_values,
        )

        audit_log_catalog_attribute_updated_metadata_v2.additional_properties = d
        return audit_log_catalog_attribute_updated_metadata_v2

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
