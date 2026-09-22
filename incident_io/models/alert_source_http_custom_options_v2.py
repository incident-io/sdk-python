from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSourceHTTPCustomOptionsV2")


@_attrs_define(kw_only=True)
class AlertSourceHTTPCustomOptionsV2:
    """
    Example:
        {'deduplication_key_path': '$.alert_id', 'transform_expression': "return {\\n  title: $.title || $.name ||
            'Unknown Alert',\\n  status: $.status === 'resolved' ? 'resolved' : 'firing',\\n  description: $.description ||
            $.message || '',\\n  sourceURL: $.url || $.link || '',\\n  metadata: { team: $.team, severity: $.severity
            }\\n}"}

    Attributes:
        deduplication_key_path (str): JSON path to extract the deduplication key from the payload Example: $.alert_id.
        transform_expression (str): JavaScript expression that returns an object with all alert fields Example: return {
              title: $.title || $.name || 'Unknown Alert',
              status: $.status === 'resolved' ? 'resolved' : 'firing',
              description: $.description || $.message || '',
              sourceURL: $.url || $.link || '',
              metadata: { team: $.team, severity: $.severity }
            }.
    """

    deduplication_key_path: str
    transform_expression: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deduplication_key_path = self.deduplication_key_path

        transform_expression = self.transform_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deduplication_key_path": deduplication_key_path,
                "transform_expression": transform_expression,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        deduplication_key_path = d.pop("deduplication_key_path")

        transform_expression = d.pop("transform_expression")

        alert_source_http_custom_options_v2 = cls(
            deduplication_key_path=deduplication_key_path,
            transform_expression=transform_expression,
        )

        alert_source_http_custom_options_v2.additional_properties = d
        return alert_source_http_custom_options_v2

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
