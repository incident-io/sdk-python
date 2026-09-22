from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_datadog_update_config_v2 import (
        TelemetryDatadogUpdateConfigV2,
    )
    from ..models.telemetry_grafana_update_config_v2 import (
        TelemetryGrafanaUpdateConfigV2,
    )


T = TypeVar("T", bound="TelemetryUpdateDataSourcePayloadV2")


@_attrs_define(kw_only=True)
class TelemetryUpdateDataSourcePayloadV2:
    """
    Example:
        {'datadog_config': {'api_key': 'abc123', 'app_key': 'abc123'}, 'grafana_config': {'api_key': 'glsa_123',
            'api_url': 'grafana.example.com'}, 'name': 'Production Grafana'}

    Attributes:
        datadog_config (TelemetryDatadogUpdateConfigV2 | Unset): Datadog-specific credential updates Example:
            {'api_key': 'abc123', 'app_key': 'abc123'}.
        grafana_config (TelemetryGrafanaUpdateConfigV2 | Unset): Grafana-specific credential and endpoint updates
            Example: {'api_key': 'glsa_123', 'api_url': 'grafana.example.com'}.
        name (str | Unset): Updated display name Example: Production Grafana.
    """

    datadog_config: TelemetryDatadogUpdateConfigV2 | Unset = UNSET
    grafana_config: TelemetryGrafanaUpdateConfigV2 | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datadog_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datadog_config, Unset):
            datadog_config = self.datadog_config.to_dict()

        grafana_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grafana_config, Unset):
            grafana_config = self.grafana_config.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datadog_config is not UNSET:
            field_dict["datadog_config"] = datadog_config
        if grafana_config is not UNSET:
            field_dict["grafana_config"] = grafana_config
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telemetry_datadog_update_config_v2 import (
            TelemetryDatadogUpdateConfigV2,
        )
        from ..models.telemetry_grafana_update_config_v2 import (
            TelemetryGrafanaUpdateConfigV2,
        )

        d = dict(src_dict)
        _datadog_config = d.pop("datadog_config", UNSET)
        datadog_config: TelemetryDatadogUpdateConfigV2 | Unset
        if isinstance(_datadog_config, Unset):
            datadog_config = UNSET
        else:
            datadog_config = TelemetryDatadogUpdateConfigV2.from_dict(_datadog_config)

        _grafana_config = d.pop("grafana_config", UNSET)
        grafana_config: TelemetryGrafanaUpdateConfigV2 | Unset
        if isinstance(_grafana_config, Unset):
            grafana_config = UNSET
        else:
            grafana_config = TelemetryGrafanaUpdateConfigV2.from_dict(_grafana_config)

        name = d.pop("name", UNSET)

        telemetry_update_data_source_payload_v2 = cls(
            datadog_config=datadog_config,
            grafana_config=grafana_config,
            name=name,
        )

        telemetry_update_data_source_payload_v2.additional_properties = d
        return telemetry_update_data_source_payload_v2

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
