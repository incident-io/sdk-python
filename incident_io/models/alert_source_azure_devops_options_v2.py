from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSourceAzureDevopsOptionsV2")


@_attrs_define
class AlertSourceAzureDevopsOptionsV2:
    """
    Example:
        {'project_ids': ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483']}

    Attributes:
        project_ids (list[str]): Which Azure DevOps projects should this alert source watch for work item updates? IDs
            can either be IDs of the projects in Azure DevOps, or IDs of catalog entries in the 'Azure DevOps Project'
            catalog type. Example: ['01GBSQF3FHF7FWZQNWGHAVQ804', 'ba038695-f5f7-4490-a9ea-bf4ab3cbf483'].
    """

    project_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_ids = self.project_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_ids": project_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        project_ids = cast(list[str], d.pop("project_ids"))

        alert_source_azure_devops_options_v2 = cls(
            project_ids=project_ids,
        )

        alert_source_azure_devops_options_v2.additional_properties = d
        return alert_source_azure_devops_options_v2

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
