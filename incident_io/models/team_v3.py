from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_entry_slim_v3v3 import CatalogEntrySlimV3V3
    from ..models.user_v3 import UserV3


T = TypeVar("T", bound="TeamV3")


@_attrs_define
class TeamV3:
    """
    Example:
        {'catalog_entry': {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Primary On-call'}, 'id': 'abc123', 'members': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id': 'U02AYNF2XJM'}], 'name': 'abc123'}

    Attributes:
        catalog_entry (CatalogEntrySlimV3V3):  Example: {'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}.
        id (str): Unique ID of the team Example: abc123.
        members (list[UserV3]): Members of the team Example: [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'slack_user_id': 'U02AYNF2XJM'}].
        name (str): Name of the team Example: abc123.
    """

    catalog_entry: CatalogEntrySlimV3V3
    id: str
    members: list[UserV3]
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entry = self.catalog_entry.to_dict()

        id = self.id

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entry": catalog_entry,
                "id": id,
                "members": members,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_entry_slim_v3v3 import (
            CatalogEntrySlimV3V3,
        )
        from ..models.user_v3 import UserV3

        d = dict(src_dict)
        catalog_entry = CatalogEntrySlimV3V3.from_dict(d.pop("catalog_entry"))

        id = d.pop("id")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = UserV3.from_dict(members_item_data)

            members.append(members_item)

        name = d.pop("name")

        team_v3 = cls(
            catalog_entry=catalog_entry,
            id=id,
            members=members,
            name=name,
        )

        team_v3.additional_properties = d
        return team_v3

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
