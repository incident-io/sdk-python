from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogExtensionPluginUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogExtensionPluginUpdatedMetadataV2:
    """
    Example:
        {'after_enabled': 'true', 'after_enabled_skill_count': '2', 'after_name': 'acme-oncall', 'after_provider':
            'github', 'after_repo_name': 'oncall-plugins', 'after_repo_owner': 'acme-forks', 'after_skill_selection_mode':
            'selected', 'after_subpath': 'plugins/acme-oncall', 'before_enabled': 'false', 'before_enabled_skill_count':
            '4', 'before_name': 'oncall', 'before_provider': 'github', 'before_repo_name': 'oncall-plugins',
            'before_repo_owner': 'acme', 'before_skill_selection_mode': 'automatic', 'before_subpath': 'plugins/acme-
            oncall', 'changed': 'location'}

    Attributes:
        changed (str): What the update changed, comma separated (enabled, skill_selection, name, location) Example:
            location.
        after_enabled (str | Unset): Whether the plugin is mounted into agent runs after the change (true, false)
            Example: true.
        after_enabled_skill_count (str | Unset): How many skills are selected after the change, absent when every skill
            loads Example: 2.
        after_name (str | Unset): The plugin's name after the change Example: acme-oncall.
        after_provider (str | Unset): The source control provider of the plugin's new repository (github, gitlab)
            Example: github.
        after_repo_name (str | Unset): The name of the plugin's new repository Example: oncall-plugins.
        after_repo_owner (str | Unset): The owner of the plugin's new repository Example: acme-forks.
        after_skill_selection_mode (str | Unset): Which skills load after the change: every skill, or only the selected
            ones (automatic, selected) Example: selected.
        after_subpath (str | Unset): The plugin's new directory within its repository, absent when it is the repository
            root Example: plugins/acme-oncall.
        before_enabled (str | Unset): Whether the plugin was mounted into agent runs before the change (true, false)
            Example: false.
        before_enabled_skill_count (str | Unset): How many skills were selected before the change, absent when every
            skill loaded Example: 4.
        before_name (str | Unset): The plugin's name before the change Example: oncall.
        before_provider (str | Unset): The source control provider of the plugin's previous repository (github, gitlab)
            Example: github.
        before_repo_name (str | Unset): The name of the plugin's previous repository Example: oncall-plugins.
        before_repo_owner (str | Unset): The owner of the plugin's previous repository Example: acme.
        before_skill_selection_mode (str | Unset): Which skills loaded before the change: every skill, or only the
            selected ones (automatic, selected) Example: automatic.
        before_subpath (str | Unset): The plugin's previous directory within its repository, absent when it was the
            repository root Example: plugins/acme-oncall.
    """

    changed: str
    after_enabled: str | Unset = UNSET
    after_enabled_skill_count: str | Unset = UNSET
    after_name: str | Unset = UNSET
    after_provider: str | Unset = UNSET
    after_repo_name: str | Unset = UNSET
    after_repo_owner: str | Unset = UNSET
    after_skill_selection_mode: str | Unset = UNSET
    after_subpath: str | Unset = UNSET
    before_enabled: str | Unset = UNSET
    before_enabled_skill_count: str | Unset = UNSET
    before_name: str | Unset = UNSET
    before_provider: str | Unset = UNSET
    before_repo_name: str | Unset = UNSET
    before_repo_owner: str | Unset = UNSET
    before_skill_selection_mode: str | Unset = UNSET
    before_subpath: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        after_enabled = self.after_enabled

        after_enabled_skill_count = self.after_enabled_skill_count

        after_name = self.after_name

        after_provider = self.after_provider

        after_repo_name = self.after_repo_name

        after_repo_owner = self.after_repo_owner

        after_skill_selection_mode = self.after_skill_selection_mode

        after_subpath = self.after_subpath

        before_enabled = self.before_enabled

        before_enabled_skill_count = self.before_enabled_skill_count

        before_name = self.before_name

        before_provider = self.before_provider

        before_repo_name = self.before_repo_name

        before_repo_owner = self.before_repo_owner

        before_skill_selection_mode = self.before_skill_selection_mode

        before_subpath = self.before_subpath

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
            }
        )
        if after_enabled is not UNSET:
            field_dict["after_enabled"] = after_enabled
        if after_enabled_skill_count is not UNSET:
            field_dict["after_enabled_skill_count"] = after_enabled_skill_count
        if after_name is not UNSET:
            field_dict["after_name"] = after_name
        if after_provider is not UNSET:
            field_dict["after_provider"] = after_provider
        if after_repo_name is not UNSET:
            field_dict["after_repo_name"] = after_repo_name
        if after_repo_owner is not UNSET:
            field_dict["after_repo_owner"] = after_repo_owner
        if after_skill_selection_mode is not UNSET:
            field_dict["after_skill_selection_mode"] = after_skill_selection_mode
        if after_subpath is not UNSET:
            field_dict["after_subpath"] = after_subpath
        if before_enabled is not UNSET:
            field_dict["before_enabled"] = before_enabled
        if before_enabled_skill_count is not UNSET:
            field_dict["before_enabled_skill_count"] = before_enabled_skill_count
        if before_name is not UNSET:
            field_dict["before_name"] = before_name
        if before_provider is not UNSET:
            field_dict["before_provider"] = before_provider
        if before_repo_name is not UNSET:
            field_dict["before_repo_name"] = before_repo_name
        if before_repo_owner is not UNSET:
            field_dict["before_repo_owner"] = before_repo_owner
        if before_skill_selection_mode is not UNSET:
            field_dict["before_skill_selection_mode"] = before_skill_selection_mode
        if before_subpath is not UNSET:
            field_dict["before_subpath"] = before_subpath

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed = d.pop("changed")

        after_enabled = d.pop("after_enabled", UNSET)

        after_enabled_skill_count = d.pop("after_enabled_skill_count", UNSET)

        after_name = d.pop("after_name", UNSET)

        after_provider = d.pop("after_provider", UNSET)

        after_repo_name = d.pop("after_repo_name", UNSET)

        after_repo_owner = d.pop("after_repo_owner", UNSET)

        after_skill_selection_mode = d.pop("after_skill_selection_mode", UNSET)

        after_subpath = d.pop("after_subpath", UNSET)

        before_enabled = d.pop("before_enabled", UNSET)

        before_enabled_skill_count = d.pop("before_enabled_skill_count", UNSET)

        before_name = d.pop("before_name", UNSET)

        before_provider = d.pop("before_provider", UNSET)

        before_repo_name = d.pop("before_repo_name", UNSET)

        before_repo_owner = d.pop("before_repo_owner", UNSET)

        before_skill_selection_mode = d.pop("before_skill_selection_mode", UNSET)

        before_subpath = d.pop("before_subpath", UNSET)

        audit_log_extension_plugin_updated_metadata_v2 = cls(
            changed=changed,
            after_enabled=after_enabled,
            after_enabled_skill_count=after_enabled_skill_count,
            after_name=after_name,
            after_provider=after_provider,
            after_repo_name=after_repo_name,
            after_repo_owner=after_repo_owner,
            after_skill_selection_mode=after_skill_selection_mode,
            after_subpath=after_subpath,
            before_enabled=before_enabled,
            before_enabled_skill_count=before_enabled_skill_count,
            before_name=before_name,
            before_provider=before_provider,
            before_repo_name=before_repo_name,
            before_repo_owner=before_repo_owner,
            before_skill_selection_mode=before_skill_selection_mode,
            before_subpath=before_subpath,
        )

        audit_log_extension_plugin_updated_metadata_v2.additional_properties = d
        return audit_log_extension_plugin_updated_metadata_v2

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
