from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_group_v2_type import AccessGroupV2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessGroupV2")


@_attrs_define(kw_only=True)
class AccessGroupV2:
    """An access group is a named group of users. Access grants give a group its
    privileges, and every member of the group gets them.

    Every organisation has base groups (Owner, Admin and Standard), which can be listed and
    granted privileges but not changed or deleted. Membership is managed in the dashboard or
    through SCIM, not through this API.

        Example:
            {'description': 'Engineers who run the platform and its tooling', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Platform team', 'slug': 'platform-team', 'type': 'custom'}

        Attributes:
            id (str): Unique identifier for this access group Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            name (str): Human-readable name, unique within the organisation Example: Platform team.
            slug (str): Stable identifier, unique within the organisation. Base groups use owner, admin and standard.
                Generated from the name when omitted on create, and cannot be changed later. Example: platform-team.
            type_ (AccessGroupV2Type): base for the groups every organisation has, which cannot be changed or deleted, or
                custom for groups you create Example: custom.
            description (str | Unset): Optional description of who belongs in this group Example: Engineers who run the
                platform and its tooling.
    """

    id: str
    name: str
    slug: str
    type_: AccessGroupV2Type
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        type_ = self.type_.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = AccessGroupV2Type(d.pop("type"))

        description = d.pop("description", UNSET)

        access_group_v2 = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            description=description,
        )

        access_group_v2.additional_properties = d
        return access_group_v2

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
