from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_type_v2 import CatalogTypeV2


T = TypeVar("T", bound="CatalogUpdateTypeSchemaResultV2")


@_attrs_define
class CatalogUpdateTypeSchemaResultV2:
    """
    Example:
        {'catalog_type': {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories':
            ['customer'], 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents
            Kubernetes clusters that we run inside of GKE.', 'dynamic_resource_parameter': 'abc123', 'estimated_count': 7,
            'icon': 'alert', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'last_synced_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Kubernetes Cluster', 'ranked': True, 'registry_type':
            'PagerDutyService', 'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name': 'tier', 'path':
            [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}], 'version': 1},
            'semantic_type': 'abc123', 'source_repo_url': 'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        catalog_type (CatalogTypeV2):  Example: {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'},
            'categories': ['customer'], 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'dynamic_resource_parameter': 'abc123',
            'estimated_count': 7, 'icon': 'alert', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False,
            'last_synced_at': '2021-08-17T13:28:57.801578Z', 'name': 'Kubernetes Cluster', 'ranked': True, 'registry_type':
            'PagerDutyService', 'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name': 'tier', 'path':
            [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}], 'version': 1},
            'semantic_type': 'custom', 'source_repo_url': 'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    catalog_type: CatalogTypeV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_type = self.catalog_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_type": catalog_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_type_v2 import CatalogTypeV2

        d = dict(src_dict)
        catalog_type = CatalogTypeV2.from_dict(d.pop("catalog_type"))

        catalog_update_type_schema_result_v2 = cls(
            catalog_type=catalog_type,
        )

        catalog_update_type_schema_result_v2.additional_properties = d
        return catalog_update_type_schema_result_v2

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
