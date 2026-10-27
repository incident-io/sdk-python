from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertAttachmentsCreatePayloadV2")


@_attrs_define(kw_only=True)
class AlertAttachmentsCreatePayloadV2:
    """
    Example:
        {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'title': 'Disk usage
            dashboard', 'url': 'https://linear.app/acme/issue/ENG-123'}

    Attributes:
        url (str): The URL to attach Example: https://linear.app/acme/issue/ENG-123.
        alert_group_id (str | Unset): ID of the alert group to attach to. Provide exactly one of alert_id or
            alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        alert_id (str | Unset): ID of the alert to attach to. Provide exactly one of alert_id or alert_group_id.
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        title (str | Unset): Title for a link. Tickets and pull requests use their own title, so we ignore this for
            them. Example: Disk usage dashboard.
    """

    url: str
    alert_group_id: str | Unset = UNSET
    alert_id: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        alert_group_id = self.alert_group_id

        alert_id = self.alert_id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if alert_group_id is not UNSET:
            field_dict["alert_group_id"] = alert_group_id
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        alert_group_id = d.pop("alert_group_id", UNSET)

        alert_id = d.pop("alert_id", UNSET)

        title = d.pop("title", UNSET)

        alert_attachments_create_payload_v2 = cls(
            url=url,
            alert_group_id=alert_group_id,
            alert_id=alert_id,
            title=title,
        )

        alert_attachments_create_payload_v2.additional_properties = d
        return alert_attachments_create_payload_v2

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
