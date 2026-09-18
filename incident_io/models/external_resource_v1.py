from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_resource_v1_resource_type import ExternalResourceV1ResourceType

T = TypeVar("T", bound="ExternalResourceV1")


@_attrs_define
class ExternalResourceV1:
    """
    Example:
        {'external_id': '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type':
            'pager_duty_incident', 'title': 'The database has gone down'}

    Attributes:
        external_id (str): ID of the resource in the external system Example: 123.
        permalink (str): URL of the resource Example: https://my.pagerduty.com/incidents/ABC.
        resource_type (ExternalResourceV1ResourceType): E.g. PagerDuty: the external system that holds the resource
            Example: pager_duty_incident.
        title (str): Title of resource Example: The database has gone down.
    """

    external_id: str
    permalink: str
    resource_type: ExternalResourceV1ResourceType
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        permalink = self.permalink

        resource_type = self.resource_type.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "permalink": permalink,
                "resource_type": resource_type,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        permalink = d.pop("permalink")

        resource_type = ExternalResourceV1ResourceType(d.pop("resource_type"))

        title = d.pop("title")

        external_resource_v1 = cls(
            external_id=external_id,
            permalink=permalink,
            resource_type=resource_type,
            title=title,
        )

        external_resource_v1.additional_properties = d
        return external_resource_v1

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
