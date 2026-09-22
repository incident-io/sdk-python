from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incidents_v2_list_incident_role_additional_property import (
        IncidentsV2ListIncidentRoleAdditionalProperty,
    )


T = TypeVar("T", bound="IncidentsV2ListIncidentRole")


@_attrs_define(kw_only=True)
class IncidentsV2ListIncidentRole:
    """Filter on an incident role. Role ID should be sent, along with backlink attribute ID (if needed) followed by the
    operator and values. The accepted operators are 'one_of', 'is_blank'.

        Example:
            {'01GBSQF3FHF7FWZQNWGHAVQ804': {'one_of': ['01GBSQF3FHF7FWZQNWGHAVQ804', '01ET65M7ZARSFZ6TFDFVQDN9AA']}}

    """

    additional_properties: dict[str, IncidentsV2ListIncidentRoleAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incidents_v2_list_incident_role_additional_property import (
            IncidentsV2ListIncidentRoleAdditionalProperty,
        )

        d = dict(src_dict)
        incidents_v2_list_incident_role = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                IncidentsV2ListIncidentRoleAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        incidents_v2_list_incident_role.additional_properties = additional_properties
        return incidents_v2_list_incident_role

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> IncidentsV2ListIncidentRoleAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: IncidentsV2ListIncidentRoleAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
