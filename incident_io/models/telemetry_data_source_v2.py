from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryDataSourceV2")


@_attrs_define
class TelemetryDataSourceV2:
    """A telemetry data source integration

    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'enabled': True, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Primary Prometheus', 'provider': 'grafana', 'source_type': 'grafana', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': '8.5.27'}

    Attributes:
        created_at (datetime.datetime): When this data source was created Example: 2021-08-17T13:28:57.801578Z.
        enabled (bool): Whether this data source is enabled Example: True.
        id (str): Unique identifier for this data source Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        name (str): Human-readable name of the data source Example: Primary Prometheus.
        provider (str): Provider that hosts this data source Example: grafana.
        source_type (str): Type of data source (e.g., prometheus, loki, tempo) Example: grafana.
        updated_at (datetime.datetime): When this data source was last updated Example: 2021-08-17T13:28:57.801578Z.
        version (str | Unset): Upstream tool version captured at probe time (e.g. "8.5.27" for Grafana, "2.9.4" for
            Loki). Empty for SaaS providers and until the first successful probe. Example: 8.5.27.
    """

    created_at: datetime.datetime
    enabled: bool
    id: str
    name: str
    provider: str
    source_type: str
    updated_at: datetime.datetime
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        enabled = self.enabled

        id = self.id

        name = self.name

        provider = self.provider

        source_type = self.source_type

        updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "enabled": enabled,
                "id": id,
                "name": name,
                "provider": provider,
                "source_type": source_type,
                "updated_at": updated_at,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        enabled = d.pop("enabled")

        id = d.pop("id")

        name = d.pop("name")

        provider = d.pop("provider")

        source_type = d.pop("source_type")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version", UNSET)

        telemetry_data_source_v2 = cls(
            created_at=created_at,
            enabled=enabled,
            id=id,
            name=name,
            provider=provider,
            source_type=source_type,
            updated_at=updated_at,
            version=version,
        )

        telemetry_data_source_v2.additional_properties = d
        return telemetry_data_source_v2

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
