from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationsV2ListAlert")


@_attrs_define(kw_only=True)
class EscalationsV2ListAlert:
    """Filter on the alert that created an escalation. Accepted operators are 'one_of' and 'not_in'.

    Example:
        {'one_of': ['01J479052SSQAA4531ASFPR3BF']}

    """

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        escalations_v2_list_alert = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        escalations_v2_list_alert.additional_properties = additional_properties
        return escalations_v2_list_alert

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
