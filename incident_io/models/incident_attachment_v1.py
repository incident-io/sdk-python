from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.external_resource_v1 import ExternalResourceV1


T = TypeVar("T", bound="IncidentAttachmentV1")


@_attrs_define(kw_only=True)
class IncidentAttachmentV1:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'external_id':
            '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title':
            'The database has gone down'}}

    Attributes:
        id (str): Unique identifier of this incident membership Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_id (str): Unique identifier of the incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        resource (ExternalResourceV1):  Example: {'external_id': '123', 'permalink':
            'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title': 'The database has
            gone down'}.
    """

    id: str
    incident_id: str
    resource: ExternalResourceV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        incident_id = self.incident_id

        resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "incident_id": incident_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_resource_v1 import ExternalResourceV1

        d = dict(src_dict)
        id = d.pop("id")

        incident_id = d.pop("incident_id")

        resource = ExternalResourceV1.from_dict(d.pop("resource"))

        incident_attachment_v1 = cls(
            id=id,
            incident_id=incident_id,
            resource=resource,
        )

        incident_attachment_v1.additional_properties = d
        return incident_attachment_v1

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
