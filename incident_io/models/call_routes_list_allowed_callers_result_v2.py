from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_route_allowed_caller_v2 import CallRouteAllowedCallerV2


T = TypeVar("T", bound="CallRoutesListAllowedCallersResultV2")


@_attrs_define(kw_only=True)
class CallRoutesListAllowedCallersResultV2:
    """
    Example:
        {'allowed_callers': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Regulator duty desk', 'phone_number':
            '+15551234567'}]}

    Attributes:
        allowed_callers (list[CallRouteAllowedCallerV2]):  Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Regulator duty desk', 'phone_number': '+15551234567'}].
    """

    allowed_callers: list[CallRouteAllowedCallerV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_callers = []
        for allowed_callers_item_data in self.allowed_callers:
            allowed_callers_item = allowed_callers_item_data.to_dict()
            allowed_callers.append(allowed_callers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_callers": allowed_callers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_allowed_caller_v2 import (
            CallRouteAllowedCallerV2,
        )

        d = dict(src_dict)
        allowed_callers = []
        _allowed_callers = d.pop("allowed_callers")
        for allowed_callers_item_data in _allowed_callers:
            allowed_callers_item = CallRouteAllowedCallerV2.from_dict(
                allowed_callers_item_data
            )

            allowed_callers.append(allowed_callers_item)

        call_routes_list_allowed_callers_result_v2 = cls(
            allowed_callers=allowed_callers,
        )

        call_routes_list_allowed_callers_result_v2.additional_properties = d
        return call_routes_list_allowed_callers_result_v2

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
