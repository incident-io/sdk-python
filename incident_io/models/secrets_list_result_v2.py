from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.secret_v2 import SecretV2


T = TypeVar("T", bound="SecretsListResultV2")


@_attrs_define(kw_only=True)
class SecretsListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'secrets': [{'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Auth token for the PagerDuty outgoing webhook', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123', 'name': 'PagerDuty webhook token', 'owning_team_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 3}]}

    Attributes:
        secrets (list[SecretV2]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Auth token
            for the PagerDuty outgoing webhook', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123', 'name':
            'PagerDuty webhook token', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    secrets: list[SecretV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secrets": secrets,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.secret_v2 import SecretV2

        d = dict(src_dict)
        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = SecretV2.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        secrets_list_result_v2 = cls(
            secrets=secrets,
            pagination_meta=pagination_meta,
        )

        secrets_list_result_v2.additional_properties = d
        return secrets_list_result_v2

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
