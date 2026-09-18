from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_type_v2 import IncidentTypeV2


T = TypeVar("T", bound="ActivityIncidentTypeChangedV2")


@_attrs_define
class ActivityIncidentTypeChangedV2:
    """
    Example:
        {'new_incident_type': {'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Customer facing production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name':
            'Production Outage', 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'previous_incident_type': {'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Customer facing production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False,
            'name': 'Production Outage', 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}}

    Attributes:
        new_incident_type (IncidentTypeV2 | Unset):  Example: {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        previous_incident_type (IncidentTypeV2 | Unset):  Example: {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    new_incident_type: IncidentTypeV2 | Unset = UNSET
    previous_incident_type: IncidentTypeV2 | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_incident_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_incident_type, Unset):
            new_incident_type = self.new_incident_type.to_dict()

        previous_incident_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_incident_type, Unset):
            previous_incident_type = self.previous_incident_type.to_dict()

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_incident_type is not UNSET:
            field_dict["new_incident_type"] = new_incident_type
        if previous_incident_type is not UNSET:
            field_dict["previous_incident_type"] = previous_incident_type
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_type_v2 import IncidentTypeV2

        d = dict(src_dict)
        _new_incident_type = d.pop("new_incident_type", UNSET)
        new_incident_type: IncidentTypeV2 | Unset
        if isinstance(_new_incident_type, Unset):
            new_incident_type = UNSET
        else:
            new_incident_type = IncidentTypeV2.from_dict(_new_incident_type)

        _previous_incident_type = d.pop("previous_incident_type", UNSET)
        previous_incident_type: IncidentTypeV2 | Unset
        if isinstance(_previous_incident_type, Unset):
            previous_incident_type = UNSET
        else:
            previous_incident_type = IncidentTypeV2.from_dict(_previous_incident_type)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_incident_type_changed_v2 = cls(
            new_incident_type=new_incident_type,
            previous_incident_type=previous_incident_type,
            updater=updater,
        )

        activity_incident_type_changed_v2.additional_properties = d
        return activity_incident_type_changed_v2

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
