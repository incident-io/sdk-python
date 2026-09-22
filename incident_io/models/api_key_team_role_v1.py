from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_team_role_v1_name import APIKeyTeamRoleV1Name

T = TypeVar("T", bound="APIKeyTeamRoleV1")


@_attrs_define(kw_only=True)
class APIKeyTeamRoleV1:
    """
    Example:
        {'description': 'can view data, like public incidents and organization settings', 'name': 'catalog_editor'}

    Attributes:
        description (str): Human readable description of the role Example: can view data, like public incidents and
            organization settings.
        name (APIKeyTeamRoleV1Name): API key role name that may be granted for team-scoped access Example:
            catalog_editor.
    """

    description: str
    name: APIKeyTeamRoleV1Name
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        name = APIKeyTeamRoleV1Name(d.pop("name"))

        api_key_team_role_v1 = cls(
            description=description,
            name=name,
        )

        api_key_team_role_v1.additional_properties = d
        return api_key_team_role_v1

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
