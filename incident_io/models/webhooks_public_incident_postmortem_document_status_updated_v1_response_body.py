from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_public_incident_postmortem_document_status_updated_v1_response_body_event_type import (
    WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.postmortem_document_with_status_change_v1 import (
        PostmortemDocumentWithStatusChangeV1,
    )


T = TypeVar(
    "T", bound="WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBody"
)


@_attrs_define
class WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBody:
    """
    Example:
        {'event_type': 'public_incident.postmortem_document_status_updated_v1',
            'public_incident.postmortem_document_status_updated_v1': {'new_status': 'complete', 'postmortem_document':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'document_url': 'https://app.incident.io/my-
            org/incidents/123/post-mortems/01GDZEW57FDA1K4S63MGMQ5DS9', 'editors': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}],
            'exported_urls': ['https://www.notion.so/INC-123-sad-database', 'https://docs.google.com/document/d/1234'],
            'id': '01GDZEW57FDA1K4S63MGMQ5DS9', 'incident_id': '01GBA8J19SMXQWPJMX3P2ESCVG', 'status': 'in_progress',
            'title': 'INC-123: Database is sad', 'type': 'in_app', 'updated_at': 'abc123'}, 'previous_status': 'review'}}

    Attributes:
        event_type (WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBodyEventType): What type of event is
            this webhook for? Example: public_incident.postmortem_document_status_updated_v1.
        public_incident_postmortem_document_status_updated_v1 (PostmortemDocumentWithStatusChangeV1):  Example:
            {'new_status': 'complete', 'postmortem_document': {'created_at': '2021-08-17T13:28:57.801578Z', 'document_url':
            'https://app.incident.io/my-org/incidents/123/post-mortems/01GDZEW57FDA1K4S63MGMQ5DS9', 'editors': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}], 'exported_urls': ['https://www.notion.so/INC-123-sad-database',
            'https://docs.google.com/document/d/1234'], 'id': '01GDZEW57FDA1K4S63MGMQ5DS9', 'incident_id':
            '01GBA8J19SMXQWPJMX3P2ESCVG', 'status': 'in_progress', 'title': 'INC-123: Database is sad', 'type': 'in_app',
            'updated_at': 'abc123'}, 'previous_status': 'review'}.
    """

    event_type: (
        WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBodyEventType
    )
    public_incident_postmortem_document_status_updated_v1: (
        PostmortemDocumentWithStatusChangeV1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        public_incident_postmortem_document_status_updated_v1 = (
            self.public_incident_postmortem_document_status_updated_v1.to_dict()
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "public_incident.postmortem_document_status_updated_v1": public_incident_postmortem_document_status_updated_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postmortem_document_with_status_change_v1 import (
            PostmortemDocumentWithStatusChangeV1,
        )

        d = dict(src_dict)
        event_type = WebhooksPublicIncidentPostmortemDocumentStatusUpdatedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        public_incident_postmortem_document_status_updated_v1 = (
            PostmortemDocumentWithStatusChangeV1.from_dict(
                d.pop("public_incident.postmortem_document_status_updated_v1")
            )
        )

        webhooks_public_incident_postmortem_document_status_updated_v1_response_body = cls(
            event_type=event_type,
            public_incident_postmortem_document_status_updated_v1=public_incident_postmortem_document_status_updated_v1,
        )

        webhooks_public_incident_postmortem_document_status_updated_v1_response_body.additional_properties = d
        return (
            webhooks_public_incident_postmortem_document_status_updated_v1_response_body
        )

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
