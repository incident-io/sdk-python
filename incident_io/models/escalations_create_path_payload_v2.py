from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalations_create_path_payload_v2_kind import (
    EscalationsCreatePathPayloadV2Kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_payload_v2 import EscalationPathNodePayloadV2
    from ..models.escalation_path_repeat_config_v2 import EscalationPathRepeatConfigV2
    from ..models.escalations_create_path_payload_v2_param_bindings import (
        EscalationsCreatePathPayloadV2ParamBindings,
    )
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationsCreatePathPayloadV2")


@_attrs_define
class EscalationsCreatePathPayloadV2:
    """
    Example:
        {'kind': 'templated', 'name': 'Urgent Support', 'param_bindings': {'abc123': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300},
            'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config': {'delay_repeat_on_activity':
            False, 'repeat_after_seconds': 1800}, 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'template_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}

    Attributes:
        name (str): The name of this escalation path, for the user's reference. Example: Urgent Support.
        path (list[EscalationPathNodePayloadV2]): The nodes that form the levels and branches of this escalation path.
            Example: [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300},
            'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        kind (EscalationsCreatePathPayloadV2Kind | Unset): Whether this path carries its own nodes, or is built from an
            escalation path template. Example: templated.
        param_bindings (EscalationsCreatePathPayloadV2ParamBindings | Unset): For a templated path, the values to bind
            to the template's declared parameters, keyed by parameter name. Example: {'abc123': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
        repeat_config (EscalationPathRepeatConfigV2 | Unset):  Example: {'delay_repeat_on_activity': False,
            'repeat_after_seconds': 1800}.
        team_ids (list[str] | Unset): IDs of the teams that own this escalation path. This will automatically sync
            escalation paths with the right teams in Catalog. If you have an escalation paths attribute on your Teams, this
            attribute is required. Example: ['01JPQA75EPNEES4479P16P4XAB'].
        template_id (str | Unset): For a templated path, the template to build it from. Required when kind is templated.
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        working_hours (list[WeekdayIntervalConfigV2] | Unset): The working hours for this escalation path. Example:
            [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}]}].
    """

    name: str
    path: list[EscalationPathNodePayloadV2]
    kind: EscalationsCreatePathPayloadV2Kind | Unset = UNSET
    param_bindings: EscalationsCreatePathPayloadV2ParamBindings | Unset = UNSET
    repeat_config: EscalationPathRepeatConfigV2 | Unset = UNSET
    team_ids: list[str] | Unset = UNSET
    template_id: str | Unset = UNSET
    working_hours: list[WeekdayIntervalConfigV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        param_bindings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.param_bindings, Unset):
            param_bindings = self.param_bindings.to_dict()

        repeat_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeat_config, Unset):
            repeat_config = self.repeat_config.to_dict()

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

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
                "name": name,
                "path": path,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if param_bindings is not UNSET:
            field_dict["param_bindings"] = param_bindings
        if repeat_config is not UNSET:
            field_dict["repeat_config"] = repeat_config
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.escalation_path_node_payload_v2 import (
            EscalationPathNodePayloadV2,
        )
        from ..models.escalation_path_repeat_config_v2 import (
            EscalationPathRepeatConfigV2,
        )
        from ..models.escalations_create_path_payload_v2_param_bindings import (
            EscalationsCreatePathPayloadV2ParamBindings,
        )
        from ..models.weekday_interval_config_v2 import (
            WeekdayIntervalConfigV2,
        )

        d = dict(src_dict)
        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathNodePayloadV2.from_dict(path_item_data)

            path.append(path_item)

        _kind = d.pop("kind", UNSET)
        kind: EscalationsCreatePathPayloadV2Kind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = EscalationsCreatePathPayloadV2Kind(_kind)

        _param_bindings = d.pop("param_bindings", UNSET)
        param_bindings: EscalationsCreatePathPayloadV2ParamBindings | Unset
        if isinstance(_param_bindings, Unset):
            param_bindings = UNSET
        else:
            param_bindings = EscalationsCreatePathPayloadV2ParamBindings.from_dict(
                _param_bindings
            )

        _repeat_config = d.pop("repeat_config", UNSET)
        repeat_config: EscalationPathRepeatConfigV2 | Unset
        if isinstance(_repeat_config, Unset):
            repeat_config = UNSET
        else:
            repeat_config = EscalationPathRepeatConfigV2.from_dict(_repeat_config)

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

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

        escalations_create_path_payload_v2 = cls(
            name=name,
            path=path,
            kind=kind,
            param_bindings=param_bindings,
            repeat_config=repeat_config,
            team_ids=team_ids,
            template_id=template_id,
            working_hours=working_hours,
        )

        escalations_create_path_payload_v2.additional_properties = d
        return escalations_create_path_payload_v2

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
