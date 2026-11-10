from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogReliabilityReviewRuleCreatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogReliabilityReviewRuleCreatedMetadataV2:
    """
    Example:
        {'kind': 'flag', 'origin': 'user', 'repository_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'severity': 'high'}

    Attributes:
        kind (str): Whether the rule tells the review to look for something or not to raise it (flag, ignore) Example:
            flag.
        origin (str): How the rule came to exist (user, dont_raise_again, remember_reply) Example: user.
        repository_id (str): The repository the rule applies to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        severity (str | Unset): The rule's severity (high, medium, low). Absent when it has none Example: high.
    """

    kind: str
    origin: str
    repository_id: str
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        origin = self.origin

        repository_id = self.repository_id

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "origin": origin,
                "repository_id": repository_id,
            }
        )
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = d.pop("kind")

        origin = d.pop("origin")

        repository_id = d.pop("repository_id")

        severity = d.pop("severity", UNSET)

        audit_log_reliability_review_rule_created_metadata_v2 = cls(
            kind=kind,
            origin=origin,
            repository_id=repository_id,
            severity=severity,
        )

        audit_log_reliability_review_rule_created_metadata_v2.additional_properties = d
        return audit_log_reliability_review_rule_created_metadata_v2

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
