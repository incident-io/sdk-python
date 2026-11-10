from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogReliabilityReviewRuleUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogReliabilityReviewRuleUpdatedMetadataV2:
    """
    Example:
        {'after_kind': 'ignore', 'after_repository_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'after_severity': 'high',
            'before_kind': 'flag', 'before_repository_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'before_severity': 'medium',
            'changed': 'body,paths', 'disabled': 'true', 'locked': 'true', 'new_rule_id': '01FCNDV6P870EA6S7TK1DSYDG2'}

    Attributes:
        changed (str): What the change changed, comma separated (title, body, kind, severity, examples, repository,
            paths, disabled, locked, restored) Example: body,paths.
        after_kind (str | Unset): The rule's kind after the change (flag, ignore) Example: ignore.
        after_repository_id (str | Unset): The repository the rule applies to after the change Example:
            01FCNDV6P870EA6S7TK1DSYDG1.
        after_severity (str | Unset): The rule's severity after the change (high, medium, low). Absent when it has none
            Example: high.
        before_kind (str | Unset): The rule's kind before the change (flag, ignore) Example: flag.
        before_repository_id (str | Unset): The repository the rule applied to before the change Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        before_severity (str | Unset): The rule's severity before the change (high, medium, low). Absent when it had
            none Example: medium.
        disabled (str | Unset): Whether the rule is switched off after the change (true, false) Example: true.
        locked (str | Unset): Whether the rule is locked after the change (true, false) Example: true.
        new_rule_id (str | Unset): The rule that replaced this one, when the change made a new version of it Example:
            01FCNDV6P870EA6S7TK1DSYDG2.
    """

    changed: str
    after_kind: str | Unset = UNSET
    after_repository_id: str | Unset = UNSET
    after_severity: str | Unset = UNSET
    before_kind: str | Unset = UNSET
    before_repository_id: str | Unset = UNSET
    before_severity: str | Unset = UNSET
    disabled: str | Unset = UNSET
    locked: str | Unset = UNSET
    new_rule_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        after_kind = self.after_kind

        after_repository_id = self.after_repository_id

        after_severity = self.after_severity

        before_kind = self.before_kind

        before_repository_id = self.before_repository_id

        before_severity = self.before_severity

        disabled = self.disabled

        locked = self.locked

        new_rule_id = self.new_rule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
            }
        )
        if after_kind is not UNSET:
            field_dict["after_kind"] = after_kind
        if after_repository_id is not UNSET:
            field_dict["after_repository_id"] = after_repository_id
        if after_severity is not UNSET:
            field_dict["after_severity"] = after_severity
        if before_kind is not UNSET:
            field_dict["before_kind"] = before_kind
        if before_repository_id is not UNSET:
            field_dict["before_repository_id"] = before_repository_id
        if before_severity is not UNSET:
            field_dict["before_severity"] = before_severity
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if locked is not UNSET:
            field_dict["locked"] = locked
        if new_rule_id is not UNSET:
            field_dict["new_rule_id"] = new_rule_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed = d.pop("changed")

        after_kind = d.pop("after_kind", UNSET)

        after_repository_id = d.pop("after_repository_id", UNSET)

        after_severity = d.pop("after_severity", UNSET)

        before_kind = d.pop("before_kind", UNSET)

        before_repository_id = d.pop("before_repository_id", UNSET)

        before_severity = d.pop("before_severity", UNSET)

        disabled = d.pop("disabled", UNSET)

        locked = d.pop("locked", UNSET)

        new_rule_id = d.pop("new_rule_id", UNSET)

        audit_log_reliability_review_rule_updated_metadata_v2 = cls(
            changed=changed,
            after_kind=after_kind,
            after_repository_id=after_repository_id,
            after_severity=after_severity,
            before_kind=before_kind,
            before_repository_id=before_repository_id,
            before_severity=before_severity,
            disabled=disabled,
            locked=locked,
            new_rule_id=new_rule_id,
        )

        audit_log_reliability_review_rule_updated_metadata_v2.additional_properties = d
        return audit_log_reliability_review_rule_updated_metadata_v2

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
