from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogCodeRepositoryAccessedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogCodeRepositoryAccessedMetadataV2:
    """
    Example:
        {'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'investigation_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'revision_sha': '9fceb02d0ae598e95dc970b74767f19372d61af8', 'run_type':
            'investigation', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        revision_sha (str): The commit the run checked out Example: 9fceb02d0ae598e95dc970b74767f19372d61af8.
        run_type (str): The kind of agent run that read the repository (investigation, chat, code_agent) Example:
            investigation.
        alert_id (str | Unset): ID of the alert the run was for, when known Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str | Unset): ID of the incident the run was for, when known Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        investigation_id (str | Unset): ID of the investigation, when an investigation read the repository Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        user_id (str | Unset): ID of the user who asked, when a chat read the repository Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    revision_sha: str
    run_type: str
    alert_id: str | Unset = UNSET
    incident_id: str | Unset = UNSET
    investigation_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_sha = self.revision_sha

        run_type = self.run_type

        alert_id = self.alert_id

        incident_id = self.incident_id

        investigation_id = self.investigation_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision_sha": revision_sha,
                "run_type": run_type,
            }
        )
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if investigation_id is not UNSET:
            field_dict["investigation_id"] = investigation_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        revision_sha = d.pop("revision_sha")

        run_type = d.pop("run_type")

        alert_id = d.pop("alert_id", UNSET)

        incident_id = d.pop("incident_id", UNSET)

        investigation_id = d.pop("investigation_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        audit_log_code_repository_accessed_metadata_v2 = cls(
            revision_sha=revision_sha,
            run_type=run_type,
            alert_id=alert_id,
            incident_id=incident_id,
            investigation_id=investigation_id,
            user_id=user_id,
        )

        audit_log_code_repository_accessed_metadata_v2.additional_properties = d
        return audit_log_code_repository_accessed_metadata_v2

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
