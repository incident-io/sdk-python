from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostmortemDocumentsShowContentResultV1")


@_attrs_define(kw_only=True)
class PostmortemDocumentsShowContentResultV1:
    """
    Example:
        {'markdown': '# Incident Postmortem\\n\\n## Summary\\n\\nThis incident was investigated by Alice Smith and
            affected the API Gateway service.\\n\\n## Timeline\\n\\n### 2024-06-15 (UTC)\\n\\n* [10:30] **Alert
            fired**\\n\\n* [10:35] **Incident declared**\\n\\n## Follow-ups\\n\\n* **Add monitoring** - Assignee: Alice
            Smith\\n'}

    Attributes:
        markdown (str): The full content of the post-mortem document, rendered as markdown. Includes all sections,
            resolved mentions, timeline, follow-ups, and custom fields. Example: # Incident Postmortem

            ## Summary

            This incident was investigated by Alice Smith and affected the API Gateway service.

            ## Timeline

            ### 2024-06-15 (UTC)

            * [10:30] **Alert fired**

            * [10:35] **Incident declared**

            ## Follow-ups

            * **Add monitoring** - Assignee: Alice Smith
            .
    """

    markdown: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markdown = self.markdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markdown": markdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        markdown = d.pop("markdown")

        postmortem_documents_show_content_result_v1 = cls(
            markdown=markdown,
        )

        postmortem_documents_show_content_result_v1.additional_properties = d
        return postmortem_documents_show_content_result_v1

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
