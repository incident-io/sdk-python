from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogOrganisationSettingsUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogOrganisationSettingsUpdatedMetadataV2:
    """
    Example:
        {'after_organisation_name': 'Acme Corporation', 'before_organisation_name': 'Pineapple Labs',
            'default_timezone': 'Europe/London'}

    Attributes:
        after_organisation_name (str | Unset): The organisation name after the change Example: Acme Corporation.
        before_organisation_name (str | Unset): The organisation name before the change Example: Pineapple Labs.
        default_timezone (str | Unset): The default timezone that was set Example: Europe/London.
    """

    after_organisation_name: str | Unset = UNSET
    before_organisation_name: str | Unset = UNSET
    default_timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_organisation_name = self.after_organisation_name

        before_organisation_name = self.before_organisation_name

        default_timezone = self.default_timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_organisation_name is not UNSET:
            field_dict["after_organisation_name"] = after_organisation_name
        if before_organisation_name is not UNSET:
            field_dict["before_organisation_name"] = before_organisation_name
        if default_timezone is not UNSET:
            field_dict["default_timezone"] = default_timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_organisation_name = d.pop("after_organisation_name", UNSET)

        before_organisation_name = d.pop("before_organisation_name", UNSET)

        default_timezone = d.pop("default_timezone", UNSET)

        audit_log_organisation_settings_updated_metadata_v2 = cls(
            after_organisation_name=after_organisation_name,
            before_organisation_name=before_organisation_name,
            default_timezone=default_timezone,
        )

        audit_log_organisation_settings_updated_metadata_v2.additional_properties = d
        return audit_log_organisation_settings_updated_metadata_v2

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
