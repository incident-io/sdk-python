from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_attachment_v1 import IncidentAttachmentV1


T = TypeVar("T", bound="IncidentAttachmentsListResultV1")


@_attrs_define
class IncidentAttachmentsListResultV1:
    """
    Example:
        {'incident_attachments': [{'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'resource': {'external_id': '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type':
            'pager_duty_incident', 'title': 'The database has gone down'}}]}

    Attributes:
        incident_attachments (list[IncidentAttachmentV1]):  Example: [{'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'external_id': '123', 'permalink':
            'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title': 'The database has
            gone down'}}].
    """

    incident_attachments: list[IncidentAttachmentV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_attachments = []
        for incident_attachments_item_data in self.incident_attachments:
            incident_attachments_item = incident_attachments_item_data.to_dict()
            incident_attachments.append(incident_attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_attachments": incident_attachments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_attachment_v1 import (
            IncidentAttachmentV1,
        )

        d = dict(src_dict)
        incident_attachments = []
        _incident_attachments = d.pop("incident_attachments")
        for incident_attachments_item_data in _incident_attachments:
            incident_attachments_item = IncidentAttachmentV1.from_dict(
                incident_attachments_item_data
            )

            incident_attachments.append(incident_attachments_item)

        incident_attachments_list_result_v1 = cls(
            incident_attachments=incident_attachments,
        )

        incident_attachments_list_result_v1.additional_properties = d
        return incident_attachments_list_result_v1

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
