from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_resource_v2_managed_by import ManagedResourceV2ManagedBy
from ..models.managed_resource_v2_resource_type import ManagedResourceV2ResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_resource_v2_annotations import ManagedResourceV2Annotations


T = TypeVar("T", bound="ManagedResourceV2")


@_attrs_define(kw_only=True)
class ManagedResourceV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'terraform', 'resource_id': 'abc123',
            'resource_type': 'alert_route', 'source_url': 'https://github.com/my-company/infrastructure'}

    Attributes:
        annotations (ManagedResourceV2Annotations): Annotations that track metadata about this resource Example:
            {'incident.io/terraform/version': '3.0.0'}.
        managed_by (ManagedResourceV2ManagedBy): How is this resource managed Example: terraform.
        resource_id (str): The ID of the resource that this relates to Example: abc123.
        resource_type (ManagedResourceV2ResourceType):  Example: alert_route.
        source_url (str | Unset): The url of the external repository where this resource is managed (if there is one)
            Example: https://github.com/my-company/infrastructure.
    """

    annotations: ManagedResourceV2Annotations
    managed_by: ManagedResourceV2ManagedBy
    resource_id: str
    resource_type: ManagedResourceV2ResourceType
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations.to_dict()

        managed_by = self.managed_by.value

        resource_id = self.resource_id

        resource_type = self.resource_type.value

        source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "managed_by": managed_by,
                "resource_id": resource_id,
                "resource_type": resource_type,
            }
        )
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.managed_resource_v2_annotations import (
            ManagedResourceV2Annotations,
        )

        d = dict(src_dict)
        annotations = ManagedResourceV2Annotations.from_dict(d.pop("annotations"))

        managed_by = ManagedResourceV2ManagedBy(d.pop("managed_by"))

        resource_id = d.pop("resource_id")

        resource_type = ManagedResourceV2ResourceType(d.pop("resource_type"))

        source_url = d.pop("source_url", UNSET)

        managed_resource_v2 = cls(
            annotations=annotations,
            managed_by=managed_by,
            resource_id=resource_id,
            resource_type=resource_type,
            source_url=source_url,
        )

        managed_resource_v2.additional_properties = d
        return managed_resource_v2

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
