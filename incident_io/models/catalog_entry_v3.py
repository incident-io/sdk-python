from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_v3_attribute_values import CatalogEntryV3AttributeValues


T = TypeVar("T", bound="CatalogEntryV3")


@_attrs_define
class CatalogEntryV3:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'archived_at': '2021-08-17T14:28:57.801578Z',
            'attribute_values': {'abc123': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2021-08-17T13:28:57.801578Z', 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank': 3, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        aliases (list[str]): Optional aliases that can be used to reference this entry Example: ['lawrence@incident.io',
            'lawrence'].
        attribute_values (CatalogEntryV3AttributeValues): Values of this entry Example: {'abc123': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123'}}}.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (datetime.datetime): When this entry was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        rank (int): When catalog type is ranked, this is used to help order things Example: 3.
        updated_at (datetime.datetime): When this entry was last updated Example: 2021-08-17T13:28:57.801578Z.
        archived_at (datetime.datetime | Unset): When this entry was archived Example: 2021-08-17T14:28:57.801578Z.
        external_id (str | Unset): An optional alternative ID for this entry, which is ensured to be unique for the type
            Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
    """

    aliases: list[str]
    attribute_values: CatalogEntryV3AttributeValues
    catalog_type_id: str
    created_at: datetime.datetime
    id: str
    name: str
    rank: int
    updated_at: datetime.datetime
    archived_at: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases = self.aliases

        attribute_values = self.attribute_values.to_dict()

        catalog_type_id = self.catalog_type_id

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        rank = self.rank

        updated_at = self.updated_at.isoformat()

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aliases": aliases,
                "attribute_values": attribute_values,
                "catalog_type_id": catalog_type_id,
                "created_at": created_at,
                "id": id,
                "name": name,
                "rank": rank,
                "updated_at": updated_at,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_entry_v3_attribute_values import (
            CatalogEntryV3AttributeValues,
        )

        d = dict(src_dict)
        aliases = cast(list[str], d.pop("aliases"))

        attribute_values = CatalogEntryV3AttributeValues.from_dict(
            d.pop("attribute_values")
        )

        catalog_type_id = d.pop("catalog_type_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        external_id = d.pop("external_id", UNSET)

        catalog_entry_v3 = cls(
            aliases=aliases,
            attribute_values=attribute_values,
            catalog_type_id=catalog_type_id,
            created_at=created_at,
            id=id,
            name=name,
            rank=rank,
            updated_at=updated_at,
            archived_at=archived_at,
            external_id=external_id,
        )

        catalog_entry_v3.additional_properties = d
        return catalog_entry_v3

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
