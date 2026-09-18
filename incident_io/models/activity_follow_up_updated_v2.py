from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_follow_up_updated_v2_new_status import (
    ActivityFollowUpUpdatedV2NewStatus,
)
from ..models.activity_follow_up_updated_v2_previous_status import (
    ActivityFollowUpUpdatedV2PreviousStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityFollowUpUpdatedV2")


@_attrs_define
class ActivityFollowUpUpdatedV2:
    """
    Example:
        {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'new_status': 'completed', 'new_title': 'Add a payments-api rollback runbook', 'previous_assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'previous_title': 'Add a runbook', 'updater':
            {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
            'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}}

    Attributes:
        follow_up_id (str): The follow-up that changed. Fetch it from GET /v2/follow_ups/{id}. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        new_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        new_status (ActivityFollowUpUpdatedV2NewStatus | Unset): Status after, when the status changed Example:
            completed.
        new_title (str | Unset): Title after, when the title changed Example: Add a payments-api rollback runbook.
        previous_assignee (UserV2 | Unset):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        previous_status (ActivityFollowUpUpdatedV2PreviousStatus | Unset): Status before, when the status changed
            Example: outstanding.
        previous_title (str | Unset): Title before, when the title changed Example: Add a runbook.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    follow_up_id: str
    new_assignee: UserV2 | Unset = UNSET
    new_status: ActivityFollowUpUpdatedV2NewStatus | Unset = UNSET
    new_title: str | Unset = UNSET
    previous_assignee: UserV2 | Unset = UNSET
    previous_status: ActivityFollowUpUpdatedV2PreviousStatus | Unset = UNSET
    previous_title: str | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_up_id = self.follow_up_id

        new_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_assignee, Unset):
            new_assignee = self.new_assignee.to_dict()

        new_status: str | Unset = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.value

        new_title = self.new_title

        previous_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_assignee, Unset):
            previous_assignee = self.previous_assignee.to_dict()

        previous_status: str | Unset = UNSET
        if not isinstance(self.previous_status, Unset):
            previous_status = self.previous_status.value

        previous_title = self.previous_title

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_up_id": follow_up_id,
            }
        )
        if new_assignee is not UNSET:
            field_dict["new_assignee"] = new_assignee
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if new_title is not UNSET:
            field_dict["new_title"] = new_title
        if previous_assignee is not UNSET:
            field_dict["previous_assignee"] = previous_assignee
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status
        if previous_title is not UNSET:
            field_dict["previous_title"] = previous_title
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.user_v2 import UserV2

        d = dict(src_dict)
        follow_up_id = d.pop("follow_up_id")

        _new_assignee = d.pop("new_assignee", UNSET)
        new_assignee: UserV2 | Unset
        if isinstance(_new_assignee, Unset):
            new_assignee = UNSET
        else:
            new_assignee = UserV2.from_dict(_new_assignee)

        _new_status = d.pop("new_status", UNSET)
        new_status: ActivityFollowUpUpdatedV2NewStatus | Unset
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = ActivityFollowUpUpdatedV2NewStatus(_new_status)

        new_title = d.pop("new_title", UNSET)

        _previous_assignee = d.pop("previous_assignee", UNSET)
        previous_assignee: UserV2 | Unset
        if isinstance(_previous_assignee, Unset):
            previous_assignee = UNSET
        else:
            previous_assignee = UserV2.from_dict(_previous_assignee)

        _previous_status = d.pop("previous_status", UNSET)
        previous_status: ActivityFollowUpUpdatedV2PreviousStatus | Unset
        if isinstance(_previous_status, Unset):
            previous_status = UNSET
        else:
            previous_status = ActivityFollowUpUpdatedV2PreviousStatus(_previous_status)

        previous_title = d.pop("previous_title", UNSET)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_follow_up_updated_v2 = cls(
            follow_up_id=follow_up_id,
            new_assignee=new_assignee,
            new_status=new_status,
            new_title=new_title,
            previous_assignee=previous_assignee,
            previous_status=previous_status,
            previous_title=previous_title,
            updater=updater,
        )

        activity_follow_up_updated_v2.additional_properties = d
        return activity_follow_up_updated_v2

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
