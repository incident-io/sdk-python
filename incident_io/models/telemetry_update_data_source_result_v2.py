from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.telemetry_data_source_v2 import TelemetryDataSourceV2


T = TypeVar("T", bound="TelemetryUpdateDataSourceResultV2")


@_attrs_define
class TelemetryUpdateDataSourceResultV2:
    """
    Example:
        {'data_source': {'created_at': '2021-08-17T13:28:57.801578Z', 'enabled': True, 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary Prometheus', 'provider': 'grafana', 'source_type': 'grafana',
            'updated_at': '2021-08-17T13:28:57.801578Z', 'version': '8.5.27'}}

    Attributes:
        data_source (TelemetryDataSourceV2): A telemetry data source integration Example: {'created_at':
            '2021-08-17T13:28:57.801578Z', 'enabled': True, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Primary
            Prometheus', 'provider': 'grafana', 'source_type': 'grafana', 'updated_at': '2021-08-17T13:28:57.801578Z',
            'version': '8.5.27'}.
    """

    data_source: TelemetryDataSourceV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_source = self.data_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source": data_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telemetry_data_source_v2 import (
            TelemetryDataSourceV2,
        )

        d = dict(src_dict)
        data_source = TelemetryDataSourceV2.from_dict(d.pop("data_source"))

        telemetry_update_data_source_result_v2 = cls(
            data_source=data_source,
        )

        telemetry_update_data_source_result_v2.additional_properties = d
        return telemetry_update_data_source_result_v2

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
