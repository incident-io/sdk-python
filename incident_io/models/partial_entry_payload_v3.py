from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_entry_payload_v3_attribute_values import (
        PartialEntryPayloadV3AttributeValues,
    )


T = TypeVar("T", bound="PartialEntryPayloadV3")


@_attrs_define
class PartialEntryPayloadV3:
    """Represents a partial entry update, allowing selective field updates

    Example:
        {'aliases': ['abc123'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value':
            {'literal': 'SEV123'}}}, 'entry_id': 'abc123', 'external_id': 'abc123', 'name': 'abc123', 'rank': 1}

    Attributes:
        attribute_values (PartialEntryPayloadV3AttributeValues): The attribute values to apply to this entry Example:
            {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}.
        entry_id (str): ID of the relevant catalog entry Example: abc123.
        aliases (list[str] | Unset): If specified, will update the aliases of the entry. When omitted, preserves the
            existing aliases. Example: ['abc123'].
        external_id (str | Unset): If specified, will update the external ID of the entry. When omitted, preserves the
            existing external ID. Example: abc123.
        name (str | Unset): If specified, will update the name of the entry. When omitted, preserves the existing name.
            Example: abc123.
        rank (int | Unset): If specified, will update the rank of the entry. When omitted, rank will be set to null
            (allowing rank removal). Example: 1.
    """

    attribute_values: PartialEntryPayloadV3AttributeValues
    entry_id: str
    aliases: list[str] | Unset = UNSET
    external_id: str | Unset = UNSET
    name: str | Unset = UNSET
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        entry_id = self.entry_id

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        external_id = self.external_id

        name = self.name

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "entry_id": entry_id,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if name is not UNSET:
            field_dict["name"] = name
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.partial_entry_payload_v3_attribute_values import (
            PartialEntryPayloadV3AttributeValues,
        )

        d = dict(src_dict)
        attribute_values = PartialEntryPayloadV3AttributeValues.from_dict(
            d.pop("attribute_values")
        )

        entry_id = d.pop("entry_id")

        aliases = cast(list[str], d.pop("aliases", UNSET))

        external_id = d.pop("external_id", UNSET)

        name = d.pop("name", UNSET)

        rank = d.pop("rank", UNSET)

        partial_entry_payload_v3 = cls(
            attribute_values=attribute_values,
            entry_id=entry_id,
            aliases=aliases,
            external_id=external_id,
            name=name,
            rank=rank,
        )

        partial_entry_payload_v3.additional_properties = d
        return partial_entry_payload_v3

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
