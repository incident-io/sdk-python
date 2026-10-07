from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogExtensionPluginCreatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogExtensionPluginCreatedMetadataV2:
    """
    Example:
        {'provider': 'github', 'repo_name': 'oncall-plugins', 'repo_owner': 'acme', 'subpath': 'plugins/acme-oncall'}

    Attributes:
        provider (str): The source control provider the plugin's repository lives in (github, gitlab) Example: github.
        repo_name (str): The name of the plugin's repository Example: oncall-plugins.
        repo_owner (str): The owner of the plugin's repository, including any GitLab group path Example: acme.
        subpath (str | Unset): The plugin's directory within the repository, absent when the plugin is the repository
            root Example: plugins/acme-oncall.
    """

    provider: str
    repo_name: str
    repo_owner: str
    subpath: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        repo_name = self.repo_name

        repo_owner = self.repo_owner

        subpath = self.subpath

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "repo_name": repo_name,
                "repo_owner": repo_owner,
            }
        )
        if subpath is not UNSET:
            field_dict["subpath"] = subpath

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = d.pop("provider")

        repo_name = d.pop("repo_name")

        repo_owner = d.pop("repo_owner")

        subpath = d.pop("subpath", UNSET)

        audit_log_extension_plugin_created_metadata_v2 = cls(
            provider=provider,
            repo_name=repo_name,
            repo_owner=repo_owner,
            subpath=subpath,
        )

        audit_log_extension_plugin_created_metadata_v2.additional_properties = d
        return audit_log_extension_plugin_created_metadata_v2

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
