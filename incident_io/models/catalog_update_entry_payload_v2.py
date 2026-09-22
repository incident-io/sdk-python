from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_update_entry_payload_v2_attribute_values import (
        CatalogUpdateEntryPayloadV2AttributeValues,
    )


T = TypeVar("T", bound="CatalogUpdateEntryPayloadV2")


@_attrs_define(kw_only=True)
class CatalogUpdateEntryPayloadV2:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call',
            'rank': 3}

    Attributes:
        attribute_values (CatalogUpdateEntryPayloadV2AttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        aliases (list[str] | Unset): Optional aliases that can be used to reference this entry Example:
            ['lawrence@incident.io', 'lawrence'].
        external_id (str | Unset): An optional alternative ID for this entry, which is ensured to be unique for the type
            Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
        rank (int | Unset): When catalog type is ranked, this is used to help order things Example: 3.
    """

    attribute_values: CatalogUpdateEntryPayloadV2AttributeValues
    name: str
    aliases: list[str] | Unset = UNSET
    external_id: str | Unset = UNSET
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        name = self.name

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        external_id = self.external_id

        rank = self.rank

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_update_entry_payload_v2_attribute_values import (
            CatalogUpdateEntryPayloadV2AttributeValues,
        )

        d = dict(src_dict)
        attribute_values = CatalogUpdateEntryPayloadV2AttributeValues.from_dict(
            d.pop("attribute_values")
        )

        name = d.pop("name")

        aliases = cast(list[str], d.pop("aliases", UNSET))

        external_id = d.pop("external_id", UNSET)

        rank = d.pop("rank", UNSET)

        catalog_update_entry_payload_v2 = cls(
            attribute_values=attribute_values,
            name=name,
            aliases=aliases,
            external_id=external_id,
            rank=rank,
        )

        catalog_update_entry_payload_v2.additional_properties = d
        return catalog_update_entry_payload_v2

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
