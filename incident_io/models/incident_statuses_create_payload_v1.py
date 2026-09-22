from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_statuses_create_payload_v1_category import (
    IncidentStatusesCreatePayloadV1Category,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentStatusesCreatePayloadV1")


@_attrs_define(kw_only=True)
class IncidentStatusesCreatePayloadV1:
    """
    Example:
        {'category': 'live', 'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed', 'rank': 4}

    Attributes:
        category (IncidentStatusesCreatePayloadV1Category): Whether the status should be considered 'live' (now renamed
            to active), 'learning' (now renamed to post-incident) or 'closed'. The triage and declined statuses cannot be
            created or modified. Example: live.
        description (str): Rich text description of the incident status Example: Impact has been **fully mitigated**,
            and we're ready to learn from this incident..
        name (str): Unique name of this status Example: Closed.
        rank (int | Unset): Where this status sits within its category, lowest rank first. No two statuses in the same
            category can share a rank, but ranks needn't run consecutively — leaving gaps (10, 20, 30) means you can later
            insert a status between two others without renumbering them. Omit it to add this status to the end of its
            category. Example: 4.
    """

    category: IncidentStatusesCreatePayloadV1Category
    description: str
    name: str
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        description = self.description

        name = self.name

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "name": name,
            }
        )
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = IncidentStatusesCreatePayloadV1Category(d.pop("category"))

        description = d.pop("description")

        name = d.pop("name")

        rank = d.pop("rank", UNSET)

        incident_statuses_create_payload_v1 = cls(
            category=category,
            description=description,
            name=name,
            rank=rank,
        )

        incident_statuses_create_payload_v1.additional_properties = d
        return incident_statuses_create_payload_v1

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
