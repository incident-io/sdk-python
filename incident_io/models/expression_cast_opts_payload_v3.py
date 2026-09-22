from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.returns_meta_v3 import ReturnsMetaV3


T = TypeVar("T", bound="ExpressionCastOptsPayloadV3")


@_attrs_define(kw_only=True)
class ExpressionCastOptsPayloadV3:
    """
    Example:
        {'returns': {'array': True, 'type': 'IncidentStatus'}}

    Attributes:
        returns (ReturnsMetaV3):  Example: {'array': True, 'type': 'IncidentStatus'}.
    """

    returns: ReturnsMetaV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        returns = self.returns.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returns": returns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.returns_meta_v3 import ReturnsMetaV3

        d = dict(src_dict)
        returns = ReturnsMetaV3.from_dict(d.pop("returns"))

        expression_cast_opts_payload_v3 = cls(
            returns=returns,
        )

        expression_cast_opts_payload_v3.additional_properties = d
        return expression_cast_opts_payload_v3

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
