from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_private_incident_follow_up_created_v2_response_body_event_type import (
    WebhooksPrivateIncidentFollowUpCreatedV2ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.webhook_private_resource_v2 import WebhookPrivateResourceV2


T = TypeVar("T", bound="WebhooksPrivateIncidentFollowUpCreatedV2ResponseBody")


@_attrs_define(kw_only=True)
class WebhooksPrivateIncidentFollowUpCreatedV2ResponseBody:
    """
    Example:
        {'event_type': 'private_incident.follow_up_created_v2', 'private_incident.follow_up_created_v2': {'id':
            'abc123'}}

    Attributes:
        event_type (WebhooksPrivateIncidentFollowUpCreatedV2ResponseBodyEventType): What type of event is this webhook
            for? Example: private_incident.follow_up_created_v2.
        private_incident_follow_up_created_v2 (WebhookPrivateResourceV2):  Example: {'id': 'abc123'}.
    """

    event_type: WebhooksPrivateIncidentFollowUpCreatedV2ResponseBodyEventType
    private_incident_follow_up_created_v2: WebhookPrivateResourceV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        private_incident_follow_up_created_v2 = (
            self.private_incident_follow_up_created_v2.to_dict()
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "private_incident.follow_up_created_v2": private_incident_follow_up_created_v2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_private_resource_v2 import (
            WebhookPrivateResourceV2,
        )

        d = dict(src_dict)
        event_type = WebhooksPrivateIncidentFollowUpCreatedV2ResponseBodyEventType(
            d.pop("event_type")
        )

        private_incident_follow_up_created_v2 = WebhookPrivateResourceV2.from_dict(
            d.pop("private_incident.follow_up_created_v2")
        )

        webhooks_private_incident_follow_up_created_v2_response_body = cls(
            event_type=event_type,
            private_incident_follow_up_created_v2=private_incident_follow_up_created_v2,
        )

        webhooks_private_incident_follow_up_created_v2_response_body.additional_properties = d
        return webhooks_private_incident_follow_up_created_v2_response_body

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
