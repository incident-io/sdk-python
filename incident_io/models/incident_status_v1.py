from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_status_v1_category import IncidentStatusV1Category

T = TypeVar("T", bound="IncidentStatusV1")


@_attrs_define
class IncidentStatusV1:
    """
    Example:
        {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        category (IncidentStatusV1Category): What category of status it is. All statuses apart from live (renamed in the
            app to Active) and learning (renamed in the app to Post-incident) are managed by incident.io and cannot be
            configured Example: triage.
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        description (str): Rich text description of the incident status Example: Impact has been **fully mitigated**,
            and we're ready to learn from this incident..
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Unique name of this status Example: Closed.
        rank (int): Order of this incident status Example: 4.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
    """

    category: IncidentStatusV1Category
    created_at: datetime.datetime
    description: str
    id: str
    name: str
    rank: int
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        name = self.name

        rank = self.rank

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "rank": rank,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = IncidentStatusV1Category(d.pop("category"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        incident_status_v1 = cls(
            category=category,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            rank=rank,
            updated_at=updated_at,
        )

        incident_status_v1.additional_properties = d
        return incident_status_v1

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
