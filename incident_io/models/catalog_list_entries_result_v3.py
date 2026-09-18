from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_entry_v3 import CatalogEntryV3
    from ..models.catalog_type_v3 import CatalogTypeV3
    from ..models.pagination_meta_result_with_total_v3 import (
        PaginationMetaResultWithTotalV3,
    )


T = TypeVar("T", bound="CatalogListEntriesResultV3")


@_attrs_define
class CatalogListEntriesResultV3:
    """
    Example:
        {'catalog_entries': [{'aliases': ['lawrence@incident.io', 'lawrence'], 'archived_at':
            '2021-08-17T14:28:57.801578Z', 'attribute_values': {'abc123': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123'}}}, 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank':
            3, 'updated_at': '2021-08-17T13:28:57.801578Z'}], 'catalog_type': {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters that we run inside of GKE.',
            'dynamic_resource_parameter': 'abc123', 'engine_resource_type': 'CatalogEntry["PagerDutyService"]',
            'estimated_count': 7, 'icon': 'alert', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'is_team_type':
            False, 'last_synced_at': '2021-08-17T13:28:57.801578Z', 'name': 'Kubernetes Cluster', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'ranked': True, 'registry_type': 'PagerDutyService', 'required_integrations':
            ['pager_duty'], 'schema': {'attributes': [{'array': False, 'backlink_attribute': 'abc123', 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'mode': '', 'name': 'tier', 'path': [{'attribute_id': 'abc123', 'attribute_name':
            'abc123'}], 'type': 'Custom["Service"]'}], 'version': 1}, 'source_repo_url': 'https://github.com/my-
            company/incident-io-catalog', 'type_name': 'Custom["BackstageGroup"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'use_name_as_identifier': True}, 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238}}

    Attributes:
        catalog_entries (list[CatalogEntryV3]):  Example: [{'aliases': ['lawrence@incident.io', 'lawrence'],
            'archived_at': '2021-08-17T14:28:57.801578Z', 'attribute_values': {'abc123': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123'}}},
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank':
            3, 'updated_at': '2021-08-17T13:28:57.801578Z'}].
        catalog_type (CatalogTypeV3):  Example: {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'},
            'categories': ['customer'], 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'dynamic_resource_parameter': 'abc123',
            'engine_resource_type': 'CatalogEntry["PagerDutyService"]', 'estimated_count': 7, 'icon': 'alert', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'is_team_type': False, 'last_synced_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'ranked': True, 'registry_type': 'PagerDutyService', 'required_integrations': ['pager_duty'], 'schema':
            {'attributes': [{'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': '',
            'name': 'tier', 'path': [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}],
            'version': 1}, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]', 'updated_at': '2021-08-17T13:28:57.801578Z', 'use_name_as_identifier': True}.
        pagination_meta (PaginationMetaResultWithTotalV3):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25, 'total_record_count': 238}.
    """

    catalog_entries: list[CatalogEntryV3]
    catalog_type: CatalogTypeV3
    pagination_meta: PaginationMetaResultWithTotalV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entries = []
        for catalog_entries_item_data in self.catalog_entries:
            catalog_entries_item = catalog_entries_item_data.to_dict()
            catalog_entries.append(catalog_entries_item)

        catalog_type = self.catalog_type.to_dict()

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entries": catalog_entries,
                "catalog_type": catalog_type,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_entry_v3 import CatalogEntryV3
        from ..models.catalog_type_v3 import CatalogTypeV3
        from ..models.pagination_meta_result_with_total_v3 import (
            PaginationMetaResultWithTotalV3,
        )

        d = dict(src_dict)
        catalog_entries = []
        _catalog_entries = d.pop("catalog_entries")
        for catalog_entries_item_data in _catalog_entries:
            catalog_entries_item = CatalogEntryV3.from_dict(catalog_entries_item_data)

            catalog_entries.append(catalog_entries_item)

        catalog_type = CatalogTypeV3.from_dict(d.pop("catalog_type"))

        pagination_meta = PaginationMetaResultWithTotalV3.from_dict(
            d.pop("pagination_meta")
        )

        catalog_list_entries_result_v3 = cls(
            catalog_entries=catalog_entries,
            catalog_type=catalog_type,
            pagination_meta=pagination_meta,
        )

        catalog_list_entries_result_v3.additional_properties = d
        return catalog_list_entries_result_v3

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
