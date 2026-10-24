from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogInvestigationConfigUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogInvestigationConfigUpdatedMetadataV2:
    """
    Example:
        {'after_auto_merge_mode': 'auto', 'after_auto_run_mode': 'on', 'after_evaluate_auto_run_on_incident_update':
            'true', 'after_hide_progress_thread': 'true', 'after_propose_code_changes_mode': 'on', 'after_status':
            'enabled', 'after_summary_template': 'compact', 'before_auto_merge_mode': 'suggest', 'before_auto_run_mode':
            'off', 'before_evaluate_auto_run_on_incident_update': 'false', 'before_hide_progress_thread': 'false',
            'before_propose_code_changes_mode': 'off', 'before_status': 'disabled', 'before_summary_template': 'default',
            'changed': 'auto_run_mode,auto_merge_mode'}

    Attributes:
        changed (str): What the update changed, comma separated (status, auto_run_mode, condition_groups,
            evaluate_auto_run_on_incident_update, auto_merge_mode, propose_code_changes_mode, tuneables,
            hide_progress_thread, summary_template) Example: auto_run_mode,auto_merge_mode.
        after_auto_merge_mode (str | Unset): What an investigation does with a duplicate incident after the change
            (suggest, auto) Example: auto.
        after_auto_run_mode (str | Unset): When investigations start on their own after the change (off, silent, on,
            conditional) Example: on.
        after_evaluate_auto_run_on_incident_update (str | Unset): Whether conditional auto-run is re-checked on incident
            updates after the change (true, false) Example: true.
        after_hide_progress_thread (str | Unset): Whether the progress thread is hidden after the change (true, false)
            Example: true.
        after_propose_code_changes_mode (str | Unset): Whether investigations can open code change tasks on their own
            after the change (off, on) Example: on.
        after_status (str | Unset): Whether investigations are switched on after the change (enabled,
            scheduled_for_enable, disabled) Example: enabled.
        after_summary_template (str | Unset): The summary template used after the change (default, compact) Example:
            compact.
        before_auto_merge_mode (str | Unset): What an investigation did with a duplicate incident before the change
            (suggest, auto) Example: suggest.
        before_auto_run_mode (str | Unset): When investigations started on their own before the change (off, silent, on,
            conditional) Example: off.
        before_evaluate_auto_run_on_incident_update (str | Unset): Whether conditional auto-run was re-checked on
            incident updates before the change (true, false) Example: false.
        before_hide_progress_thread (str | Unset): Whether the progress thread was hidden before the change (true,
            false) Example: false.
        before_propose_code_changes_mode (str | Unset): Whether investigations could open code change tasks on their own
            before the change (off, on) Example: off.
        before_status (str | Unset): Whether investigations were switched on before the change (enabled,
            scheduled_for_enable, disabled) Example: disabled.
        before_summary_template (str | Unset): The summary template used before the change (default, compact) Example:
            default.
    """

    changed: str
    after_auto_merge_mode: str | Unset = UNSET
    after_auto_run_mode: str | Unset = UNSET
    after_evaluate_auto_run_on_incident_update: str | Unset = UNSET
    after_hide_progress_thread: str | Unset = UNSET
    after_propose_code_changes_mode: str | Unset = UNSET
    after_status: str | Unset = UNSET
    after_summary_template: str | Unset = UNSET
    before_auto_merge_mode: str | Unset = UNSET
    before_auto_run_mode: str | Unset = UNSET
    before_evaluate_auto_run_on_incident_update: str | Unset = UNSET
    before_hide_progress_thread: str | Unset = UNSET
    before_propose_code_changes_mode: str | Unset = UNSET
    before_status: str | Unset = UNSET
    before_summary_template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        after_auto_merge_mode = self.after_auto_merge_mode

        after_auto_run_mode = self.after_auto_run_mode

        after_evaluate_auto_run_on_incident_update = (
            self.after_evaluate_auto_run_on_incident_update
        )

        after_hide_progress_thread = self.after_hide_progress_thread

        after_propose_code_changes_mode = self.after_propose_code_changes_mode

        after_status = self.after_status

        after_summary_template = self.after_summary_template

        before_auto_merge_mode = self.before_auto_merge_mode

        before_auto_run_mode = self.before_auto_run_mode

        before_evaluate_auto_run_on_incident_update = (
            self.before_evaluate_auto_run_on_incident_update
        )

        before_hide_progress_thread = self.before_hide_progress_thread

        before_propose_code_changes_mode = self.before_propose_code_changes_mode

        before_status = self.before_status

        before_summary_template = self.before_summary_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
            }
        )
        if after_auto_merge_mode is not UNSET:
            field_dict["after_auto_merge_mode"] = after_auto_merge_mode
        if after_auto_run_mode is not UNSET:
            field_dict["after_auto_run_mode"] = after_auto_run_mode
        if after_evaluate_auto_run_on_incident_update is not UNSET:
            field_dict["after_evaluate_auto_run_on_incident_update"] = (
                after_evaluate_auto_run_on_incident_update
            )
        if after_hide_progress_thread is not UNSET:
            field_dict["after_hide_progress_thread"] = after_hide_progress_thread
        if after_propose_code_changes_mode is not UNSET:
            field_dict["after_propose_code_changes_mode"] = (
                after_propose_code_changes_mode
            )
        if after_status is not UNSET:
            field_dict["after_status"] = after_status
        if after_summary_template is not UNSET:
            field_dict["after_summary_template"] = after_summary_template
        if before_auto_merge_mode is not UNSET:
            field_dict["before_auto_merge_mode"] = before_auto_merge_mode
        if before_auto_run_mode is not UNSET:
            field_dict["before_auto_run_mode"] = before_auto_run_mode
        if before_evaluate_auto_run_on_incident_update is not UNSET:
            field_dict["before_evaluate_auto_run_on_incident_update"] = (
                before_evaluate_auto_run_on_incident_update
            )
        if before_hide_progress_thread is not UNSET:
            field_dict["before_hide_progress_thread"] = before_hide_progress_thread
        if before_propose_code_changes_mode is not UNSET:
            field_dict["before_propose_code_changes_mode"] = (
                before_propose_code_changes_mode
            )
        if before_status is not UNSET:
            field_dict["before_status"] = before_status
        if before_summary_template is not UNSET:
            field_dict["before_summary_template"] = before_summary_template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed = d.pop("changed")

        after_auto_merge_mode = d.pop("after_auto_merge_mode", UNSET)

        after_auto_run_mode = d.pop("after_auto_run_mode", UNSET)

        after_evaluate_auto_run_on_incident_update = d.pop(
            "after_evaluate_auto_run_on_incident_update", UNSET
        )

        after_hide_progress_thread = d.pop("after_hide_progress_thread", UNSET)

        after_propose_code_changes_mode = d.pop(
            "after_propose_code_changes_mode", UNSET
        )

        after_status = d.pop("after_status", UNSET)

        after_summary_template = d.pop("after_summary_template", UNSET)

        before_auto_merge_mode = d.pop("before_auto_merge_mode", UNSET)

        before_auto_run_mode = d.pop("before_auto_run_mode", UNSET)

        before_evaluate_auto_run_on_incident_update = d.pop(
            "before_evaluate_auto_run_on_incident_update", UNSET
        )

        before_hide_progress_thread = d.pop("before_hide_progress_thread", UNSET)

        before_propose_code_changes_mode = d.pop(
            "before_propose_code_changes_mode", UNSET
        )

        before_status = d.pop("before_status", UNSET)

        before_summary_template = d.pop("before_summary_template", UNSET)

        audit_log_investigation_config_updated_metadata_v2 = cls(
            changed=changed,
            after_auto_merge_mode=after_auto_merge_mode,
            after_auto_run_mode=after_auto_run_mode,
            after_evaluate_auto_run_on_incident_update=after_evaluate_auto_run_on_incident_update,
            after_hide_progress_thread=after_hide_progress_thread,
            after_propose_code_changes_mode=after_propose_code_changes_mode,
            after_status=after_status,
            after_summary_template=after_summary_template,
            before_auto_merge_mode=before_auto_merge_mode,
            before_auto_run_mode=before_auto_run_mode,
            before_evaluate_auto_run_on_incident_update=before_evaluate_auto_run_on_incident_update,
            before_hide_progress_thread=before_hide_progress_thread,
            before_propose_code_changes_mode=before_propose_code_changes_mode,
            before_status=before_status,
            before_summary_template=before_summary_template,
        )

        audit_log_investigation_config_updated_metadata_v2.additional_properties = d
        return audit_log_investigation_config_updated_metadata_v2

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
