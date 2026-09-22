from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryDatadogUpdateConfigV2")


@_attrs_define(kw_only=True)
class TelemetryDatadogUpdateConfigV2:
    """Datadog-specific credential updates

    Example:
        {'api_key': 'abc123', 'app_key': 'abc123'}

    Attributes:
        api_key (str | Unset): New Datadog API key Example: abc123.
        app_key (str | Unset): New Datadog Application key Example: abc123.
    """

    api_key: str | Unset = UNSET
    app_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        app_key = self.app_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if app_key is not UNSET:
            field_dict["app_key"] = app_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        api_key = d.pop("api_key", UNSET)

        app_key = d.pop("app_key", UNSET)

        telemetry_datadog_update_config_v2 = cls(
            api_key=api_key,
            app_key=app_key,
        )

        telemetry_datadog_update_config_v2.additional_properties = d
        return telemetry_datadog_update_config_v2

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
