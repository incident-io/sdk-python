from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_rules_create_payload_v2_conditions_no_longer_apply_behaviour import (
    AnnouncementRulesCreatePayloadV2ConditionsNoLongerApplyBehaviour,
)
from ..models.announcement_rules_create_payload_v2_mode import (
    AnnouncementRulesCreatePayloadV2Mode,
)
from ..models.announcement_rules_create_payload_v2_private_incident_scope import (
    AnnouncementRulesCreatePayloadV2PrivateIncidentScope,
)
from ..models.announcement_rules_create_payload_v2_update_sharing_mode import (
    AnnouncementRulesCreatePayloadV2UpdateSharingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2


T = TypeVar("T", bound="AnnouncementRulesCreatePayloadV2")


@_attrs_define(kw_only=True)
class AnnouncementRulesCreatePayloadV2:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'conditions_no_longer_apply_behaviour':
            'leave_in_place', 'microsoft_teams_channel_ids': ['19:abc@thread.tacv2/19:def@thread.tacv2'], 'mode':
            'live_and_closed', 'name': 'Data Breaches', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'],
            'private_incident_scope': 'all', 'slack_channel_ids': ['C02AW36C1M5'], 'template_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'update_sharing_mode': 'none'}

    Attributes:
        condition_groups (list[ConditionGroupPayloadV2]): Incidents are announced when they match any of these condition
            groups Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        mode (AnnouncementRulesCreatePayloadV2Mode): Which incidents are announced: live incidents only, or triage
            incidents too Example: live_and_closed.
        name (str): Human readable name for the rule Example: Data Breaches.
        update_sharing_mode (AnnouncementRulesCreatePayloadV2UpdateSharingMode): Where incident updates are shared once
            the incident is announced Example: none.
        conditions_no_longer_apply_behaviour (AnnouncementRulesCreatePayloadV2ConditionsNoLongerApplyBehaviour | Unset):
            Whether to remove announcement posts when the incident no longer matches this rule's conditions. Defaults to
            leaving them in place. Example: leave_in_place.
        microsoft_teams_channel_ids (list[str] | Unset): Microsoft Teams channels to post announcements into, as
            team_id/channel_id. Required when the organisation uses Microsoft Teams. Example:
            ['19:abc@thread.tacv2/19:def@thread.tacv2'].
        owning_team_ids (list[str] | Unset): IDs of the teams that own this rule Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        private_incident_scope (AnnouncementRulesCreatePayloadV2PrivateIncidentScope | Unset): Which private incidents
            this rule announces: every private incident (all), those an owning team can see (owning_teams), or none.
            Defaults to none on create, and is left unchanged on update when omitted. Example: all.
        slack_channel_ids (list[str] | Unset): IDs of the Slack channels to post announcements into. Required when the
            organisation uses Slack. Example: ['C02AW36C1M5'].
        template_id (str | Unset): ID of the announcement template used to render this rule's posts. Defaults to the
            organisation's default template when omitted. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    condition_groups: list[ConditionGroupPayloadV2]
    mode: AnnouncementRulesCreatePayloadV2Mode
    name: str
    update_sharing_mode: AnnouncementRulesCreatePayloadV2UpdateSharingMode
    conditions_no_longer_apply_behaviour: (
        AnnouncementRulesCreatePayloadV2ConditionsNoLongerApplyBehaviour | Unset
    ) = UNSET
    microsoft_teams_channel_ids: list[str] | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    private_incident_scope: (
        AnnouncementRulesCreatePayloadV2PrivateIncidentScope | Unset
    ) = UNSET
    slack_channel_ids: list[str] | Unset = UNSET
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        mode = self.mode.value

        name = self.name

        update_sharing_mode = self.update_sharing_mode.value

        conditions_no_longer_apply_behaviour: str | Unset = UNSET
        if not isinstance(self.conditions_no_longer_apply_behaviour, Unset):
            conditions_no_longer_apply_behaviour = (
                self.conditions_no_longer_apply_behaviour.value
            )

        microsoft_teams_channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.microsoft_teams_channel_ids, Unset):
            microsoft_teams_channel_ids = self.microsoft_teams_channel_ids

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        private_incident_scope: str | Unset = UNSET
        if not isinstance(self.private_incident_scope, Unset):
            private_incident_scope = self.private_incident_scope.value

        slack_channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.slack_channel_ids, Unset):
            slack_channel_ids = self.slack_channel_ids

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "mode": mode,
                "name": name,
                "update_sharing_mode": update_sharing_mode,
            }
        )
        if conditions_no_longer_apply_behaviour is not UNSET:
            field_dict["conditions_no_longer_apply_behaviour"] = (
                conditions_no_longer_apply_behaviour
            )
        if microsoft_teams_channel_ids is not UNSET:
            field_dict["microsoft_teams_channel_ids"] = microsoft_teams_channel_ids
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if private_incident_scope is not UNSET:
            field_dict["private_incident_scope"] = private_incident_scope
        if slack_channel_ids is not UNSET:
            field_dict["slack_channel_ids"] = slack_channel_ids
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )

        d = dict(src_dict)
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        mode = AnnouncementRulesCreatePayloadV2Mode(d.pop("mode"))

        name = d.pop("name")

        update_sharing_mode = AnnouncementRulesCreatePayloadV2UpdateSharingMode(
            d.pop("update_sharing_mode")
        )

        _conditions_no_longer_apply_behaviour = d.pop(
            "conditions_no_longer_apply_behaviour", UNSET
        )
        conditions_no_longer_apply_behaviour: (
            AnnouncementRulesCreatePayloadV2ConditionsNoLongerApplyBehaviour | Unset
        )
        if isinstance(_conditions_no_longer_apply_behaviour, Unset):
            conditions_no_longer_apply_behaviour = UNSET
        else:
            conditions_no_longer_apply_behaviour = (
                AnnouncementRulesCreatePayloadV2ConditionsNoLongerApplyBehaviour(
                    _conditions_no_longer_apply_behaviour
                )
            )

        microsoft_teams_channel_ids = cast(
            list[str], d.pop("microsoft_teams_channel_ids", UNSET)
        )

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        _private_incident_scope = d.pop("private_incident_scope", UNSET)
        private_incident_scope: (
            AnnouncementRulesCreatePayloadV2PrivateIncidentScope | Unset
        )
        if isinstance(_private_incident_scope, Unset):
            private_incident_scope = UNSET
        else:
            private_incident_scope = (
                AnnouncementRulesCreatePayloadV2PrivateIncidentScope(
                    _private_incident_scope
                )
            )

        slack_channel_ids = cast(list[str], d.pop("slack_channel_ids", UNSET))

        template_id = d.pop("template_id", UNSET)

        announcement_rules_create_payload_v2 = cls(
            condition_groups=condition_groups,
            mode=mode,
            name=name,
            update_sharing_mode=update_sharing_mode,
            conditions_no_longer_apply_behaviour=conditions_no_longer_apply_behaviour,
            microsoft_teams_channel_ids=microsoft_teams_channel_ids,
            owning_team_ids=owning_team_ids,
            private_incident_scope=private_incident_scope,
            slack_channel_ids=slack_channel_ids,
            template_id=template_id,
        )

        announcement_rules_create_payload_v2.additional_properties = d
        return announcement_rules_create_payload_v2

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
