from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v1 import ActorV1
    from ..models.image_v1 import ImageV1


T = TypeVar("T", bound="AlertNoteV1")


@_attrs_define(kw_only=True)
class AlertNoteV1:
    """
    Example:
        {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content': 'Customer
            reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-api`.\\n\\n- Error rate: ~12% on
            `/checkout`\\n- Region: `eu-west-1`\\n- See [dashboard](https://grafana.example.com/d/abc)\\n', 'created_at':
            '2026-05-28T15:30:00Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'id': '01J1X9J85C7Y12G8P8W8K55Q5Y', 'images': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'url': 'https://storage.googleapis.com/incident-io/images/...'}],
            'last_edited_at': '2026-05-28T15:35:00Z', 'updated_at': '2026-05-28T15:35:00Z'}

    Attributes:
        content (str): Markdown body of the note Example: Customer reports **checkout 500s** starting ~14:32 UTC.
            Investigating `payments-api`.

            - Error rate: ~12% on `/checkout`
            - Region: `eu-west-1`
            - See [dashboard](https://grafana.example.com/d/abc)
            .
        created_at (datetime.datetime): When this note was first created Example: 2026-05-28T15:30:00Z.
        creator (ActorV1):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        id (str): Unique identifier for the alert note Example: 01J1X9J85C7Y12G8P8W8K55Q5Y.
        images (list[ImageV1]): Images attached to the current version of the note, with signed URLs valid for 10
            minutes Example: [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'url': 'https://storage.googleapis.com/incident-
            io/images/...'}].
        updated_at (datetime.datetime): When this note was last updated Example: 2026-05-28T15:35:00Z.
        alert_group_id (str | Unset): ID of the alert group this note is attached to. Exactly one of alert_id or
            alert_group_id is set; the other is null. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        alert_id (str | Unset): ID of the alert this note is attached to. Exactly one of alert_id or alert_group_id is
            set; the other is null. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        last_edited_at (datetime.datetime | Unset): When this note was last edited, only set if it has been edited at
            least once since creation Example: 2026-05-28T15:35:00Z.
    """

    content: str
    created_at: datetime.datetime
    creator: ActorV1
    id: str
    images: list[ImageV1]
    updated_at: datetime.datetime
    alert_group_id: str | Unset = UNSET
    alert_id: str | Unset = UNSET
    last_edited_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        updated_at = self.updated_at.isoformat()

        alert_group_id = self.alert_group_id

        alert_id = self.alert_id

        last_edited_at: str | Unset = UNSET
        if not isinstance(self.last_edited_at, Unset):
            last_edited_at = self.last_edited_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "created_at": created_at,
                "creator": creator,
                "id": id,
                "images": images,
                "updated_at": updated_at,
            }
        )
        if alert_group_id is not UNSET:
            field_dict["alert_group_id"] = alert_group_id
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id
        if last_edited_at is not UNSET:
            field_dict["last_edited_at"] = last_edited_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v1 import ActorV1
        from ..models.image_v1 import ImageV1

        d = dict(src_dict)
        content = d.pop("content")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV1.from_dict(d.pop("creator"))

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = ImageV1.from_dict(images_item_data)

            images.append(images_item)

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alert_group_id = d.pop("alert_group_id", UNSET)

        alert_id = d.pop("alert_id", UNSET)

        _last_edited_at = d.pop("last_edited_at", UNSET)
        last_edited_at: datetime.datetime | Unset
        if isinstance(_last_edited_at, Unset):
            last_edited_at = UNSET
        else:
            last_edited_at = datetime.datetime.fromisoformat(_last_edited_at)

        alert_note_v1 = cls(
            content=content,
            created_at=created_at,
            creator=creator,
            id=id,
            images=images,
            updated_at=updated_at,
            alert_group_id=alert_group_id,
            alert_id=alert_id,
            last_edited_at=last_edited_at,
        )

        alert_note_v1.additional_properties = d
        return alert_note_v1

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
