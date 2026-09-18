from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.follow_ups_connect_external_issue_payload_v3_provider import (
    FollowUpsConnectExternalIssuePayloadV3Provider,
)

T = TypeVar("T", bound="FollowUpsConnectExternalIssuePayloadV3")


@_attrs_define
class FollowUpsConnectExternalIssuePayloadV3:
    """
    Example:
        {'provider': 'linear', 'url': 'https://linear.app/incident/issue/INC-123'}

    Attributes:
        provider (FollowUpsConnectExternalIssuePayloadV3Provider): The issue tracker provider the issue belongs to
            Example: linear.
        url (str): URL of the issue in the external provider Example: https://linear.app/incident/issue/INC-123.
    """

    provider: FollowUpsConnectExternalIssuePayloadV3Provider
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = FollowUpsConnectExternalIssuePayloadV3Provider(d.pop("provider"))

        url = d.pop("url")

        follow_ups_connect_external_issue_payload_v3 = cls(
            provider=provider,
            url=url,
        )

        follow_ups_connect_external_issue_payload_v3.additional_properties = d
        return follow_ups_connect_external_issue_payload_v3

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
