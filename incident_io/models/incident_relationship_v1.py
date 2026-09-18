from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_relationship_details_v1 import IncidentRelationshipDetailsV1


T = TypeVar("T", bound="IncidentRelationshipV1")


@_attrs_define
class IncidentRelationshipV1:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident': {'external_id': 123, 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'The database is down'}}

    Attributes:
        id (str): Unique identifier of this incident relationship Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident (IncidentRelationshipDetailsV1):  Example: {'external_id': 123, 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'The database is down'}.
    """

    id: str
    incident: IncidentRelationshipDetailsV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        incident = self.incident.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "incident": incident,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_relationship_details_v1 import (
            IncidentRelationshipDetailsV1,
        )

        d = dict(src_dict)
        id = d.pop("id")

        incident = IncidentRelationshipDetailsV1.from_dict(d.pop("incident"))

        incident_relationship_v1 = cls(
            id=id,
            incident=incident,
        )

        incident_relationship_v1.additional_properties = d
        return incident_relationship_v1

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
