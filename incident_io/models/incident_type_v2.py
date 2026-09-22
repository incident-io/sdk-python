from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_type_v2_create_in_triage import IncidentTypeV2CreateInTriage

T = TypeVar("T", bound="IncidentTypeV2")


@_attrs_define(kw_only=True)
class IncidentTypeV2:
    """
    Example:
        {'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing
            production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage',
            'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        create_in_triage (IncidentTypeV2CreateInTriage): Whether incidents of this must always, or can optionally, be
            created in triage Example: always.
        created_at (datetime.datetime): When this resource was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): What is this incident type for? Example: Customer facing production outages.
        id (str): Unique identifier for this Incident Type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_default (bool): The default Incident Type is used when no other type is explicitly specified Example: False.
        name (str): The name of this Incident Type Example: Production Outage.
        private_incidents_only (bool): Should all incidents created with this Incident Type be private? Example: False.
        updated_at (datetime.datetime): When this resource was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    create_in_triage: IncidentTypeV2CreateInTriage
    created_at: datetime.datetime
    description: str
    id: str
    is_default: bool
    name: str
    private_incidents_only: bool
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_in_triage = self.create_in_triage.value

        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        is_default = self.is_default

        name = self.name

        private_incidents_only = self.private_incidents_only

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_in_triage": create_in_triage,
                "created_at": created_at,
                "description": description,
                "id": id,
                "is_default": is_default,
                "name": name,
                "private_incidents_only": private_incidents_only,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        create_in_triage = IncidentTypeV2CreateInTriage(d.pop("create_in_triage"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        is_default = d.pop("is_default")

        name = d.pop("name")

        private_incidents_only = d.pop("private_incidents_only")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        incident_type_v2 = cls(
            create_in_triage=create_in_triage,
            created_at=created_at,
            description=description,
            id=id,
            is_default=is_default,
            name=name,
            private_incidents_only=private_incidents_only,
            updated_at=updated_at,
        )

        incident_type_v2.additional_properties = d
        return incident_type_v2

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
