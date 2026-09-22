from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_status_v2 import IncidentStatusV2
    from ..models.severity_v2 import SeverityV2


T = TypeVar("T", bound="ActivityIncidentUpdateV2")


@_attrs_define(kw_only=True)
class ActivityIncidentUpdateV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message': 'Rolled back **payments-api** to v411, error rate recovering.',
            'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'new_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has
            been **fully mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'next_update_in_minutes': 30,
            'previous_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'previous_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact
            has been **fully mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}

    Attributes:
        id (str): ID of the incident update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        message (str | Unset): The update the responder wrote, in markdown Example: Rolled back **payments-api** to
            v411, error rate recovering..
        new_severity (SeverityV2 | Unset):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        new_status (IncidentStatusV2 | Unset):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        next_update_in_minutes (int | Unset): When the responder said the next update would come Example: 30.
        previous_severity (SeverityV2 | Unset):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        previous_status (IncidentStatusV2 | Unset):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    id: str
    message: str | Unset = UNSET
    new_severity: SeverityV2 | Unset = UNSET
    new_status: IncidentStatusV2 | Unset = UNSET
    next_update_in_minutes: int | Unset = UNSET
    previous_severity: SeverityV2 | Unset = UNSET
    previous_status: IncidentStatusV2 | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message = self.message

        new_severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_severity, Unset):
            new_severity = self.new_severity.to_dict()

        new_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.to_dict()

        next_update_in_minutes = self.next_update_in_minutes

        previous_severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_severity, Unset):
            previous_severity = self.previous_severity.to_dict()

        previous_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_status, Unset):
            previous_status = self.previous_status.to_dict()

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if new_severity is not UNSET:
            field_dict["new_severity"] = new_severity
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if next_update_in_minutes is not UNSET:
            field_dict["next_update_in_minutes"] = next_update_in_minutes
        if previous_severity is not UNSET:
            field_dict["previous_severity"] = previous_severity
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_status_v2 import IncidentStatusV2
        from ..models.severity_v2 import SeverityV2

        d = dict(src_dict)
        id = d.pop("id")

        message = d.pop("message", UNSET)

        _new_severity = d.pop("new_severity", UNSET)
        new_severity: SeverityV2 | Unset
        if isinstance(_new_severity, Unset):
            new_severity = UNSET
        else:
            new_severity = SeverityV2.from_dict(_new_severity)

        _new_status = d.pop("new_status", UNSET)
        new_status: IncidentStatusV2 | Unset
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = IncidentStatusV2.from_dict(_new_status)

        next_update_in_minutes = d.pop("next_update_in_minutes", UNSET)

        _previous_severity = d.pop("previous_severity", UNSET)
        previous_severity: SeverityV2 | Unset
        if isinstance(_previous_severity, Unset):
            previous_severity = UNSET
        else:
            previous_severity = SeverityV2.from_dict(_previous_severity)

        _previous_status = d.pop("previous_status", UNSET)
        previous_status: IncidentStatusV2 | Unset
        if isinstance(_previous_status, Unset):
            previous_status = UNSET
        else:
            previous_status = IncidentStatusV2.from_dict(_previous_status)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_incident_update_v2 = cls(
            id=id,
            message=message,
            new_severity=new_severity,
            new_status=new_status,
            next_update_in_minutes=next_update_in_minutes,
            previous_severity=previous_severity,
            previous_status=previous_status,
            updater=updater,
        )

        activity_incident_update_v2.additional_properties = d
        return activity_incident_update_v2

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
