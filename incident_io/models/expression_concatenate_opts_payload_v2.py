from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExpressionConcatenateOptsPayloadV2")


@_attrs_define
class ExpressionConcatenateOptsPayloadV2:
    """
    Example:
        {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}

    Attributes:
        reference (str): The reference that you want to concatenate with Example:
            catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"].
    """

    reference: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reference = d.pop("reference")

        expression_concatenate_opts_payload_v2 = cls(
            reference=reference,
        )

        expression_concatenate_opts_payload_v2.additional_properties = d
        return expression_concatenate_opts_payload_v2

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
