from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_attachment_v2 import AlertAttachmentV2


T = TypeVar("T", bound="AlertAttachmentsCreateResultV2")


@_attrs_define(kw_only=True)
class AlertAttachmentsCreateResultV2:
    """
    Example:
        {'alert_attachment': {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2026-10-23T15:30:00Z', 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'title': 'Tune the disk usage alert',
            'url': 'https://linear.app/acme/issue/ENG-123'}}

    Attributes:
        alert_attachment (AlertAttachmentV2): Something attached to an alert or alert group, such as a ticket, a pull
            request or
            a link. Example: {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2026-10-23T15:30:00Z', 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'title': 'Tune the disk usage alert',
            'url': 'https://linear.app/acme/issue/ENG-123'}.
    """

    alert_attachment: AlertAttachmentV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_attachment = self.alert_attachment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_attachment": alert_attachment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attachment_v2 import AlertAttachmentV2

        d = dict(src_dict)
        alert_attachment = AlertAttachmentV2.from_dict(d.pop("alert_attachment"))

        alert_attachments_create_result_v2 = cls(
            alert_attachment=alert_attachment,
        )

        alert_attachments_create_result_v2.additional_properties = d
        return alert_attachments_create_result_v2

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
