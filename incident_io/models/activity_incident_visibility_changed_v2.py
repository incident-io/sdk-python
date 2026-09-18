from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_incident_visibility_changed_v2_new_visibility import (
    ActivityIncidentVisibilityChangedV2NewVisibility,
)
from ..models.activity_incident_visibility_changed_v2_previous_visibility import (
    ActivityIncidentVisibilityChangedV2PreviousVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2


T = TypeVar("T", bound="ActivityIncidentVisibilityChangedV2")


@_attrs_define
class ActivityIncidentVisibilityChangedV2:
    """
    Example:
        {'new_visibility': 'private', 'previous_visibility': 'public', 'updater': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}

    Attributes:
        new_visibility (ActivityIncidentVisibilityChangedV2NewVisibility): Visibility after the change Example: private.
        previous_visibility (ActivityIncidentVisibilityChangedV2PreviousVisibility): Visibility before the change
            Example: public.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    new_visibility: ActivityIncidentVisibilityChangedV2NewVisibility
    previous_visibility: ActivityIncidentVisibilityChangedV2PreviousVisibility
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_visibility = self.new_visibility.value

        previous_visibility = self.previous_visibility.value

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_visibility": new_visibility,
                "previous_visibility": previous_visibility,
            }
        )
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2

        d = dict(src_dict)
        new_visibility = ActivityIncidentVisibilityChangedV2NewVisibility(
            d.pop("new_visibility")
        )

        previous_visibility = ActivityIncidentVisibilityChangedV2PreviousVisibility(
            d.pop("previous_visibility")
        )

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_incident_visibility_changed_v2 = cls(
            new_visibility=new_visibility,
            previous_visibility=previous_visibility,
            updater=updater,
        )

        activity_incident_visibility_changed_v2.additional_properties = d
        return activity_incident_visibility_changed_v2

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
