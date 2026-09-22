from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_issue_reference_v2_provider import (
    ExternalIssueReferenceV2Provider,
)

T = TypeVar("T", bound="ExternalIssueReferenceV2")


@_attrs_define(kw_only=True)
class ExternalIssueReferenceV2:
    """
    Example:
        {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}

    Attributes:
        issue_name (str): Human readable ID for the issue Example: INC-123.
        issue_permalink (str): URL linking directly to the action in the issue tracker Example:
            https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up.
        provider (ExternalIssueReferenceV2Provider): ID of the issue tracker provider Example: asana.
    """

    issue_name: str
    issue_permalink: str
    provider: ExternalIssueReferenceV2Provider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_name = self.issue_name

        issue_permalink = self.issue_permalink

        provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_name": issue_name,
                "issue_permalink": issue_permalink,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issue_name = d.pop("issue_name")

        issue_permalink = d.pop("issue_permalink")

        provider = ExternalIssueReferenceV2Provider(d.pop("provider"))

        external_issue_reference_v2 = cls(
            issue_name=issue_name,
            issue_permalink=issue_permalink,
            provider=provider,
        )

        external_issue_reference_v2.additional_properties = d
        return external_issue_reference_v2

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
