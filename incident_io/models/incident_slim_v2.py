from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_slim_v2_status_category import IncidentSlimV2StatusCategory
from ..models.incident_slim_v2_visibility import IncidentSlimV2Visibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentSlimV2")


@_attrs_define
class IncidentSlimV2:
    """Incident slim is a subset of the full incident object, listing key fields.

    Example:
        {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
            'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
            'visibility': 'public'}

    Attributes:
        external_id (int): External identifier for the incident - often displayed with an INC- prefix Example: 123.
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        name (str): Explanation of the incident Example: Our database is sad.
        reference (str): Reference to this incident, as displayed across the product Example: INC-123.
        status_category (IncidentSlimV2StatusCategory): The category of the incidents status Example: triage.
        visibility (IncidentSlimV2Visibility): Whether the incident should be open to anyone in your Slack workspace
            (public), or invite-only (private). For more information on Private Incidents see our
            [docs](https://docs.incident.io/incidents/sensitive-incidents). Example: public.
        summary (str | Unset): Detailed description of the incident Example: Our database is really really sad, and we
            don't know why yet..
    """

    external_id: int
    id: str
    name: str
    reference: str
    status_category: IncidentSlimV2StatusCategory
    visibility: IncidentSlimV2Visibility
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        id = self.id

        name = self.name

        reference = self.reference

        status_category = self.status_category.value

        visibility = self.visibility.value

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "id": id,
                "name": name,
                "reference": reference,
                "status_category": status_category,
                "visibility": visibility,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        id = d.pop("id")

        name = d.pop("name")

        reference = d.pop("reference")

        status_category = IncidentSlimV2StatusCategory(d.pop("status_category"))

        visibility = IncidentSlimV2Visibility(d.pop("visibility"))

        summary = d.pop("summary", UNSET)

        incident_slim_v2 = cls(
            external_id=external_id,
            id=id,
            name=name,
            reference=reference,
            status_category=status_category,
            visibility=visibility,
            summary=summary,
        )

        incident_slim_v2.additional_properties = d
        return incident_slim_v2

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
