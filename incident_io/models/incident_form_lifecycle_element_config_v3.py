from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentFormLifecycleElementConfigV3")


@_attrs_define(kw_only=True)
class IncidentFormLifecycleElementConfigV3:
    """
    Example:
        {'require_comment': False}

    Attributes:
        require_comment (bool | Unset): Whether the free-text comment must be filled in, for anyone giving investigation
            feedback Example: False.
    """

    require_comment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        require_comment = self.require_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if require_comment is not UNSET:
            field_dict["require_comment"] = require_comment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        require_comment = d.pop("require_comment", UNSET)

        incident_form_lifecycle_element_config_v3 = cls(
            require_comment=require_comment,
        )

        incident_form_lifecycle_element_config_v3.additional_properties = d
        return incident_form_lifecycle_element_config_v3

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
