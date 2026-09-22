from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_timestamp_v2 import IncidentTimestampV2


T = TypeVar("T", bound="ActivityIncidentTimestampSetV2")


@_attrs_define(kw_only=True)
class ActivityIncidentTimestampSetV2:
    """
    Example:
        {'incident_timestamp': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'new_value':
            '2026-09-01T13:42:00Z', 'previous_value': '2026-09-01T14:00:00Z', 'updater': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}

    Attributes:
        incident_timestamp (IncidentTimestampV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact
            started', 'rank': 1}.
        new_value (datetime.datetime): What it was set to Example: 2026-09-01T13:42:00Z.
        previous_value (datetime.datetime | Unset): What it was before. Absent when it was previously unset. Example:
            2026-09-01T14:00:00Z.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    incident_timestamp: IncidentTimestampV2
    new_value: datetime.datetime
    previous_value: datetime.datetime | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_timestamp = self.incident_timestamp.to_dict()

        new_value = self.new_value.isoformat()

        previous_value: str | Unset = UNSET
        if not isinstance(self.previous_value, Unset):
            previous_value = self.previous_value.isoformat()

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timestamp": incident_timestamp,
                "new_value": new_value,
            }
        )
        if previous_value is not UNSET:
            field_dict["previous_value"] = previous_value
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_timestamp_v2 import IncidentTimestampV2

        d = dict(src_dict)
        incident_timestamp = IncidentTimestampV2.from_dict(d.pop("incident_timestamp"))

        new_value = datetime.datetime.fromisoformat(d.pop("new_value"))

        _previous_value = d.pop("previous_value", UNSET)
        previous_value: datetime.datetime | Unset
        if isinstance(_previous_value, Unset):
            previous_value = UNSET
        else:
            previous_value = datetime.datetime.fromisoformat(_previous_value)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_incident_timestamp_set_v2 = cls(
            incident_timestamp=incident_timestamp,
            new_value=new_value,
            previous_value=previous_value,
            updater=updater,
        )

        activity_incident_timestamp_set_v2.additional_properties = d
        return activity_incident_timestamp_set_v2

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
