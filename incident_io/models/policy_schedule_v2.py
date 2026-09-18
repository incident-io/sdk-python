from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_schedule_v2_evaluation_level import PolicyScheduleV2EvaluationLevel
from ..models.policy_schedule_v2_requirement_type import PolicyScheduleV2RequirementType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyScheduleV2")


@_attrs_define
class PolicyScheduleV2:
    """Detects gaps in on-call coverage. Set when policy_type is schedule.

    Example:
        {'evaluation_level': 'schedule', 'requirement_type': 'contiguous'}

    Attributes:
        requirement_type (PolicyScheduleV2RequirementType):  Example: contiguous.
        evaluation_level (PolicyScheduleV2EvaluationLevel | Unset): Evaluate coverage across the whole schedule, or per
            rotation. Defaults to schedule. Example: schedule.
    """

    requirement_type: PolicyScheduleV2RequirementType
    evaluation_level: PolicyScheduleV2EvaluationLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requirement_type = self.requirement_type.value

        evaluation_level: str | Unset = UNSET
        if not isinstance(self.evaluation_level, Unset):
            evaluation_level = self.evaluation_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requirement_type": requirement_type,
            }
        )
        if evaluation_level is not UNSET:
            field_dict["evaluation_level"] = evaluation_level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        requirement_type = PolicyScheduleV2RequirementType(d.pop("requirement_type"))

        _evaluation_level = d.pop("evaluation_level", UNSET)
        evaluation_level: PolicyScheduleV2EvaluationLevel | Unset
        if isinstance(_evaluation_level, Unset):
            evaluation_level = UNSET
        else:
            evaluation_level = PolicyScheduleV2EvaluationLevel(_evaluation_level)

        policy_schedule_v2 = cls(
            requirement_type=requirement_type,
            evaluation_level=evaluation_level,
        )

        policy_schedule_v2.additional_properties = d
        return policy_schedule_v2

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
