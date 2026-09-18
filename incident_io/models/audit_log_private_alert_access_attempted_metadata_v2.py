from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_private_alert_access_attempted_metadata_v2_outcome import (
    AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogPrivateAlertAccessAttemptedMetadataV2")


@_attrs_define
class AuditLogPrivateAlertAccessAttemptedMetadataV2:
    """
    Example:
        {'outcome': 'granted'}

    Attributes:
        outcome (AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome | Unset): Whether or not the user was able to
            access the private alert Example: granted.
    """

    outcome: AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _outcome = d.pop("outcome", UNSET)
        outcome: AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = AuditLogPrivateAlertAccessAttemptedMetadataV2Outcome(_outcome)

        audit_log_private_alert_access_attempted_metadata_v2 = cls(
            outcome=outcome,
        )

        audit_log_private_alert_access_attempted_metadata_v2.additional_properties = d
        return audit_log_private_alert_access_attempted_metadata_v2

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
