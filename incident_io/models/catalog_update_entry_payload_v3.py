from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_update_entry_payload_v3_attribute_values import (
        CatalogUpdateEntryPayloadV3AttributeValues,
    )


T = TypeVar("T", bound="CatalogUpdateEntryPayloadV3")


@_attrs_define(kw_only=True)
class CatalogUpdateEntryPayloadV3:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal':
            'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name':
            'Primary On-call', 'rank': 3, 'update_attributes': ['abc123']}

    Attributes:
        attribute_values (CatalogUpdateEntryPayloadV3AttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        aliases (list[str] | Unset): Optional aliases that can be used to reference this entry Example:
            ['lawrence@incident.io', 'lawrence'].
        external_id (str | Unset): An optional alternative ID for this entry, which is ensured to be unique for the type
            Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
        rank (int | Unset): When catalog type is ranked, this is used to help order things Example: 3.
        update_attributes (list[str] | Unset): If provided, only update these attribute_values keys. If not provided,
            update all attribute values.
            If you specify an attribute key that's not in your payload, the associated attribute value will be cleared.
            Example: ['abc123'].
    """

    attribute_values: CatalogUpdateEntryPayloadV3AttributeValues
    name: str
    aliases: list[str] | Unset = UNSET
    external_id: str | Unset = UNSET
    rank: int | Unset = UNSET
    update_attributes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        name = self.name

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        external_id = self.external_id

        rank = self.rank

        update_attributes: list[str] | Unset = UNSET
        if not isinstance(self.update_attributes, Unset):
            update_attributes = self.update_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "name": name,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if rank is not UNSET:
            field_dict["rank"] = rank
        if update_attributes is not UNSET:
            field_dict["update_attributes"] = update_attributes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_update_entry_payload_v3_attribute_values import (
            CatalogUpdateEntryPayloadV3AttributeValues,
        )

        d = dict(src_dict)
        attribute_values = CatalogUpdateEntryPayloadV3AttributeValues.from_dict(
            d.pop("attribute_values")
        )

        name = d.pop("name")

        aliases = cast(list[str], d.pop("aliases", UNSET))

        external_id = d.pop("external_id", UNSET)

        rank = d.pop("rank", UNSET)

        update_attributes = cast(list[str], d.pop("update_attributes", UNSET))

        catalog_update_entry_payload_v3 = cls(
            attribute_values=attribute_values,
            name=name,
            aliases=aliases,
            external_id=external_id,
            rank=rank,
            update_attributes=update_attributes,
        )

        catalog_update_entry_payload_v3.additional_properties = d
        return catalog_update_entry_payload_v3

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
