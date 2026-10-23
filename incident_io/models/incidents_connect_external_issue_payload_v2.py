from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incidents_connect_external_issue_payload_v2_provider import (
    IncidentsConnectExternalIssuePayloadV2Provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentsConnectExternalIssuePayloadV2")


@_attrs_define(kw_only=True)
class IncidentsConnectExternalIssuePayloadV2:
    """
    Example:
        {'issue_template_id': '01GBA8J19SMXQWPJMX3P2ESCVG', 'provider': 'jira', 'replace': False, 'url':
            'https://example.atlassian.net/browse/OPS-42'}

    Attributes:
        issue_template_id (str): ID of the incident ticket template to sync the issue with Example:
            01GBA8J19SMXQWPJMX3P2ESCVG.
        provider (IncidentsConnectExternalIssuePayloadV2Provider): The issue tracker provider the issue belongs to. It
            must match the provider of the incident ticket template. Example: jira.
        url (str): URL of the issue in the issue tracker Example: https://example.atlassian.net/browse/OPS-42.
        replace (bool | Unset): Whether to replace the incident's current external issue, if it has a different one
            Default: False. Example: False.
    """

    issue_template_id: str
    provider: IncidentsConnectExternalIssuePayloadV2Provider
    url: str
    replace: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_template_id = self.issue_template_id

        provider = self.provider.value

        url = self.url

        replace = self.replace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_template_id": issue_template_id,
                "provider": provider,
                "url": url,
            }
        )
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        issue_template_id = d.pop("issue_template_id")

        provider = IncidentsConnectExternalIssuePayloadV2Provider(d.pop("provider"))

        url = d.pop("url")

        replace = d.pop("replace", UNSET)

        incidents_connect_external_issue_payload_v2 = cls(
            issue_template_id=issue_template_id,
            provider=provider,
            url=url,
            replace=replace,
        )

        incidents_connect_external_issue_payload_v2.additional_properties = d
        return incidents_connect_external_issue_payload_v2

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
