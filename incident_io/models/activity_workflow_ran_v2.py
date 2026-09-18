from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2


T = TypeVar("T", bound="ActivityWorkflowRanV2")


@_attrs_define
class ActivityWorkflowRanV2:
    """
    Example:
        {'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'event_description': 'Stopped the synthetic load test in staging.', 'event_title': 'Load test
            halted'}

    Attributes:
        event_title (str): Title of the event the workflow added Example: Load test halted.
        creator (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
        event_description (str | Unset): Description of the event the workflow added, in markdown Example: Stopped the
            synthetic load test in staging..
    """

    event_title: str
    creator: ActorV2 | Unset = UNSET
    event_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_title = self.event_title

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        event_description = self.event_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_title": event_title,
            }
        )
        if creator is not UNSET:
            field_dict["creator"] = creator
        if event_description is not UNSET:
            field_dict["event_description"] = event_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2

        d = dict(src_dict)
        event_title = d.pop("event_title")

        _creator = d.pop("creator", UNSET)
        creator: ActorV2 | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ActorV2.from_dict(_creator)

        event_description = d.pop("event_description", UNSET)

        activity_workflow_ran_v2 = cls(
            event_title=event_title,
            creator=creator,
            event_description=event_description,
        )

        activity_workflow_ran_v2.additional_properties = d
        return activity_workflow_ran_v2

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
