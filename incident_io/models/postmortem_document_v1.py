from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postmortem_document_v1_status import PostmortemDocumentV1Status
from ..models.postmortem_document_v1_type import PostmortemDocumentV1Type

if TYPE_CHECKING:
    from ..models.user_v1 import UserV1


T = TypeVar("T", bound="PostmortemDocumentV1")


@_attrs_define
class PostmortemDocumentV1:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'document_url': 'https://app.incident.io/my-
            org/incidents/123/post-mortems/01GDZEW57FDA1K4S63MGMQ5DS9', 'editors': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}],
            'exported_urls': ['https://www.notion.so/INC-123-sad-database', 'https://docs.google.com/document/d/1234'],
            'id': '01GDZEW57FDA1K4S63MGMQ5DS9', 'incident_id': '01GBA8J19SMXQWPJMX3P2ESCVG', 'status': 'in_progress',
            'title': 'INC-123: Database is sad', 'type': 'in_app', 'updated_at': 'abc123'}

    Attributes:
        created_at (datetime.datetime): Timestamp for when the document was created Example:
            2021-08-17T13:28:57.801578Z.
        document_url (str): A URL to view the post-mortem document in the incident.io dashboard Example:
            https://app.incident.io/my-org/incidents/123/post-mortems/01GDZEW57FDA1K4S63MGMQ5DS9.
        editors (list[UserV1]): The list of users who have edited this post-mortem document Example: [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}].
        exported_urls (list[str]): URLs of any external locations this document has been exported to Example:
            ['https://www.notion.so/INC-123-sad-database', 'https://docs.google.com/document/d/1234'].
        id (str): Unique identifier for the post-mortem document Example: 01GDZEW57FDA1K4S63MGMQ5DS9.
        incident_id (str): The unique identifier of the incident that this post-mortem document belongs to Example:
            01GBA8J19SMXQWPJMX3P2ESCVG.
        status (PostmortemDocumentV1Status): The current status of this post-mortem document Example: in_progress.
        title (str): The display title of the post-mortem document Example: INC-123: Database is sad.
        type_ (PostmortemDocumentV1Type): Whether this is a native incident.io post-mortem or one hosted in an external
            provider Example: in_app.
        updated_at (str): Timestamp for when the document was last updated Example: abc123.
    """

    created_at: datetime.datetime
    document_url: str
    editors: list[UserV1]
    exported_urls: list[str]
    id: str
    incident_id: str
    status: PostmortemDocumentV1Status
    title: str
    type_: PostmortemDocumentV1Type
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        document_url = self.document_url

        editors = []
        for editors_item_data in self.editors:
            editors_item = editors_item_data.to_dict()
            editors.append(editors_item)

        exported_urls = self.exported_urls

        id = self.id

        incident_id = self.incident_id

        status = self.status.value

        title = self.title

        type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "document_url": document_url,
                "editors": editors,
                "exported_urls": exported_urls,
                "id": id,
                "incident_id": incident_id,
                "status": status,
                "title": title,
                "type": type_,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_v1 import UserV1

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        document_url = d.pop("document_url")

        editors = []
        _editors = d.pop("editors")
        for editors_item_data in _editors:
            editors_item = UserV1.from_dict(editors_item_data)

            editors.append(editors_item)

        exported_urls = cast(list[str], d.pop("exported_urls"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        status = PostmortemDocumentV1Status(d.pop("status"))

        title = d.pop("title")

        type_ = PostmortemDocumentV1Type(d.pop("type"))

        updated_at = d.pop("updated_at")

        postmortem_document_v1 = cls(
            created_at=created_at,
            document_url=document_url,
            editors=editors,
            exported_urls=exported_urls,
            id=id,
            incident_id=incident_id,
            status=status,
            title=title,
            type_=type_,
            updated_at=updated_at,
        )

        postmortem_document_v1.additional_properties = d
        return postmortem_document_v1

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
