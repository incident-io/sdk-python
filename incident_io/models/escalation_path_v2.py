from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_v2_kind import EscalationPathV2Kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_v2 import EscalationPathNodeV2
    from ..models.escalation_path_repeat_config_v2 import EscalationPathRepeatConfigV2
    from ..models.escalation_path_v2_param_bindings import EscalationPathV2ParamBindings
    from ..models.user_v2 import UserV2
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationPathV2")


@_attrs_define
class EscalationPathV2:
    """
    Example:
        {'current_responders': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'kind':
            'templated', 'name': 'Urgent Support', 'param_bindings': {'abc123': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'path': [{'delay': {'delay_interval_condition': 'active',
            'delay_seconds': 300, 'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path':
            {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else':
            {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}],
            'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config': {'delay_repeat_on_activity':
            False, 'repeat_after_seconds': 1800}, 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}

    Attributes:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        kind (EscalationPathV2Kind): Whether this path carries its own nodes, or is built from an escalation path
            template. Example: templated.
        name (str): The name of this escalation path, for the user's reference. Example: Urgent Support.
        path (list[EscalationPathNodeV2]): The nodes that form the levels and branches of this escalation path. Empty
            for a templated path, which takes them from its template. Example: [{'delay': {'delay_interval_condition':
            'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}],
            'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        team_ids (list[str]): IDs of the teams that own this escalation path. This will automatically sync escalation
            paths with the right teams in Catalog. If you have an escalation paths attribute on your Teams, this attribute
            is required. Example: ['01JPQA75EPNEES4479P16P4XAB'].
        current_responders (list[UserV2] | Unset): Users who are currently on-call for this escalation path Example:
            [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'owner', 'slack_user_id': 'U02AYNF2XJM'}].
        param_bindings (EscalationPathV2ParamBindings | Unset): For a templated path, the values bound to the template's
            declared parameters, keyed by parameter name. Example: {'abc123': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}.
        repeat_config (EscalationPathRepeatConfigV2 | Unset):  Example: {'delay_repeat_on_activity': False,
            'repeat_after_seconds': 1800}.
        template_id (str | Unset): For a templated path, the template it is built from. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        working_hours (list[WeekdayIntervalConfigV2] | Unset): The working hours for this escalation path. Absent for a
            templated path, which takes them from its template. Example: [{'id': 'abc123', 'name': 'abc123', 'timezone':
            'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}].
    """

    id: str
    kind: EscalationPathV2Kind
    name: str
    path: list[EscalationPathNodeV2]
    team_ids: list[str]
    current_responders: list[UserV2] | Unset = UNSET
    param_bindings: EscalationPathV2ParamBindings | Unset = UNSET
    repeat_config: EscalationPathRepeatConfigV2 | Unset = UNSET
    template_id: str | Unset = UNSET
    working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        team_ids = self.team_ids

        current_responders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_responders, Unset):
            current_responders = []
            for current_responders_item_data in self.current_responders:
                current_responders_item = current_responders_item_data.to_dict()
                current_responders.append(current_responders_item)

        param_bindings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.param_bindings, Unset):
            param_bindings = self.param_bindings.to_dict()

        repeat_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat_config, Unset):
            repeat_config = self.repeat_config.to_dict()

        template_id = self.template_id

        working_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.working_hours, Unset):
            working_hours = []
            for working_hours_item_data in self.working_hours:
                working_hours_item = working_hours_item_data.to_dict()
                working_hours.append(working_hours_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "name": name,
                "path": path,
                "team_ids": team_ids,
            }
        )
        if current_responders is not UNSET:
            field_dict["current_responders"] = current_responders
        if param_bindings is not UNSET:
            field_dict["param_bindings"] = param_bindings
        if repeat_config is not UNSET:
            field_dict["repeat_config"] = repeat_config
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_node_v2 import (
            EscalationPathNodeV2,
        )
        from ..models.escalation_path_repeat_config_v2 import (
            EscalationPathRepeatConfigV2,
        )
        from ..models.escalation_path_v2_param_bindings import (
            EscalationPathV2ParamBindings,
        )
        from ..models.user_v2 import UserV2
        from ..models.weekday_interval_config_v2 import (
            WeekdayIntervalConfigV2,
        )

        d = dict(src_dict)
        id = d.pop("id")

        kind = EscalationPathV2Kind(d.pop("kind"))

        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathNodeV2.from_dict(path_item_data)

            path.append(path_item)

        team_ids = cast(list[str], d.pop("team_ids"))

        _current_responders = d.pop("current_responders", UNSET)
        current_responders: list[UserV2] | Unset = UNSET
        if _current_responders is not UNSET:
            current_responders = []
            for current_responders_item_data in _current_responders:
                current_responders_item = UserV2.from_dict(current_responders_item_data)

                current_responders.append(current_responders_item)

        _param_bindings = d.pop("param_bindings", UNSET)
        param_bindings: EscalationPathV2ParamBindings | Unset
        if isinstance(_param_bindings, Unset):
            param_bindings = UNSET
        else:
            param_bindings = EscalationPathV2ParamBindings.from_dict(_param_bindings)

        _repeat_config = d.pop("repeat_config", UNSET)
        repeat_config: EscalationPathRepeatConfigV2 | Unset
        if isinstance(_repeat_config, Unset):
            repeat_config = UNSET
        else:
            repeat_config = EscalationPathRepeatConfigV2.from_dict(_repeat_config)

        template_id = d.pop("template_id", UNSET)

        _working_hours = d.pop("working_hours", UNSET)
        working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
        if _working_hours is not UNSET:
            working_hours = []
            for working_hours_item_data in _working_hours:
                working_hours_item = WeekdayIntervalConfigV2.from_dict(
                    working_hours_item_data
                )

                working_hours.append(working_hours_item)

        escalation_path_v2 = cls(
            id=id,
            kind=kind,
            name=name,
            path=path,
            team_ids=team_ids,
            current_responders=current_responders,
            param_bindings=param_bindings,
            repeat_config=repeat_config,
            template_id=template_id,
            working_hours=working_hours,
        )

        escalation_path_v2.additional_properties = d
        return escalation_path_v2

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
