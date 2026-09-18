from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_private_insights_underlying_data_queried_metadata_v2_outcome import (
    AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2")


@_attrs_define
class AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2:
    """
    Example:
        {'measure': 'alert_volume', 'outcome': 'granted'}

    Attributes:
        measure (str | Unset): Name of the Insights measure Example: alert_volume.
        outcome (AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome | Unset): Whether or not the user was
            able to access private Insights data Example: granted.
    """

    measure: str | Unset = UNSET
    outcome: AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measure = self.measure

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measure is not UNSET:
            field_dict["measure"] = measure
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        measure = d.pop("measure", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome(
                _outcome
            )

        audit_log_private_insights_underlying_data_queried_metadata_v2 = cls(
            measure=measure,
            outcome=outcome,
        )

        audit_log_private_insights_underlying_data_queried_metadata_v2.additional_properties = d
        return audit_log_private_insights_underlying_data_queried_metadata_v2

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
