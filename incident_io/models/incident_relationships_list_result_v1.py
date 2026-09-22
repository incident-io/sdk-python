from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_relationship_v1 import IncidentRelationshipV1
    from ..models.pagination_meta_result_v1 import PaginationMetaResultV1


T = TypeVar("T", bound="IncidentRelationshipsListResultV1")


@_attrs_define(kw_only=True)
class IncidentRelationshipsListResultV1:
    """
    Example:
        {'incident_relationships': [{'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident': {'external_id': 123, 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'The database is down'}}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        incident_relationships (list[IncidentRelationshipV1]):  Example: [{'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident': {'external_id': 123, 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'The database is down'}}].
        pagination_meta (PaginationMetaResultV1 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    incident_relationships: list[IncidentRelationshipV1]
    pagination_meta: PaginationMetaResultV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_relationships = []
        for incident_relationships_item_data in self.incident_relationships:
            incident_relationships_item = incident_relationships_item_data.to_dict()
            incident_relationships.append(incident_relationships_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_relationships": incident_relationships,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_relationship_v1 import (
            IncidentRelationshipV1,
        )
        from ..models.pagination_meta_result_v1 import (
            PaginationMetaResultV1,
        )

        d = dict(src_dict)
        incident_relationships = []
        _incident_relationships = d.pop("incident_relationships")
        for incident_relationships_item_data in _incident_relationships:
            incident_relationships_item = IncidentRelationshipV1.from_dict(
                incident_relationships_item_data
            )

            incident_relationships.append(incident_relationships_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV1 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV1.from_dict(_pagination_meta)

        incident_relationships_list_result_v1 = cls(
            incident_relationships=incident_relationships,
            pagination_meta=pagination_meta,
        )

        incident_relationships_list_result_v1.additional_properties = d
        return incident_relationships_list_result_v1

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
