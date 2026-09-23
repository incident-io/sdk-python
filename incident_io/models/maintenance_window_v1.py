from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.condition_group_v2 import ConditionGroupV2
    from ..models.maintenance_window_escalation_target_v1 import (
        MaintenanceWindowEscalationTargetV1,
    )
    from ..models.maintenance_window_notify_channel_v1 import (
        MaintenanceWindowNotifyChannelV1,
    )


T = TypeVar("T", bound="MaintenanceWindowV1")


@_attrs_define(kw_only=True)
class MaintenanceWindowV1:
    """
    Example:
        {'alert_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'archived_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T14:28:57.801578Z', 'escalation_targets':
            [{'escalation_paths': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'users': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'lead': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to
            connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}, 'name': 'Planned database migration', 'notification_message': 'Scheduled downtime for database
            migration', 'notify_channels': [{'channel_id': 'C0ACTHQMHS8', 'channel_name': 'general', 'channel_type':
            'public', 'is_private': False}], 'notify_end_minutes_before': 5, 'notify_start_minutes_before': 15,
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'reroute_on_end': False, 'resolve_on_end': False,
            'show_in_sidebar': True, 'start_at': '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        alert_condition_groups (list[ConditionGroupV2]): Condition groups that determine which alerts this maintenance
            window applies to Example: [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}].
        created_at (datetime.datetime): When this maintenance window was created Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime): When the maintenance window ends Example: 2021-08-17T14:28:57.801578Z.
        id (str): Unique identifier for this maintenance window Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        lead (ActorV2):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage:
            PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}.
        name (str): Human readable name for the maintenance window Example: Planned database migration.
        reroute_on_end (bool): Whether to retrigger firing alerts through alert routing when the window ends Example:
            False.
        resolve_on_end (bool): Whether to automatically resolve all firing alerts that matched this window when it ends
            Example: False.
        show_in_sidebar (bool): Whether to show this maintenance window in the dashboard sidebar when active Example:
            True.
        start_at (datetime.datetime): When the maintenance window starts Example: 2021-08-17T13:28:57.801578Z.
        updated_at (datetime.datetime): When this maintenance window was last updated Example:
            2021-08-17T13:28:57.801578Z.
        archived_at (datetime.datetime | Unset): When this maintenance window was archived, if it has been Example:
            2021-08-17T13:28:57.801578Z.
        escalation_targets (list[MaintenanceWindowEscalationTargetV1] | Unset): If set, alerts matching this window will
            be escalated to these targets Example: [{'escalation_paths': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'users': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}}].
        incident_id (str | Unset): If set, alerts matching this window will be automatically attached to this incident
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        notification_message (str | Unset): Custom message included in notifications about this maintenance window
            Example: Scheduled downtime for database migration.
        notify_channels (list[MaintenanceWindowNotifyChannelV1] | Unset): Channels to notify about the maintenance
            window starting and ending Example: [{'channel_id': 'C0ACTHQMHS8', 'channel_name': 'general', 'channel_type':
            'public', 'is_private': False}].
        notify_end_minutes_before (int | Unset): Minutes before the end to send a notification to the configured
            channels Example: 5.
        notify_start_minutes_before (int | Unset): Minutes before the start to send a notification to the configured
            channels Example: 15.
        owning_team_ids (list[str] | Unset): IDs of teams that own this maintenance window. Owning teams control who can
            manage the window, and restrict it to holding alerts belonging to those teams or their descendants in the team
            hierarchy. Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    alert_condition_groups: list[ConditionGroupV2]
    created_at: datetime.datetime
    end_at: datetime.datetime
    id: str
    lead: ActorV2
    name: str
    reroute_on_end: bool
    resolve_on_end: bool
    show_in_sidebar: bool
    start_at: datetime.datetime
    updated_at: datetime.datetime
    archived_at: datetime.datetime | Unset = UNSET
    escalation_targets: list[MaintenanceWindowEscalationTargetV1] | Unset = UNSET
    incident_id: str | Unset = UNSET
    notification_message: str | Unset = UNSET
    notify_channels: list[MaintenanceWindowNotifyChannelV1] | Unset = UNSET
    notify_end_minutes_before: int | Unset = UNSET
    notify_start_minutes_before: int | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_condition_groups = []
        for alert_condition_groups_item_data in self.alert_condition_groups:
            alert_condition_groups_item = alert_condition_groups_item_data.to_dict()
            alert_condition_groups.append(alert_condition_groups_item)

        created_at = self.created_at.isoformat()

        end_at = self.end_at.isoformat()

        id = self.id

        lead = self.lead.to_dict()

        name = self.name

        reroute_on_end = self.reroute_on_end

        resolve_on_end = self.resolve_on_end

        show_in_sidebar = self.show_in_sidebar

        start_at = self.start_at.isoformat()

        updated_at = self.updated_at.isoformat()

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        escalation_targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.escalation_targets, Unset):
            escalation_targets = []
            for escalation_targets_item_data in self.escalation_targets:
                escalation_targets_item = escalation_targets_item_data.to_dict()
                escalation_targets.append(escalation_targets_item)

        incident_id = self.incident_id

        notification_message = self.notification_message

        notify_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notify_channels, Unset):
            notify_channels = []
            for notify_channels_item_data in self.notify_channels:
                notify_channels_item = notify_channels_item_data.to_dict()
                notify_channels.append(notify_channels_item)

        notify_end_minutes_before = self.notify_end_minutes_before

        notify_start_minutes_before = self.notify_start_minutes_before

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_condition_groups": alert_condition_groups,
                "created_at": created_at,
                "end_at": end_at,
                "id": id,
                "lead": lead,
                "name": name,
                "reroute_on_end": reroute_on_end,
                "resolve_on_end": resolve_on_end,
                "show_in_sidebar": show_in_sidebar,
                "start_at": start_at,
                "updated_at": updated_at,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if escalation_targets is not UNSET:
            field_dict["escalation_targets"] = escalation_targets
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if notification_message is not UNSET:
            field_dict["notification_message"] = notification_message
        if notify_channels is not UNSET:
            field_dict["notify_channels"] = notify_channels
        if notify_end_minutes_before is not UNSET:
            field_dict["notify_end_minutes_before"] = notify_end_minutes_before
        if notify_start_minutes_before is not UNSET:
            field_dict["notify_start_minutes_before"] = notify_start_minutes_before
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.condition_group_v2 import ConditionGroupV2
        from ..models.maintenance_window_escalation_target_v1 import (
            MaintenanceWindowEscalationTargetV1,
        )
        from ..models.maintenance_window_notify_channel_v1 import (
            MaintenanceWindowNotifyChannelV1,
        )

        d = dict(src_dict)
        alert_condition_groups = []
        _alert_condition_groups = d.pop("alert_condition_groups")
        for alert_condition_groups_item_data in _alert_condition_groups:
            alert_condition_groups_item = ConditionGroupV2.from_dict(
                alert_condition_groups_item_data
            )

            alert_condition_groups.append(alert_condition_groups_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        id = d.pop("id")

        lead = ActorV2.from_dict(d.pop("lead"))

        name = d.pop("name")

        reroute_on_end = d.pop("reroute_on_end")

        resolve_on_end = d.pop("resolve_on_end")

        show_in_sidebar = d.pop("show_in_sidebar")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        _escalation_targets = d.pop("escalation_targets", UNSET)
        escalation_targets: list[MaintenanceWindowEscalationTargetV1] | Unset = UNSET
        if _escalation_targets is not UNSET:
            escalation_targets = []
            for escalation_targets_item_data in _escalation_targets:
                escalation_targets_item = MaintenanceWindowEscalationTargetV1.from_dict(
                    escalation_targets_item_data
                )

                escalation_targets.append(escalation_targets_item)

        incident_id = d.pop("incident_id", UNSET)

        notification_message = d.pop("notification_message", UNSET)

        _notify_channels = d.pop("notify_channels", UNSET)
        notify_channels: list[MaintenanceWindowNotifyChannelV1] | Unset = UNSET
        if _notify_channels is not UNSET:
            notify_channels = []
            for notify_channels_item_data in _notify_channels:
                notify_channels_item = MaintenanceWindowNotifyChannelV1.from_dict(
                    notify_channels_item_data
                )

                notify_channels.append(notify_channels_item)

        notify_end_minutes_before = d.pop("notify_end_minutes_before", UNSET)

        notify_start_minutes_before = d.pop("notify_start_minutes_before", UNSET)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        maintenance_window_v1 = cls(
            alert_condition_groups=alert_condition_groups,
            created_at=created_at,
            end_at=end_at,
            id=id,
            lead=lead,
            name=name,
            reroute_on_end=reroute_on_end,
            resolve_on_end=resolve_on_end,
            show_in_sidebar=show_in_sidebar,
            start_at=start_at,
            updated_at=updated_at,
            archived_at=archived_at,
            escalation_targets=escalation_targets,
            incident_id=incident_id,
            notification_message=notification_message,
            notify_channels=notify_channels,
            notify_end_minutes_before=notify_end_minutes_before,
            notify_start_minutes_before=notify_start_minutes_before,
            owning_team_ids=owning_team_ids,
        )

        maintenance_window_v1.additional_properties = d
        return maintenance_window_v1

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
