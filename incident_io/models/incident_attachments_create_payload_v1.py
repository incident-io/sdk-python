from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_attachments_create_payload_v1_resource import (
        IncidentAttachmentsCreatePayloadV1Resource,
    )


T = TypeVar("T", bound="IncidentAttachmentsCreatePayloadV1")


@_attrs_define(kw_only=True)
class IncidentAttachmentsCreatePayloadV1:
    """
    Example:
        {'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'emoji': 'rocket', 'external_id': '123',
            'resource_type': 'pager_duty_incident', 'title': 'Impact tracking spreadsheet', 'url':
            'https://github.com/company/repo/pull/123'}}

    Attributes:
        incident_id (str): ID of the incident to add an attachment to Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        resource (IncidentAttachmentsCreatePayloadV1Resource):  Example: {'emoji': 'rocket', 'external_id': '123',
            'resource_type': 'pager_duty_incident', 'title': 'Impact tracking spreadsheet', 'url':
            'https://github.com/company/repo/pull/123'}.
    """

    incident_id: str
    resource: IncidentAttachmentsCreatePayloadV1Resource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_attachments_create_payload_v1_resource import (
            IncidentAttachmentsCreatePayloadV1Resource,
        )

        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        resource = IncidentAttachmentsCreatePayloadV1Resource.from_dict(
            d.pop("resource")
        )

        incident_attachments_create_payload_v1 = cls(
            incident_id=incident_id,
            resource=resource,
        )

        incident_attachments_create_payload_v1.additional_properties = d
        return incident_attachments_create_payload_v1

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
