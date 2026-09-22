from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RBACRoleV2")


@_attrs_define(kw_only=True)
class RBACRoleV2:
    """
    Example:
        {'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}

    Attributes:
        id (str): Unique identifier of the RBAC role Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name of the RBAC role Example: Customer Success.
        slug (str): Unique human-readable slug for the RBAC role Example: customer-success.
        description (str | Unset): Description of the purpose for the RBAC role Example: Elevated permissions for the
            customer success team..
    """

    id: str
    name: str
    slug: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
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

        description = d.pop("description", UNSET)

        rbac_role_v2 = cls(
            id=id,
            name=name,
            slug=slug,
            description=description,
        )

        rbac_role_v2.additional_properties = d
        return rbac_role_v2

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
