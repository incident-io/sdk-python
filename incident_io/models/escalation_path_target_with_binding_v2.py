from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_target_with_binding_v2_schedule_mode import (
    EscalationPathTargetWithBindingV2ScheduleMode,
)
from ..models.escalation_path_target_with_binding_v2_type import (
    EscalationPathTargetWithBindingV2Type,
)
from ..models.escalation_path_target_with_binding_v2_urgency import (
    EscalationPathTargetWithBindingV2Urgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="EscalationPathTargetWithBindingV2")


@_attrs_define
class EscalationPathTargetWithBindingV2:
    """
    Example:
        {'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'schedule_mode': 'currently_on_call',
            'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}

    Attributes:
        type_ (EscalationPathTargetWithBindingV2Type): Controls what type of entity this target identifies, such as
            EscalationPolicy or User Example: schedule.
        urgency (EscalationPathTargetWithBindingV2Urgency): The urgency of this escalation path target Example: high.
        binding (EngineParamBindingV2 | Unset):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
        id (str | Unset): Uniquely identifies a concrete target. Omitted when binding is set. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        schedule_mode (EscalationPathTargetWithBindingV2ScheduleMode | Unset): Only set for schedule targets, this
            specifies which users to fetch from the schedule. Example: currently_on_call.
        selected_rota_id (str | Unset): For schedule targets, identifies which rota on the schedule the schedule_mode
            applies to. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    type_: EscalationPathTargetWithBindingV2Type
    urgency: EscalationPathTargetWithBindingV2Urgency
    binding: EngineParamBindingV2 | Unset = UNSET
    id: str | Unset = UNSET
    schedule_mode: EscalationPathTargetWithBindingV2ScheduleMode | Unset = UNSET
    selected_rota_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        urgency = self.urgency.value

        binding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.to_dict()

        id = self.id

        schedule_mode: str | Unset = UNSET
        if not isinstance(self.schedule_mode, Unset):
            schedule_mode = self.schedule_mode.value

        selected_rota_id = self.selected_rota_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "urgency": urgency,
            }
        )
        if binding is not UNSET:
            field_dict["binding"] = binding
        if id is not UNSET:
            field_dict["id"] = id
        if schedule_mode is not UNSET:
            field_dict["schedule_mode"] = schedule_mode
        if selected_rota_id is not UNSET:
            field_dict["selected_rota_id"] = selected_rota_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )

        d = dict(src_dict)
        type_ = EscalationPathTargetWithBindingV2Type(d.pop("type"))

        urgency = EscalationPathTargetWithBindingV2Urgency(d.pop("urgency"))

        _binding = d.pop("binding", UNSET)
        binding: EngineParamBindingV2 | Unset
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = EngineParamBindingV2.from_dict(_binding)

        id = d.pop("id", UNSET)

        _schedule_mode = d.pop("schedule_mode", UNSET)
        schedule_mode: EscalationPathTargetWithBindingV2ScheduleMode | Unset
        if isinstance(_schedule_mode, Unset):
            schedule_mode = UNSET
        else:
            schedule_mode = EscalationPathTargetWithBindingV2ScheduleMode(
                _schedule_mode
            )

        selected_rota_id = d.pop("selected_rota_id", UNSET)

        escalation_path_target_with_binding_v2 = cls(
            type_=type_,
            urgency=urgency,
            binding=binding,
            id=id,
            schedule_mode=schedule_mode,
            selected_rota_id=selected_rota_id,
        )

        escalation_path_target_with_binding_v2.additional_properties = d
        return escalation_path_target_with_binding_v2

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
