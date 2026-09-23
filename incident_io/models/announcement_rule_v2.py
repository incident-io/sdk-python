from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_rule_v2_conditions_no_longer_apply_behaviour import (
    AnnouncementRuleV2ConditionsNoLongerApplyBehaviour,
)
from ..models.announcement_rule_v2_mode import AnnouncementRuleV2Mode
from ..models.announcement_rule_v2_private_incident_scope import (
    AnnouncementRuleV2PrivateIncidentScope,
)
from ..models.announcement_rule_v2_update_sharing_mode import (
    AnnouncementRuleV2UpdateSharingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_v2 import ConditionGroupV2


T = TypeVar("T", bound="AnnouncementRuleV2")


@_attrs_define(kw_only=True)
class AnnouncementRuleV2:
    """An announcement rule posts an announcement of matching incidents into one or more channels.

    Example:
        {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'conditions_no_longer_apply_behaviour': 'leave_in_place', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'microsoft_teams_channel_ids':
            ['19:abc@thread.tacv2/19:def@thread.tacv2'], 'mode': 'live_and_closed', 'name': 'Data Breaches',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'private_incident_scope': 'all', 'slack_channel_ids':
            ['C02AW36C1M5'], 'template_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'update_sharing_mode': 'none', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        condition_groups (list[ConditionGroupV2]): Incidents are announced when they match any of these condition groups
            Example: [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}].
        conditions_no_longer_apply_behaviour (AnnouncementRuleV2ConditionsNoLongerApplyBehaviour): Whether to remove
            announcement posts when the incident no longer matches this rule's conditions Example: leave_in_place.
        created_at (datetime.datetime): When the rule was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier for this announcement rule Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        microsoft_teams_channel_ids (list[str]): Microsoft Teams channels to post announcements into, as
            team_id/channel_id, when the organisation uses Microsoft Teams Example:
            ['19:abc@thread.tacv2/19:def@thread.tacv2'].
        mode (AnnouncementRuleV2Mode): Which incidents are announced: live incidents only, or triage incidents too
            Example: live_and_closed.
        name (str): Human readable name for the rule Example: Data Breaches.
        owning_team_ids (list[str]): IDs of the teams that own this rule Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        slack_channel_ids (list[str]): IDs of the Slack channels to post announcements into, when the organisation uses
            Slack Example: ['C02AW36C1M5'].
        update_sharing_mode (AnnouncementRuleV2UpdateSharingMode): Where incident updates are shared once the incident
            is announced Example: none.
        updated_at (datetime.datetime): When the rule was last updated Example: 2021-08-17T13:28:57.801578Z.
        private_incident_scope (AnnouncementRuleV2PrivateIncidentScope | Unset): Which private incidents this rule
            announces: every private incident (all), those an owning team can see (owning_teams), or none Example: all.
        template_id (str | Unset): ID of the announcement template used to render this rule's posts Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    condition_groups: list[ConditionGroupV2]
    conditions_no_longer_apply_behaviour: (
        AnnouncementRuleV2ConditionsNoLongerApplyBehaviour
    )
    created_at: datetime.datetime
    id: str
    microsoft_teams_channel_ids: list[str]
    mode: AnnouncementRuleV2Mode
    name: str
    owning_team_ids: list[str]
    slack_channel_ids: list[str]
    update_sharing_mode: AnnouncementRuleV2UpdateSharingMode
    updated_at: datetime.datetime
    private_incident_scope: AnnouncementRuleV2PrivateIncidentScope | Unset = UNSET
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        conditions_no_longer_apply_behaviour = (
            self.conditions_no_longer_apply_behaviour.value
        )

        created_at = self.created_at.isoformat()

        id = self.id

        microsoft_teams_channel_ids = self.microsoft_teams_channel_ids

        mode = self.mode.value

        name = self.name

        owning_team_ids = self.owning_team_ids

        slack_channel_ids = self.slack_channel_ids

        update_sharing_mode = self.update_sharing_mode.value

        updated_at = self.updated_at.isoformat()

        private_incident_scope: str | Unset = UNSET
        if not isinstance(self.private_incident_scope, Unset):
            private_incident_scope = self.private_incident_scope.value

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "conditions_no_longer_apply_behaviour": conditions_no_longer_apply_behaviour,
                "created_at": created_at,
                "id": id,
                "microsoft_teams_channel_ids": microsoft_teams_channel_ids,
                "mode": mode,
                "name": name,
                "owning_team_ids": owning_team_ids,
                "slack_channel_ids": slack_channel_ids,
                "update_sharing_mode": update_sharing_mode,
                "updated_at": updated_at,
            }
        )
        if private_incident_scope is not UNSET:
            field_dict["private_incident_scope"] = private_incident_scope
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_v2 import ConditionGroupV2

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        conditions_no_longer_apply_behaviour = (
            AnnouncementRuleV2ConditionsNoLongerApplyBehaviour(
                d.pop("conditions_no_longer_apply_behaviour")
            )
        )

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        microsoft_teams_channel_ids = cast(
            list[str], d.pop("microsoft_teams_channel_ids")
        )

        mode = AnnouncementRuleV2Mode(d.pop("mode"))

        name = d.pop("name")

        owning_team_ids = cast(list[str], d.pop("owning_team_ids"))

        slack_channel_ids = cast(list[str], d.pop("slack_channel_ids"))

        update_sharing_mode = AnnouncementRuleV2UpdateSharingMode(
            d.pop("update_sharing_mode")
        )

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _private_incident_scope = d.pop("private_incident_scope", UNSET)
        private_incident_scope: AnnouncementRuleV2PrivateIncidentScope | Unset
        if isinstance(_private_incident_scope, Unset):
            private_incident_scope = UNSET
        else:
            private_incident_scope = AnnouncementRuleV2PrivateIncidentScope(
                _private_incident_scope
            )

        template_id = d.pop("template_id", UNSET)

        announcement_rule_v2 = cls(
            condition_groups=condition_groups,
            conditions_no_longer_apply_behaviour=conditions_no_longer_apply_behaviour,
            created_at=created_at,
            id=id,
            microsoft_teams_channel_ids=microsoft_teams_channel_ids,
            mode=mode,
            name=name,
            owning_team_ids=owning_team_ids,
            slack_channel_ids=slack_channel_ids,
            update_sharing_mode=update_sharing_mode,
            updated_at=updated_at,
            private_incident_scope=private_incident_scope,
            template_id=template_id,
        )

        announcement_rule_v2.additional_properties = d
        return announcement_rule_v2

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
