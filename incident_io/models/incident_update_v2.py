from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_status_v2 import IncidentStatusV2
    from ..models.severity_v2 import SeverityV2


T = TypeVar("T", bound="IncidentUpdateV2")


@_attrs_define
class IncidentUpdateV2:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'merged_into_incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message': "We're working
            on a fix, hoping to ship in the next 30 minutes", 'new_incident_status': {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}}

    Attributes:
        created_at (datetime.datetime): When the update was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier for this incident update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): The incident this update relates to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        new_incident_status (IncidentStatusV2):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        updater (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        merged_into_incident_id (str | Unset): The ID of the incident this incident was merged into, if the to state of
            this update is 'merged'. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        message (str | Unset): Message that explains the context behind the update Example: We're working on a fix,
            hoping to ship in the next 30 minutes.
        new_severity (SeverityV2 | Unset):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    created_at: datetime.datetime
    id: str
    incident_id: str
    new_incident_status: IncidentStatusV2
    updater: ActorV2
    merged_into_incident_id: str | Unset = UNSET
    message: str | Unset = UNSET
    new_severity: SeverityV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        incident_id = self.incident_id

        new_incident_status = self.new_incident_status.to_dict()

        updater = self.updater.to_dict()

        merged_into_incident_id = self.merged_into_incident_id

        message = self.message

        new_severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_severity, Unset):
            new_severity = self.new_severity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_id": incident_id,
                "new_incident_status": new_incident_status,
                "updater": updater,
            }
        )
        if merged_into_incident_id is not UNSET:
            field_dict["merged_into_incident_id"] = merged_into_incident_id
        if message is not UNSET:
            field_dict["message"] = message
        if new_severity is not UNSET:
            field_dict["new_severity"] = new_severity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_status_v2 import IncidentStatusV2
        from ..models.severity_v2 import SeverityV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        new_incident_status = IncidentStatusV2.from_dict(d.pop("new_incident_status"))

        updater = ActorV2.from_dict(d.pop("updater"))

        merged_into_incident_id = d.pop("merged_into_incident_id", UNSET)

        message = d.pop("message", UNSET)

        _new_severity = d.pop("new_severity", UNSET)
        new_severity: SeverityV2 | Unset
        if isinstance(_new_severity, Unset):
            new_severity = UNSET
        else:
            new_severity = SeverityV2.from_dict(_new_severity)

        incident_update_v2 = cls(
            created_at=created_at,
            id=id,
            incident_id=incident_id,
            new_incident_status=new_incident_status,
            updater=updater,
            merged_into_incident_id=merged_into_incident_id,
            message=message,
            new_severity=new_severity,
        )

        incident_update_v2.additional_properties = d
        return incident_update_v2

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
