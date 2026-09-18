from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentRelationshipDetailsV1")


@_attrs_define
class IncidentRelationshipDetailsV1:
    """
    Example:
        {'external_id': 123, 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'The database is down'}

    Attributes:
        external_id (int): External ID of this incident often prepended with 'INC-' Example: 123.
        id (str): Unique identifier of this incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Name of this incident Example: The database is down.
    """

    external_id: int
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        id = d.pop("id")

        name = d.pop("name")

        incident_relationship_details_v1 = cls(
            external_id=external_id,
            id=id,
            name=name,
        )

        incident_relationship_details_v1.additional_properties = d
        return incident_relationship_details_v1

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
