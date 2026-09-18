from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_private_incident_access_attempted_metadata_v2v2_access_type import (
    AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType,
)
from ..models.audit_log_private_incident_access_attempted_metadata_v2v2_outcome import (
    AuditLogPrivateIncidentAccessAttemptedMetadataV2V2Outcome,
)

T = TypeVar("T", bound="AuditLogPrivateIncidentAccessAttemptedMetadataV2V2")


@_attrs_define
class AuditLogPrivateIncidentAccessAttemptedMetadataV2V2:
    """
    Example:
        {'access_type': 'N/A', 'outcome': 'granted', 'team_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        access_type (AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType): How the user was granted access to
            the private incident, or N/A when access was denied Example: N/A.
        outcome (AuditLogPrivateIncidentAccessAttemptedMetadataV2V2Outcome): Whether or not the user was able to access
            the private incident Example: granted.
        team_id (str): The ID of the team through which access was granted, or N/A when access_type is not
            team_membership Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    access_type: AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType
    outcome: AuditLogPrivateIncidentAccessAttemptedMetadataV2V2Outcome
    team_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_type = self.access_type.value

        outcome = self.outcome.value

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_type": access_type,
                "outcome": outcome,
                "team_id": team_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_type = AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType(
            d.pop("access_type")
        )

        outcome = AuditLogPrivateIncidentAccessAttemptedMetadataV2V2Outcome(
            d.pop("outcome")
        )

        team_id = d.pop("team_id")

        audit_log_private_incident_access_attempted_metadata_v2v2 = cls(
            access_type=access_type,
            outcome=outcome,
            team_id=team_id,
        )

        audit_log_private_incident_access_attempted_metadata_v2v2.additional_properties = d
        return audit_log_private_incident_access_attempted_metadata_v2v2

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
