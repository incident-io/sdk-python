from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExpressionNavigateOptsV3")


@_attrs_define(kw_only=True)
class ExpressionNavigateOptsV3:
    """
    Example:
        {'reference': '1235', 'reference_label': 'Teams'}

    Attributes:
        reference (str): The reference within the scope to navigate to Example: 1235.
        reference_label (str): The name of the reference to navigate to Example: Teams.
    """

    reference: str
    reference_label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        reference_label = self.reference_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "reference_label": reference_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reference = d.pop("reference")

        reference_label = d.pop("reference_label")

        expression_navigate_opts_v3 = cls(
            reference=reference,
            reference_label=reference_label,
        )

        expression_navigate_opts_v3.additional_properties = d
        return expression_navigate_opts_v3

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
