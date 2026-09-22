from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertsAddTagsPayloadV2")


@_attrs_define(kw_only=True)
class AlertsAddTagsPayloadV2:
    """
    Example:
        {'tags': ['known issue', 'customer impacting']}

    Attributes:
        tags (list[str]): Tag names to add to this alert Example: ['known issue', 'customer impacting'].
    """

    tags: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags"))

        alerts_add_tags_payload_v2 = cls(
            tags=tags,
        )

        alerts_add_tags_payload_v2.additional_properties = d
        return alerts_add_tags_payload_v2

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
