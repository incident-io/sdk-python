from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2


T = TypeVar("T", bound="PolicyFindingDismissalV2")


@_attrs_define(kw_only=True)
class PolicyFindingDismissalV2:
    """
    Example:
        {'dismissed_at': '2021-08-17T13:28:57.801578Z', 'dismissed_by': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
            'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'reason': 'This incident is special.'}

    Attributes:
        dismissed_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        dismissed_by (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        reason (str): Why it was dismissed Example: This incident is special..
    """

    dismissed_at: datetime.datetime
    dismissed_by: ActorV2
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dismissed_at = self.dismissed_at.isoformat()

        dismissed_by = self.dismissed_by.to_dict()

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dismissed_at": dismissed_at,
                "dismissed_by": dismissed_by,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2

        d = dict(src_dict)
        dismissed_at = datetime.datetime.fromisoformat(d.pop("dismissed_at"))

        dismissed_by = ActorV2.from_dict(d.pop("dismissed_by"))

        reason = d.pop("reason")

        policy_finding_dismissal_v2 = cls(
            dismissed_at=dismissed_at,
            dismissed_by=dismissed_by,
            reason=reason,
        )

        policy_finding_dismissal_v2.additional_properties = d
        return policy_finding_dismissal_v2

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
