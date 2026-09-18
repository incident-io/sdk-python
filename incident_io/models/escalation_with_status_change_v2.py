from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_with_status_change_v2_new_status import (
    EscalationWithStatusChangeV2NewStatus,
)
from ..models.escalation_with_status_change_v2_previous_status import (
    EscalationWithStatusChangeV2PreviousStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.escalation_v2 import EscalationV2


T = TypeVar("T", bound="EscalationWithStatusChangeV2")


@_attrs_define
class EscalationWithStatusChangeV2:
    """
    Example:
        {'actor': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'escalation': {'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Database CPU has been above 90% for 5 minutes', 'escalation_path_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'events': [{'channels': [{'microsoft_teams_channel_id': 'abc123',
            'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123', 'slack_team_id': 'abc123'}], 'event':
            'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at': '2021-08-17T13:28:57.801578Z',
            'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'priority': {'name': 'P1'}, 'related_alerts': [{'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'],
            'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at': '2021-08-17T13:28:57.801578Z',
            'deduplication_key': '4293868629', 'description': 'CPU on the payments service has exceeded 75 percent for 5
            minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage:
            PG::Error failed to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}], 'related_incidents':
            [{'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
            'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
            'visibility': 'public'}], 'status': 'pending', 'title': 'Database CPU is high', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'new_status': 'pending', 'previous_status': 'pending'}

    Attributes:
        escalation (EscalationV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'description': 'Database CPU has been above 90% for 5 minutes', 'escalation_path_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'events': [{'channels': [{'microsoft_teams_channel_id': 'abc123',
            'microsoft_teams_team_id': 'abc123', 'slack_channel_id': 'abc123', 'slack_team_id': 'abc123'}], 'event':
            'entered_grace_period', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'occurred_at': '2021-08-17T13:28:57.801578Z',
            'urgency': 'high', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}]}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'priority': {'name': 'P1'}, 'related_alerts': [{'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'],
            'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66', 'created_at': '2021-08-17T13:28:57.801578Z',
            'deduplication_key': '4293868629', 'description': 'CPU on the payments service has exceeded 75 percent for 5
            minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage:
            PG::Error failed to connect', 'updated_at': '2021-08-17T13:28:57.801578Z'}], 'related_incidents':
            [{'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123',
            'status_category': 'triage', 'summary': "Our database is really really sad, and we don't know why yet.",
            'visibility': 'public'}], 'status': 'pending', 'title': 'Database CPU is high', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        new_status (EscalationWithStatusChangeV2NewStatus): The new status of the escalation Example: pending.
        actor (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        previous_status (EscalationWithStatusChangeV2PreviousStatus | Unset): The previous status of the escalation
            Example: pending.
    """

    escalation: EscalationV2
    new_status: EscalationWithStatusChangeV2NewStatus
    actor: ActorV2 | Unset = UNSET
    previous_status: EscalationWithStatusChangeV2PreviousStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation = self.escalation.to_dict()

        new_status = self.new_status.value

        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        previous_status: str | Unset = UNSET
        if not isinstance(self.previous_status, Unset):
            previous_status = self.previous_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation": escalation,
                "new_status": new_status,
            }
        )
        if actor is not UNSET:
            field_dict["actor"] = actor
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.escalation_v2 import EscalationV2

        d = dict(src_dict)
        escalation = EscalationV2.from_dict(d.pop("escalation"))

        new_status = EscalationWithStatusChangeV2NewStatus(d.pop("new_status"))

        _actor = d.pop("actor", UNSET)
        actor: ActorV2 | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = ActorV2.from_dict(_actor)

        _previous_status = d.pop("previous_status", UNSET)
        previous_status: EscalationWithStatusChangeV2PreviousStatus | Unset
        if isinstance(_previous_status, Unset):
            previous_status = UNSET
        else:
            previous_status = EscalationWithStatusChangeV2PreviousStatus(
                _previous_status
            )

        escalation_with_status_change_v2 = cls(
            escalation=escalation,
            new_status=new_status,
            actor=actor,
            previous_status=previous_status,
        )

        escalation_with_status_change_v2.additional_properties = d
        return escalation_with_status_change_v2

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
