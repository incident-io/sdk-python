from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_public_escalation_created_v1_response_body_event_type import (
    WebhooksPublicEscalationCreatedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.escalation_v2 import EscalationV2


T = TypeVar("T", bound="WebhooksPublicEscalationCreatedV1ResponseBody")


@_attrs_define
class WebhooksPublicEscalationCreatedV1ResponseBody:
    """
    Example:
        {'event_type': 'public_escalation.escalation_created_v1', 'public_escalation.escalation_created_v1':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'description': 'Database CPU
            has been above 90% for 5 minutes', 'escalation_path_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'events': [{'channels':
            [{'microsoft_teams_channel_id': 'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123',
            'slack_team_id': 'abc123'}], 'event': 'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at':
            '2021-08-17T13:28:57.801578Z', 'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'priority': {'name': 'P1'}, 'related_alerts': [{'alert_group_ids':
            ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629', 'description': 'CPU on the payments service
            has exceeded 75 percent for 5 minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at':
            '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}], 'related_incidents': [{'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'name': 'Our database is sad', 'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is
            really really sad, and we don't know why yet.", 'visibility': 'public'}], 'status': 'pending', 'title':
            'Database CPU is high', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        event_type (WebhooksPublicEscalationCreatedV1ResponseBodyEventType): What type of event is this webhook for?
            Example: public_escalation.escalation_created_v1.
        public_escalation_escalation_created_v1 (EscalationV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z',
            'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'description': 'Database CPU has been above 90% for 5 minutes',
            'escalation_path_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'events': [{'channels': [{'microsoft_teams_channel_id':
            'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123', 'slack_team_id': 'abc123'}],
            'event': 'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at':
            '2021-08-17T13:28:57.801578Z', 'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'priority': {'name': 'P1'}, 'related_alerts': [{'alert_group_ids':
            ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629', 'description': 'CPU on the payments service
            has exceeded 75 percent for 5 minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at':
            '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}], 'related_incidents': [{'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'name': 'Our database is sad', 'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is
            really really sad, and we don't know why yet.", 'visibility': 'public'}], 'status': 'pending', 'title':
            'Database CPU is high', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    event_type: WebhooksPublicEscalationCreatedV1ResponseBodyEventType
    public_escalation_escalation_created_v1: EscalationV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        public_escalation_escalation_created_v1 = (
            self.public_escalation_escalation_created_v1.to_dict()
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "public_escalation.escalation_created_v1": public_escalation_escalation_created_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_v2 import EscalationV2

        d = dict(src_dict)
        event_type = WebhooksPublicEscalationCreatedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        public_escalation_escalation_created_v1 = EscalationV2.from_dict(
            d.pop("public_escalation.escalation_created_v1")
        )

        webhooks_public_escalation_created_v1_response_body = cls(
            event_type=event_type,
            public_escalation_escalation_created_v1=public_escalation_escalation_created_v1,
        )

        webhooks_public_escalation_created_v1_response_body.additional_properties = d
        return webhooks_public_escalation_created_v1_response_body

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
