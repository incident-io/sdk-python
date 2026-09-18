from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSourceRateLimitShardingV2")


@_attrs_define
class AlertSourceRateLimitShardingV2:
    """Controls how this source's ingest rate limit is split into buckets.

    Example:
        {'rate_limit_shard_key_path': '$.priority'}

    Attributes:
        rate_limit_shard_key_path (str): JSON path to a value that splits this source's rate limit into per-value
            buckets. Default: ''. Example: $.priority.
    """

    rate_limit_shard_key_path: str = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_limit_shard_key_path = self.rate_limit_shard_key_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rate_limit_shard_key_path": rate_limit_shard_key_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rate_limit_shard_key_path = d.pop("rate_limit_shard_key_path")

        alert_source_rate_limit_sharding_v2 = cls(
            rate_limit_shard_key_path=rate_limit_shard_key_path,
        )

        alert_source_rate_limit_sharding_v2.additional_properties = d
        return alert_source_rate_limit_sharding_v2

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
