from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_attachments_create_payload_v1_resource_resource_type import (
    IncidentAttachmentsCreatePayloadV1ResourceResourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentAttachmentsCreatePayloadV1Resource")


@_attrs_define
class IncidentAttachmentsCreatePayloadV1Resource:
    """
    Example:
        {'emoji': 'rocket', 'external_id': '123', 'resource_type': 'pager_duty_incident', 'title': 'Impact tracking
            spreadsheet', 'url': 'https://github.com/company/repo/pull/123'}

    Attributes:
        resource_type (IncidentAttachmentsCreatePayloadV1ResourceResourceType): E.g. PagerDuty: the external system that
            holds the resource Example: pager_duty_incident.
        emoji (str | Unset): Emoji shortcode representing the link, without surrounding colons. Only supported for the
            arbitrary_url resource type. Example: rocket.
        external_id (str | Unset): ID of the resource in the external system Example: 123.
        title (str | Unset): Human readable title for the link. Only supported for the arbitrary_url resource type.
            Example: Impact tracking spreadsheet.
        url (str | Unset): URL of the external resource to attach for the given resource type. Example:
            https://github.com/company/repo/pull/123.
    """

    resource_type: IncidentAttachmentsCreatePayloadV1ResourceResourceType
    emoji: str | Unset = UNSET
    external_id: str | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        emoji = self.emoji

        external_id = self.external_id

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
            }
        )
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        resource_type = IncidentAttachmentsCreatePayloadV1ResourceResourceType(
            d.pop("resource_type")
        )

        emoji = d.pop("emoji", UNSET)

        external_id = d.pop("external_id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        incident_attachments_create_payload_v1_resource = cls(
            resource_type=resource_type,
            emoji=emoji,
            external_id=external_id,
            title=title,
            url=url,
        )

        incident_attachments_create_payload_v1_resource.additional_properties = d
        return incident_attachments_create_payload_v1_resource

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
