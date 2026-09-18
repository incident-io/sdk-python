from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PayReportsUnpublishPayloadV2")


@_attrs_define
class PayReportsUnpublishPayloadV2:
    """
    Example:
        {'unpublish_reason': 'The date range is wrong and one schedule was incorrectly synced.'}

    Attributes:
        unpublish_reason (str): Why this report is being unpublished Example: The date range is wrong and one schedule
            was incorrectly synced..
    """

    unpublish_reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unpublish_reason = self.unpublish_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unpublish_reason": unpublish_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unpublish_reason = d.pop("unpublish_reason")

        pay_reports_unpublish_payload_v2 = cls(
            unpublish_reason=unpublish_reason,
        )

        pay_reports_unpublish_payload_v2.additional_properties = d
        return pay_reports_unpublish_payload_v2

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
