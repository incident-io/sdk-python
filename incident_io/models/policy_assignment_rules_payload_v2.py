from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2
    from ..models.policy_reminder_cadence_v2 import PolicyReminderCadenceV2


T = TypeVar("T", bound="PolicyAssignmentRulesPayloadV2")


@_attrs_define(kw_only=True)
class PolicyAssignmentRulesPayloadV2:
    """
    Example:
        {'bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'reminder_cadence_after': {'interval': 'daily'},
            'reminder_cadence_before': {'interval': 'daily'}, 'reminder_detected_date_offset_hours': [0, 48],
            'reminder_due_date_offset_hours': [-24, 0, 24]}

    Attributes:
        bindings (list[EngineParamBindingPayloadV2]): Bindings which define the user to be assigned. We will assign the
            first user which evaluates; the rest are fallback values Example: [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}].
        reminder_due_date_offset_hours (list[int]): List of hours relative to the due date to remind the assignee.
            Negative values are before the due date, positive after. Example: [-24, 0, 24].
        reminder_cadence_after (PolicyReminderCadenceV2 | Unset): A recurring reminder, which repeats once per interval
            until the finding is resolved. Example: {'interval': 'daily'}.
        reminder_cadence_before (PolicyReminderCadenceV2 | Unset): A recurring reminder, which repeats once per interval
            until the finding is resolved. Example: {'interval': 'daily'}.
        reminder_detected_date_offset_hours (list[int] | Unset): List of hours relative to when the finding was detected
            to remind the assignee. Non-negative only; 0 means immediately on detection. Only valid for policy types that
            support detection reminders (e.g. schedule). Example: [0, 48].
    """

    bindings: list[EngineParamBindingPayloadV2]
    reminder_due_date_offset_hours: list[int]
    reminder_cadence_after: PolicyReminderCadenceV2 | Unset = UNSET
    reminder_cadence_before: PolicyReminderCadenceV2 | Unset = UNSET
    reminder_detected_date_offset_hours: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bindings = []
        for bindings_item_data in self.bindings:
            bindings_item = bindings_item_data.to_dict()
            bindings.append(bindings_item)

        reminder_due_date_offset_hours = self.reminder_due_date_offset_hours

        reminder_cadence_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reminder_cadence_after, Unset):
            reminder_cadence_after = self.reminder_cadence_after.to_dict()

        reminder_cadence_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reminder_cadence_before, Unset):
            reminder_cadence_before = self.reminder_cadence_before.to_dict()

        reminder_detected_date_offset_hours: list[int] | Unset = UNSET
        if not isinstance(self.reminder_detected_date_offset_hours, Unset):
            reminder_detected_date_offset_hours = (
                self.reminder_detected_date_offset_hours
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bindings": bindings,
                "reminder_due_date_offset_hours": reminder_due_date_offset_hours,
            }
        )
        if reminder_cadence_after is not UNSET:
            field_dict["reminder_cadence_after"] = reminder_cadence_after
        if reminder_cadence_before is not UNSET:
            field_dict["reminder_cadence_before"] = reminder_cadence_before
        if reminder_detected_date_offset_hours is not UNSET:
            field_dict["reminder_detected_date_offset_hours"] = (
                reminder_detected_date_offset_hours
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v2 import (
            EngineParamBindingPayloadV2,
        )
        from ..models.policy_reminder_cadence_v2 import (
            PolicyReminderCadenceV2,
        )

        d = dict(src_dict)
        bindings = []
        _bindings = d.pop("bindings")
        for bindings_item_data in _bindings:
            bindings_item = EngineParamBindingPayloadV2.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        reminder_due_date_offset_hours = cast(
            list[int], d.pop("reminder_due_date_offset_hours")
        )

        _reminder_cadence_after = d.pop("reminder_cadence_after", UNSET)
        reminder_cadence_after: PolicyReminderCadenceV2 | Unset
        if isinstance(_reminder_cadence_after, Unset):
            reminder_cadence_after = UNSET
        else:
            reminder_cadence_after = PolicyReminderCadenceV2.from_dict(
                _reminder_cadence_after
            )

        _reminder_cadence_before = d.pop("reminder_cadence_before", UNSET)
        reminder_cadence_before: PolicyReminderCadenceV2 | Unset
        if isinstance(_reminder_cadence_before, Unset):
            reminder_cadence_before = UNSET
        else:
            reminder_cadence_before = PolicyReminderCadenceV2.from_dict(
                _reminder_cadence_before
            )

        reminder_detected_date_offset_hours = cast(
            list[int], d.pop("reminder_detected_date_offset_hours", UNSET)
        )

        policy_assignment_rules_payload_v2 = cls(
            bindings=bindings,
            reminder_due_date_offset_hours=reminder_due_date_offset_hours,
            reminder_cadence_after=reminder_cadence_after,
            reminder_cadence_before=reminder_cadence_before,
            reminder_detected_date_offset_hours=reminder_detected_date_offset_hours,
        )

        policy_assignment_rules_payload_v2.additional_properties = d
        return policy_assignment_rules_payload_v2

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
