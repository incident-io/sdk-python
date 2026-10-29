from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogExtensionConnectorCalledMetadataV5V2")


@_attrs_define(kw_only=True)
class AuditLogExtensionConnectorCalledMetadataV5V2:
    """
    Example:
        {'access_source': 'policy', 'approval_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'approved_by':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'class': 'write', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'investigation_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'outcome': 'requires_approval', 'reason': 'requires_approval', 'source_kind':
            'mcp', 'surface': 'chat', 'telemetry_query_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'write': 'true'}

    Attributes:
        outcome (str): How the call ended (success, error, denied, requires_approval). A denied call was refused by the
            connector's access policy and a requires_approval call is waiting for a person's approval; neither reached the
            connected system Example: requires_approval.
        source_kind (str): The kind of connector that was called (mcp, http) Example: mcp.
        surface (str): The product surface the call ran from (chat, investigation, explore, mcp_client, verify), or
            internal for system paths with no surface Example: chat.
        write (str): Whether the call was permitted to change the connected system (true, false) Example: true.
        access_source (str | Unset): What decided: the connector's access policy, or a decision pinned on this tool
            (policy, override) Example: policy.
        approval_id (str | Unset): ID of the approval request this call executed, when a person's approval is what
            permitted it Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        approved_by (str | Unset): ID of the user who approved the approval request this call executed Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        class_ (str | Unset): What calling the tool does to the connected system, as the tool's own server describes it
            (read, write, destructive, unknown) Example: write.
        incident_id (str | Unset): The incident the call was made for, when incident-scoped Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        investigation_id (str | Unset): The investigation that made the call, when investigation-driven Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        reason (str | Unset): Why the call was allowed, refused or made to wait (allowed, denied_by_rule, disabled,
            unknown_rule_type, rule_not_found, not_read, no_person_present, not_in_allow_list, requires_approval) Example:
            requires_approval.
        telemetry_query_id (str | Unset): ID of our stored record of this call, absent for a call that was refused or is
            waiting for approval Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    outcome: str
    source_kind: str
    surface: str
    write: str
    access_source: str | Unset = UNSET
    approval_id: str | Unset = UNSET
    approved_by: str | Unset = UNSET
    class_: str | Unset = UNSET
    incident_id: str | Unset = UNSET
    investigation_id: str | Unset = UNSET
    reason: str | Unset = UNSET
    telemetry_query_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome

        source_kind = self.source_kind

        surface = self.surface

        write = self.write

        access_source = self.access_source

        approval_id = self.approval_id

        approved_by = self.approved_by

        class_ = self.class_

        incident_id = self.incident_id

        investigation_id = self.investigation_id

        reason = self.reason

        telemetry_query_id = self.telemetry_query_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "source_kind": source_kind,
                "surface": surface,
                "write": write,
            }
        )
        if access_source is not UNSET:
            field_dict["access_source"] = access_source
        if approval_id is not UNSET:
            field_dict["approval_id"] = approval_id
        if approved_by is not UNSET:
            field_dict["approved_by"] = approved_by
        if class_ is not UNSET:
            field_dict["class"] = class_
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if investigation_id is not UNSET:
            field_dict["investigation_id"] = investigation_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if telemetry_query_id is not UNSET:
            field_dict["telemetry_query_id"] = telemetry_query_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        outcome = d.pop("outcome")

        source_kind = d.pop("source_kind")

        surface = d.pop("surface")

        write = d.pop("write")

        access_source = d.pop("access_source", UNSET)

        approval_id = d.pop("approval_id", UNSET)

        approved_by = d.pop("approved_by", UNSET)

        class_ = d.pop("class", UNSET)

        incident_id = d.pop("incident_id", UNSET)

        investigation_id = d.pop("investigation_id", UNSET)

        reason = d.pop("reason", UNSET)

        telemetry_query_id = d.pop("telemetry_query_id", UNSET)

        audit_log_extension_connector_called_metadata_v5v2 = cls(
            outcome=outcome,
            source_kind=source_kind,
            surface=surface,
            write=write,
            access_source=access_source,
            approval_id=approval_id,
            approved_by=approved_by,
            class_=class_,
            incident_id=incident_id,
            investigation_id=investigation_id,
            reason=reason,
            telemetry_query_id=telemetry_query_id,
        )

        audit_log_extension_connector_called_metadata_v5v2.additional_properties = d
        return audit_log_extension_connector_called_metadata_v5v2

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
