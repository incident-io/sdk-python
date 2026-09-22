from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReturnsMetaV2")


@_attrs_define(kw_only=True)
class ReturnsMetaV2:
    """
    Example:
        {'array': True, 'type': 'IncidentStatus'}

    Attributes:
        array (bool): Whether the return value should be single or multi-value Example: True.
        type_ (str): Expected return type of this expression (what to try casting the result to) Example:
            IncidentStatus.
    """

    array: bool
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        array = d.pop("array")

        type_ = d.pop("type")

        returns_meta_v2 = cls(
            array=array,
            type_=type_,
        )

        returns_meta_v2.additional_properties = d
        return returns_meta_v2

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
