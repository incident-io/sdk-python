from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_v2_status import EscalationV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_slim_v2 import AlertSlimV2
    from ..models.escalation_creator_v2 import EscalationCreatorV2
    from ..models.escalation_event_v2 import EscalationEventV2
    from ..models.escalation_priority_v2 import EscalationPriorityV2
    from ..models.incident_slim_v2 import IncidentSlimV2


T = TypeVar("T", bound="EscalationV2")


@_attrs_define(kw_only=True)
class EscalationV2:
    """
    Example:
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
            'Database CPU is high', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When this escalation was created Example: 2021-08-17T13:28:57.801578Z.
        creator (EscalationCreatorV2): The creator of this escalation. Can be a user, a workflow, or an alert. If the
            escalation came from a call route, this will be empty. Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
            'title': '*errors.withMessage: PG::Error failed to connect'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}.
        description (str): Additional detail provided with this escalation. When it isn't set explicitly, this is taken
            from the alert description or the incident summary, and is empty when neither applies. Example: Database CPU has
            been above 90% for 5 minutes.
        events (list[EscalationEventV2]): Events which describe the history of this escalation. Events include
            information about what users or channels were notified and what users acked. Example: [{'channels':
            [{'microsoft_teams_channel_id': 'abc123', 'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123',
            'slack_team_id': 'abc123'}], 'event': 'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at':
            '2021-08-17T13:28:57.801578Z', 'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}].
        id (str): Unique ID of the escalation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        priority (EscalationPriorityV2): The priority associated with this escalation. Example: {'name': 'P1'}.
        related_alerts (list[AlertSlimV2]): Alerts related to this escalation Example: [{'alert_group_ids':
            ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'deduplication_key': '4293868629', 'description': 'CPU on the payments service
            has exceeded 75 percent for 5 minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at':
            '2021-08-17T14:28:57.801578Z', 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
        related_incidents (list[IncidentSlimV2]): Incidents related to this escalation Example: [{'external_id': 123,
            'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123', 'status_category':
            'triage', 'summary': "Our database is really really sad, and we don't know why yet.", 'visibility': 'public'}].
        status (EscalationV2Status): Status of the escalation Example: pending.
        title (str): The title of this escalation Example: Database CPU is high.
        updated_at (datetime.datetime): When this escalation was last updated Example: 2021-08-17T13:28:57.801578Z.
        escalation_path_id (str | Unset): Unique identifier of the escalation path that the escalation was created from
            Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
    """

    created_at: datetime.datetime
    creator: EscalationCreatorV2
    description: str
    events: list[EscalationEventV2]
    id: str
    priority: EscalationPriorityV2
    related_alerts: list[AlertSlimV2]
    related_incidents: list[IncidentSlimV2]
    status: EscalationV2Status
    title: str
    updated_at: datetime.datetime
    escalation_path_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        description = self.description

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        id = self.id

        priority = self.priority.to_dict()

        related_alerts = []
        for related_alerts_item_data in self.related_alerts:
            related_alerts_item = related_alerts_item_data.to_dict()
            related_alerts.append(related_alerts_item)

        related_incidents = []
        for related_incidents_item_data in self.related_incidents:
            related_incidents_item = related_incidents_item_data.to_dict()
            related_incidents.append(related_incidents_item)

        status = self.status.value

        title = self.title

        updated_at = self.updated_at.isoformat()

        escalation_path_id = self.escalation_path_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "description": description,
                "events": events,
                "id": id,
                "priority": priority,
                "related_alerts": related_alerts,
                "related_incidents": related_incidents,
                "status": status,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if escalation_path_id is not UNSET:
            field_dict["escalation_path_id"] = escalation_path_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_slim_v2 import AlertSlimV2
        from ..models.escalation_creator_v2 import EscalationCreatorV2
        from ..models.escalation_event_v2 import EscalationEventV2
        from ..models.escalation_priority_v2 import (
            EscalationPriorityV2,
        )
        from ..models.incident_slim_v2 import IncidentSlimV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = EscalationCreatorV2.from_dict(d.pop("creator"))

        description = d.pop("description")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EscalationEventV2.from_dict(events_item_data)

            events.append(events_item)

        id = d.pop("id")

        priority = EscalationPriorityV2.from_dict(d.pop("priority"))

        related_alerts = []
        _related_alerts = d.pop("related_alerts")
        for related_alerts_item_data in _related_alerts:
            related_alerts_item = AlertSlimV2.from_dict(related_alerts_item_data)

            related_alerts.append(related_alerts_item)

        related_incidents = []
        _related_incidents = d.pop("related_incidents")
        for related_incidents_item_data in _related_incidents:
            related_incidents_item = IncidentSlimV2.from_dict(
                related_incidents_item_data
            )

            related_incidents.append(related_incidents_item)

        status = EscalationV2Status(d.pop("status"))

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        escalation_path_id = d.pop("escalation_path_id", UNSET)

        escalation_v2 = cls(
            created_at=created_at,
            creator=creator,
            description=description,
            events=events,
            id=id,
            priority=priority,
            related_alerts=related_alerts,
            related_incidents=related_incidents,
            status=status,
            title=title,
            updated_at=updated_at,
            escalation_path_id=escalation_path_id,
        )

        escalation_v2.additional_properties = d
        return escalation_v2

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
