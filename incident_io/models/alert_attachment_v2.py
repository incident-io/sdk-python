from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertAttachmentV2")


@_attrs_define(kw_only=True)
class AlertAttachmentV2:
    """Something attached to an alert or alert group, such as a ticket, a pull request or
    a link.

        Example:
            {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
                '2026-10-23T15:30:00Z', 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'title': 'Tune the disk usage alert', 'url':
                'https://linear.app/acme/issue/ENG-123'}

        Attributes:
            created_at (datetime.datetime): When it was attached Example: 2026-10-23T15:30:00Z.
            id (str): Unique identifier for the alert attachment Example: 01J1X9J85C7Y12G8P8W8K55Q5Y.
            title (str): The ticket or pull request's title, or the link's title Example: Tune the disk usage alert.
            url (str): URL of the attached ticket, pull request or link Example: https://linear.app/acme/issue/ENG-123.
            alert_group_id (str | Unset): ID of the alert group this is attached to. Exactly one of alert_id or
                alert_group_id is set. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
            alert_id (str | Unset): ID of the alert this is attached to. Exactly one of alert_id or alert_group_id is set.
                Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    created_at: datetime.datetime
    id: str
    title: str
    url: str
    alert_group_id: str | Unset = UNSET
    alert_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        title = self.title

        url = self.url

        alert_group_id = self.alert_group_id

        alert_id = self.alert_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "title": title,
                "url": url,
            }
        )
        if alert_group_id is not UNSET:
            field_dict["alert_group_id"] = alert_group_id
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        title = d.pop("title")

        url = d.pop("url")

        alert_group_id = d.pop("alert_group_id", UNSET)

        alert_id = d.pop("alert_id", UNSET)

        alert_attachment_v2 = cls(
            created_at=created_at,
            id=id,
            title=title,
            url=url,
            alert_group_id=alert_group_id,
            alert_id=alert_id,
        )

        alert_attachment_v2.additional_properties = d
        return alert_attachment_v2

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
