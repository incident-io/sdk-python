from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_v1 import APIKeyV1
    from ..models.pagination_meta_result_v1 import PaginationMetaResultV1


T = TypeVar("T", bound="APIKeysListResultV1")


@_attrs_define(kw_only=True)
class APIKeysListResultV1:
    """
    Example:
        {'api_keys': [{'comments': 'Requested in https://example.slack.com/archives/C123/p456', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_used_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'My test API key', 'roles': [{'description': 'can view data, like public
            incidents and organization settings', 'name': 'viewer'}], 'team_ids': ['abc123'], 'team_roles': [{'description':
            'can view data, like public incidents and organization settings', 'name': 'catalog_editor'}],
            'token_last_issued_at': '2021-08-17T13:28:57.801578Z'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        api_keys (list[APIKeyV1]):  Example: [{'comments': 'Requested in https://example.slack.com/archives/C123/p456',
            'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'last_used_at': '2021-08-17T13:28:57.801578Z', 'name': 'My test API key', 'roles': [{'description': 'can view
            data, like public incidents and organization settings', 'name': 'viewer'}], 'team_ids': ['abc123'],
            'team_roles': [{'description': 'can view data, like public incidents and organization settings', 'name':
            'catalog_editor'}], 'token_last_issued_at': '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV1):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    api_keys: list[APIKeyV1]
    pagination_meta: PaginationMetaResultV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_keys": api_keys,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_key_v1 import APIKeyV1
        from ..models.pagination_meta_result_v1 import (
            PaginationMetaResultV1,
        )

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = APIKeyV1.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        pagination_meta = PaginationMetaResultV1.from_dict(d.pop("pagination_meta"))

        api_keys_list_result_v1 = cls(
            api_keys=api_keys,
            pagination_meta=pagination_meta,
        )

        api_keys_list_result_v1.additional_properties = d
        return api_keys_list_result_v1

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
