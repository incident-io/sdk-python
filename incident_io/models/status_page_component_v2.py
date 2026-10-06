from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_meta_v2 import ManagementMetaV2


T = TypeVar("T", bound="StatusPageComponentV2")


@_attrs_define(kw_only=True)
class StatusPageComponentV2:
    """A status page component that can appear on one or more status pages.

    Components are organisation-scoped. Placement on a page is controlled by that
    page's structure, not by ownership of the component.

        Example:
            {'description': 'Our iOS app', 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'management_meta': {'annotations':
                {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard', 'source_url': 'https://github.com/my-
                company/infrastructure'}, 'name': 'App'}

        Attributes:
            id (str): Unique identifier for this component Example: 01FCNDV6P870EA6S7TK1DSYDG1.
            management_meta (ManagementMetaV2):  Example: {'annotations': {'incident.io/terraform/version': '3.0.0'},
                'managed_by': 'dashboard', 'source_url': 'https://github.com/my-company/infrastructure'}.
            name (str): Human-readable name for the component Example: App.
            description (str | Unset): Optional short description of this component Example: Our iOS app.
    """

    id: str
    management_meta: ManagementMetaV2
    name: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        management_meta = self.management_meta.to_dict()

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "management_meta": management_meta,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.management_meta_v2 import ManagementMetaV2

        d = dict(src_dict)
        id = d.pop("id")

        management_meta = ManagementMetaV2.from_dict(d.pop("management_meta"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        status_page_component_v2 = cls(
            id=id,
            management_meta=management_meta,
            name=name,
            description=description,
        )

        status_page_component_v2.additional_properties = d
        return status_page_component_v2

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
