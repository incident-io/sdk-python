from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_resources_create_managed_resource_payload_v2_resource_type import (
    ManagedResourcesCreateManagedResourcePayloadV2ResourceType,
)

if TYPE_CHECKING:
    from ..models.managed_resources_create_managed_resource_payload_v2_annotations import (
        ManagedResourcesCreateManagedResourcePayloadV2Annotations,
    )


T = TypeVar("T", bound="ManagedResourcesCreateManagedResourcePayloadV2")


@_attrs_define(kw_only=True)
class ManagedResourcesCreateManagedResourcePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'alert_route'}

    Attributes:
        annotations (ManagedResourcesCreateManagedResourcePayloadV2Annotations): Annotations that track metadata about
            this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        resource_id (str): The ID of the resource that this relates to Example: abc123.
        resource_type (ManagedResourcesCreateManagedResourcePayloadV2ResourceType): The type of the related resource
            Example: alert_route.
    """

    annotations: ManagedResourcesCreateManagedResourcePayloadV2Annotations
    resource_id: str
    resource_type: ManagedResourcesCreateManagedResourcePayloadV2ResourceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations.to_dict()

        resource_id = self.resource_id

        resource_type = self.resource_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "resource_id": resource_id,
                "resource_type": resource_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.managed_resources_create_managed_resource_payload_v2_annotations import (
            ManagedResourcesCreateManagedResourcePayloadV2Annotations,
        )

        d = dict(src_dict)
        annotations = (
            ManagedResourcesCreateManagedResourcePayloadV2Annotations.from_dict(
                d.pop("annotations")
            )
        )

        resource_id = d.pop("resource_id")

        resource_type = ManagedResourcesCreateManagedResourcePayloadV2ResourceType(
            d.pop("resource_type")
        )

        managed_resources_create_managed_resource_payload_v2 = cls(
            annotations=annotations,
            resource_id=resource_id,
            resource_type=resource_type,
        )

        managed_resources_create_managed_resource_payload_v2.additional_properties = d
        return managed_resources_create_managed_resource_payload_v2

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
