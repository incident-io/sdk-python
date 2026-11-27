from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSourceAlertmanagerOptionsV2")


@_attrs_define(kw_only=True)
class AlertSourceAlertmanagerOptionsV2:
    """
    Example:
        {'one_alert_per_group': True}

    Attributes:
        one_alert_per_group (bool): Whether to create one alert per evaluation group or one alert per series within a
            group Default: True. Example: True.
    """

    one_alert_per_group: bool = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_alert_per_group = self.one_alert_per_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one_alert_per_group": one_alert_per_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        one_alert_per_group = d.pop("one_alert_per_group")

        alert_source_alertmanager_options_v2 = cls(
            one_alert_per_group=one_alert_per_group,
        )

        alert_source_alertmanager_options_v2.additional_properties = d
        return alert_source_alertmanager_options_v2

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
