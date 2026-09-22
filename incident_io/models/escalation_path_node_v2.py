from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_v2_type import EscalationPathNodeV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_delay_v2 import EscalationPathNodeDelayV2
    from ..models.escalation_path_node_escalation_path_v2 import (
        EscalationPathNodeEscalationPathV2,
    )
    from ..models.escalation_path_node_if_else_v2 import EscalationPathNodeIfElseV2
    from ..models.escalation_path_node_level_v2 import EscalationPathNodeLevelV2
    from ..models.escalation_path_node_notify_channel_v2 import (
        EscalationPathNodeNotifyChannelV2,
    )
    from ..models.escalation_path_node_repeat_v2 import EscalationPathNodeRepeatV2


T = TypeVar("T", bound="EscalationPathNodeV2")


@_attrs_define(kw_only=True)
class EscalationPathNodeV2:
    """
    Example:
        {'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}

    Attributes:
        id (str): An ID for this node, unique within the escalation path.

            This allows you to reference the node in other nodes, such as when configuring a 'repeat' node. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        type_ (EscalationPathNodeV2Type): The type of this node. Available types are:
            * level: A set of targets (users or schedules) that should be paged, either all at once, or with a round-robin
            configuration.
            * notify_channel: Send the escalation to a Slack channel, where it can be acked by anyone in the channel.
            * if_else: Branch the escalation based on a set of conditions.
            * repeat: Go back to a previous node and repeat the logic from there.
            * delay: Pause the escalation for a configured duration before advancing to the next node.
            * escalation_path: Reassign the escalation to another escalation path, continuing from that path's first node.
            * voicemail: Send an inbound caller to voicemail. Only valid inside a call route's path. Example: if_else.
        delay (EscalationPathNodeDelayV2 | Unset):  Example: {'delay_interval_condition': 'active', 'delay_seconds':
            300, 'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        escalation_path (EscalationPathNodeEscalationPathV2 | Unset):  Example: {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
        if_else (EscalationPathNodeIfElseV2 | Unset):  Example: {'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode':
            'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'then_path': [{'delay':
            {'delay_interval_condition': 'active', 'delay_seconds': 300, 'delay_weekday_interval_config_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config':
            {'attempts': 3, 'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120},
            'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'repeat': {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}]}.
        level (EscalationPathNodeLevelV2 | Unset):  Example: {'ack_mode': 'all', 'retry_config': {'attempts': 3,
            'interval_seconds': 300}, 'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        notify_channel (EscalationPathNodeNotifyChannelV2 | Unset):  Example: {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        repeat (EscalationPathNodeRepeatV2 | Unset):  Example: {'repeat_times': 3, 'to_node':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    id: str
    type_: EscalationPathNodeV2Type
    delay: EscalationPathNodeDelayV2 | Unset = UNSET
    escalation_path: EscalationPathNodeEscalationPathV2 | Unset = UNSET
    if_else: EscalationPathNodeIfElseV2 | Unset = UNSET
    level: EscalationPathNodeLevelV2 | Unset = UNSET
    notify_channel: EscalationPathNodeNotifyChannelV2 | Unset = UNSET
    repeat: EscalationPathNodeRepeatV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        escalation_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalation_path, Unset):
            escalation_path = self.escalation_path.to_dict()

        if_else: dict[str, Any] | Unset = UNSET
        if not isinstance(self.if_else, Unset):
            if_else = self.if_else.to_dict()

        level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        notify_channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notify_channel, Unset):
            notify_channel = self.notify_channel.to_dict()

        repeat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat, Unset):
            repeat = self.repeat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay
        if escalation_path is not UNSET:
            field_dict["escalation_path"] = escalation_path
        if if_else is not UNSET:
            field_dict["if_else"] = if_else
        if level is not UNSET:
            field_dict["level"] = level
        if notify_channel is not UNSET:
            field_dict["notify_channel"] = notify_channel
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_node_delay_v2 import (
            EscalationPathNodeDelayV2,
        )
        from ..models.escalation_path_node_escalation_path_v2 import (
            EscalationPathNodeEscalationPathV2,
        )
        from ..models.escalation_path_node_if_else_v2 import (
            EscalationPathNodeIfElseV2,
        )
        from ..models.escalation_path_node_level_v2 import (
            EscalationPathNodeLevelV2,
        )
        from ..models.escalation_path_node_notify_channel_v2 import (
            EscalationPathNodeNotifyChannelV2,
        )
        from ..models.escalation_path_node_repeat_v2 import (
            EscalationPathNodeRepeatV2,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = EscalationPathNodeV2Type(d.pop("type"))

        _delay = d.pop("delay", UNSET)
        delay: EscalationPathNodeDelayV2 | Unset
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = EscalationPathNodeDelayV2.from_dict(_delay)

        _escalation_path = d.pop("escalation_path", UNSET)
        escalation_path: EscalationPathNodeEscalationPathV2 | Unset
        if isinstance(_escalation_path, Unset):
            escalation_path = UNSET
        else:
            escalation_path = EscalationPathNodeEscalationPathV2.from_dict(
                _escalation_path
            )

        _if_else = d.pop("if_else", UNSET)
        if_else: EscalationPathNodeIfElseV2 | Unset
        if isinstance(_if_else, Unset):
            if_else = UNSET
        else:
            if_else = EscalationPathNodeIfElseV2.from_dict(_if_else)

        _level = d.pop("level", UNSET)
        level: EscalationPathNodeLevelV2 | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = EscalationPathNodeLevelV2.from_dict(_level)

        _notify_channel = d.pop("notify_channel", UNSET)
        notify_channel: EscalationPathNodeNotifyChannelV2 | Unset
        if isinstance(_notify_channel, Unset):
            notify_channel = UNSET
        else:
            notify_channel = EscalationPathNodeNotifyChannelV2.from_dict(
                _notify_channel
            )

        _repeat = d.pop("repeat", UNSET)
        repeat: EscalationPathNodeRepeatV2 | Unset
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = EscalationPathNodeRepeatV2.from_dict(_repeat)

        escalation_path_node_v2 = cls(
            id=id,
            type_=type_,
            delay=delay,
            escalation_path=escalation_path,
            if_else=if_else,
            level=level,
            notify_channel=notify_channel,
            repeat=repeat,
        )

        escalation_path_node_v2.additional_properties = d
        return escalation_path_node_v2

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
