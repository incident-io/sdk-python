from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_meta_v2_managed_by import ManagementMetaV2ManagedBy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_meta_v2_annotations import ManagementMetaV2Annotations


T = TypeVar("T", bound="ManagementMetaV2")


@_attrs_define
class ManagementMetaV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard', 'source_url':
            'https://github.com/my-company/infrastructure'}

    Attributes:
        annotations (ManagementMetaV2Annotations): Annotations that track metadata about this resource Example:
            {'incident.io/terraform/version': '3.0.0'}.
        managed_by (ManagementMetaV2ManagedBy): How is this resource managed Example: dashboard.
        source_url (str | Unset): The url of the external repository where this resource is managed (if there is one)
            Example: https://github.com/my-company/infrastructure.
    """

    annotations: ManagementMetaV2Annotations
    managed_by: ManagementMetaV2ManagedBy
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations.to_dict()

        managed_by = self.managed_by.value

        source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "managed_by": managed_by,
            }
        )
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.management_meta_v2_annotations import (
            ManagementMetaV2Annotations,
        )

        d = dict(src_dict)
        annotations = ManagementMetaV2Annotations.from_dict(d.pop("annotations"))

        managed_by = ManagementMetaV2ManagedBy(d.pop("managed_by"))

        source_url = d.pop("source_url", UNSET)

        management_meta_v2 = cls(
            annotations=annotations,
            managed_by=managed_by,
            source_url=source_url,
        )

        management_meta_v2.additional_properties = d
        return management_meta_v2

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
