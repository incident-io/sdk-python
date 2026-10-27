from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogReliabilityReviewSpendLimitUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogReliabilityReviewSpendLimitUpdatedMetadataV2:
    """
    Example:
        {'after_spend_limit_cents': '100000', 'before_spend_limit_cents': '50000'}

    Attributes:
        after_spend_limit_cents (str | Unset): The monthly spend limit after the change, in cents. Absent when there is
            no limit Example: 100000.
        before_spend_limit_cents (str | Unset): The monthly spend limit before the change, in cents. Absent when there
            was no limit Example: 50000.
    """

    after_spend_limit_cents: str | Unset = UNSET
    before_spend_limit_cents: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_spend_limit_cents = self.after_spend_limit_cents

        before_spend_limit_cents = self.before_spend_limit_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_spend_limit_cents is not UNSET:
            field_dict["after_spend_limit_cents"] = after_spend_limit_cents
        if before_spend_limit_cents is not UNSET:
            field_dict["before_spend_limit_cents"] = before_spend_limit_cents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_spend_limit_cents = d.pop("after_spend_limit_cents", UNSET)

        before_spend_limit_cents = d.pop("before_spend_limit_cents", UNSET)

        audit_log_reliability_review_spend_limit_updated_metadata_v2 = cls(
            after_spend_limit_cents=after_spend_limit_cents,
            before_spend_limit_cents=before_spend_limit_cents,
        )

        audit_log_reliability_review_spend_limit_updated_metadata_v2.additional_properties = d
        return audit_log_reliability_review_spend_limit_updated_metadata_v2

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
