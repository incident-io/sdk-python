from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryGrafanaUpdateConfigV2")


@_attrs_define
class TelemetryGrafanaUpdateConfigV2:
    """Grafana-specific credential and endpoint updates

    Example:
        {'api_key': 'glsa_123', 'api_url': 'grafana.example.com'}

    Attributes:
        api_key (str | Unset): New Grafana service account token Example: glsa_123.
        api_url (str | Unset): Grafana API URL (without protocol) Example: grafana.example.com.
    """

    api_key: str | Unset = UNSET
    api_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        api_url = self.api_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_url is not UNSET:
            field_dict["api_url"] = api_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        api_key = d.pop("api_key", UNSET)

        api_url = d.pop("api_url", UNSET)

        telemetry_grafana_update_config_v2 = cls(
            api_key=api_key,
            api_url=api_url,
        )

        telemetry_grafana_update_config_v2.additional_properties = d
        return telemetry_grafana_update_config_v2

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
