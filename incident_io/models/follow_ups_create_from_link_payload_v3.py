from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FollowUpsCreateFromLinkPayloadV3")


@_attrs_define(kw_only=True)
class FollowUpsCreateFromLinkPayloadV3:
    """
    Example:
        {'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'url': 'https://linear.app/incident/issue/INC-123'}

    Attributes:
        incident_id (str): Unique identifier of the incident the follow-up belongs to Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        url (str): URL of the issue in the external provider Example: https://linear.app/incident/issue/INC-123.
    """

    incident_id: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        url = d.pop("url")

        follow_ups_create_from_link_payload_v3 = cls(
            incident_id=incident_id,
            url=url,
        )

        follow_ups_create_from_link_payload_v3.additional_properties = d
        return follow_ups_create_from_link_payload_v3

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
