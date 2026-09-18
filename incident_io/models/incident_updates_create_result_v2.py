from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_update_v2 import IncidentUpdateV2


T = TypeVar("T", bound="IncidentUpdatesCreateResultV2")


@_attrs_define
class IncidentUpdatesCreateResultV2:
    """
    Example:
        {'incident_update': {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merged_into_incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'message':
            "We're working on a fix, hoping to ship in the next 30 minutes", 'new_incident_status': {'category': 'triage',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're
            ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}}}

    Attributes:
        incident_update (IncidentUpdateV2):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merged_into_incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'message': "We're working on a fix, hoping to ship in the next 30 minutes",
            'new_incident_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            "Impact has been **fully mitigated**, and we're ready to learn from this incident.", 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}}.
    """

    incident_update: IncidentUpdateV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_update = self.incident_update.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_update": incident_update,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_update_v2 import IncidentUpdateV2

        d = dict(src_dict)
        incident_update = IncidentUpdateV2.from_dict(d.pop("incident_update"))

        incident_updates_create_result_v2 = cls(
            incident_update=incident_update,
        )

        incident_updates_create_result_v2.additional_properties = d
        return incident_updates_create_result_v2

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
