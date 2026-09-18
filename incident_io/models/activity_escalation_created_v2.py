from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityEscalationCreatedV2")


@_attrs_define
class ActivityEscalationCreatedV2:
    """
    Example:
        {'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'escalated_to_users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'escalation_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG1'}

    Attributes:
        escalation_id (str): The escalation. Fetch it from GET /v2/escalations/{id}. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        creator (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
        escalated_to_users (list[UserV2] | Unset): Users this escalation paged Example: [{'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id':
            'U02AYNF2XJM'}].
        escalation_path_id (str | Unset): The escalation path used, when one was Example: 01FCNDV6P870EA6S7TK1DSYDG1.
    """

    escalation_id: str
    creator: ActorV2 | Unset = UNSET
    escalated_to_users: list[UserV2] | Unset = UNSET
    escalation_path_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation_id = self.escalation_id

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        escalated_to_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.escalated_to_users, Unset):
            escalated_to_users = []
            for escalated_to_users_item_data in self.escalated_to_users:
                escalated_to_users_item = escalated_to_users_item_data.to_dict()
                escalated_to_users.append(escalated_to_users_item)

        escalation_path_id = self.escalation_path_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_id": escalation_id,
            }
        )
        if creator is not UNSET:
            field_dict["creator"] = creator
        if escalated_to_users is not UNSET:
            field_dict["escalated_to_users"] = escalated_to_users
        if escalation_path_id is not UNSET:
            field_dict["escalation_path_id"] = escalation_path_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        escalation_id = d.pop("escalation_id")

        _creator = d.pop("creator", UNSET)
        creator: ActorV2 | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ActorV2.from_dict(_creator)

        _escalated_to_users = d.pop("escalated_to_users", UNSET)
        escalated_to_users: list[UserV2] | Unset = UNSET
        if _escalated_to_users is not UNSET:
            escalated_to_users = []
            for escalated_to_users_item_data in _escalated_to_users:
                escalated_to_users_item = UserV2.from_dict(escalated_to_users_item_data)

                escalated_to_users.append(escalated_to_users_item)

        escalation_path_id = d.pop("escalation_path_id", UNSET)

        activity_escalation_created_v2 = cls(
            escalation_id=escalation_id,
            creator=creator,
            escalated_to_users=escalated_to_users,
            escalation_path_id=escalation_path_id,
        )

        activity_escalation_created_v2.additional_properties = d
        return activity_escalation_created_v2

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
