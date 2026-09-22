from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_note_v1 import AlertNoteV1
    from ..models.pagination_meta_result_v1 import PaginationMetaResultV1


T = TypeVar("T", bound="AlertNotesListResultV1")


@_attrs_define(kw_only=True)
class AlertNotesListResultV1:
    """
    Example:
        {'alert_notes': [{'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'content': 'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-api`.\\n\\n- Error
            rate: ~12% on `/checkout`\\n- Region: `eu-west-1`\\n- See [dashboard](https://grafana.example.com/d/abc)\\n',
            'created_at': '2026-05-28T15:30:00Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'images':
            [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'url': 'https://storage.googleapis.com/incident-io/images/...'}],
            'last_edited_at': '2026-05-28T15:35:00Z', 'updated_at': '2026-05-28T15:35:00Z'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        alert_notes (list[AlertNoteV1]):  Example: [{'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'content': 'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating
            `payments-api`.\\n\\n- Error rate: ~12% on `/checkout`\\n- Region: `eu-west-1`\\n- See
            [dashboard](https://grafana.example.com/d/abc)\\n', 'created_at': '2026-05-28T15:30:00Z', 'creator': {'api_key':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}},
            'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'images': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'url':
            'https://storage.googleapis.com/incident-io/images/...'}], 'last_edited_at': '2026-05-28T15:35:00Z',
            'updated_at': '2026-05-28T15:35:00Z'}].
        pagination_meta (PaginationMetaResultV1):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    alert_notes: list[AlertNoteV1]
    pagination_meta: PaginationMetaResultV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_notes = []
        for alert_notes_item_data in self.alert_notes:
            alert_notes_item = alert_notes_item_data.to_dict()
            alert_notes.append(alert_notes_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_notes": alert_notes,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_note_v1 import AlertNoteV1
        from ..models.pagination_meta_result_v1 import (
            PaginationMetaResultV1,
        )

        d = dict(src_dict)
        alert_notes = []
        _alert_notes = d.pop("alert_notes")
        for alert_notes_item_data in _alert_notes:
            alert_notes_item = AlertNoteV1.from_dict(alert_notes_item_data)

            alert_notes.append(alert_notes_item)

        pagination_meta = PaginationMetaResultV1.from_dict(d.pop("pagination_meta"))

        alert_notes_list_result_v1 = cls(
            alert_notes=alert_notes,
            pagination_meta=pagination_meta,
        )

        alert_notes_list_result_v1.additional_properties = d
        return alert_notes_list_result_v1

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
