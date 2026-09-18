from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_action_updated_v2_new_status import (
    ActivityActionUpdatedV2NewStatus,
)
from ..models.activity_action_updated_v2_previous_status import (
    ActivityActionUpdatedV2PreviousStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityActionUpdatedV2")


@_attrs_define
class ActivityActionUpdatedV2:
    """
    Example:
        {'action_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'new_status': 'completed', 'previous_assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'previous_status': 'outstanding', 'updater': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}}

    Attributes:
        action_id (str): The action that changed. Fetch it from GET /v2/actions/{id}. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        new_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        new_status (ActivityActionUpdatedV2NewStatus | Unset): Status after, when the status changed Example: completed.
        previous_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        previous_status (ActivityActionUpdatedV2PreviousStatus | Unset): Status before, when the status changed Example:
            outstanding.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    action_id: str
    new_assignee: UserV2 | Unset = UNSET
    new_status: ActivityActionUpdatedV2NewStatus | Unset = UNSET
    previous_assignee: UserV2 | Unset = UNSET
    previous_status: ActivityActionUpdatedV2PreviousStatus | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_id = self.action_id

        new_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_assignee, Unset):
            new_assignee = self.new_assignee.to_dict()

        new_status: str | Unset = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.value

        previous_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_assignee, Unset):
            previous_assignee = self.previous_assignee.to_dict()

        previous_status: str | Unset = UNSET
        if not isinstance(self.previous_status, Unset):
            previous_status = self.previous_status.value

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_id": action_id,
            }
        )
        if new_assignee is not UNSET:
            field_dict["new_assignee"] = new_assignee
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if previous_assignee is not UNSET:
            field_dict["previous_assignee"] = previous_assignee
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        action_id = d.pop("action_id")

        _new_assignee = d.pop("new_assignee", UNSET)
        new_assignee: UserV2 | Unset
        if isinstance(_new_assignee, Unset):
            new_assignee = UNSET
        else:
            new_assignee = UserV2.from_dict(_new_assignee)

        _new_status = d.pop("new_status", UNSET)
        new_status: ActivityActionUpdatedV2NewStatus | Unset
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = ActivityActionUpdatedV2NewStatus(_new_status)

        _previous_assignee = d.pop("previous_assignee", UNSET)
        previous_assignee: UserV2 | Unset
        if isinstance(_previous_assignee, Unset):
            previous_assignee = UNSET
        else:
            previous_assignee = UserV2.from_dict(_previous_assignee)

        _previous_status = d.pop("previous_status", UNSET)
        previous_status: ActivityActionUpdatedV2PreviousStatus | Unset
        if isinstance(_previous_status, Unset):
            previous_status = UNSET
        else:
            previous_status = ActivityActionUpdatedV2PreviousStatus(_previous_status)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_action_updated_v2 = cls(
            action_id=action_id,
            new_assignee=new_assignee,
            new_status=new_status,
            previous_assignee=previous_assignee,
            previous_status=previous_status,
            updater=updater,
        )

        activity_action_updated_v2.additional_properties = d
        return activity_action_updated_v2

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
