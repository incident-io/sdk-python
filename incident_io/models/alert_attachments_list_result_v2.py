from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attachment_v2 import AlertAttachmentV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="AlertAttachmentsListResultV2")


@_attrs_define(kw_only=True)
class AlertAttachmentsListResultV2:
    """
    Example:
        {'alert_attachments': [{'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2026-10-23T15:30:00Z', 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'title':
            'Tune the disk usage alert', 'url': 'https://linear.app/acme/issue/ENG-123'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        alert_attachments (list[AlertAttachmentV2]):  Example: [{'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS',
            'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2026-10-23T15:30:00Z', 'id':
            '01J1X9J85C7Y12G8P8W8K55Q5Y', 'title': 'Tune the disk usage alert', 'url':
            'https://linear.app/acme/issue/ENG-123'}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    alert_attachments: list[AlertAttachmentV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_attachments = []
        for alert_attachments_item_data in self.alert_attachments:
            alert_attachments_item = alert_attachments_item_data.to_dict()
            alert_attachments.append(alert_attachments_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_attachments": alert_attachments,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attachment_v2 import AlertAttachmentV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        alert_attachments = []
        _alert_attachments = d.pop("alert_attachments")
        for alert_attachments_item_data in _alert_attachments:
            alert_attachments_item = AlertAttachmentV2.from_dict(
                alert_attachments_item_data
            )

            alert_attachments.append(alert_attachments_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        alert_attachments_list_result_v2 = cls(
            alert_attachments=alert_attachments,
            pagination_meta=pagination_meta,
        )

        alert_attachments_list_result_v2.additional_properties = d
        return alert_attachments_list_result_v2

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
