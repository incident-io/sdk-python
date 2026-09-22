from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_finding_schedule_impacted_user_v2_cause import (
    PolicyFindingScheduleImpactedUserV2Cause,
)

T = TypeVar("T", bound="PolicyFindingScheduleImpactedUserV2")


@_attrs_define(kw_only=True)
class PolicyFindingScheduleImpactedUserV2:
    """
    Example:
        {'cause': 'no_on_call_seat', 'name': 'Alice Green', 'user_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        cause (PolicyFindingScheduleImpactedUserV2Cause): Why this user's entries don't count as cover Example:
            no_on_call_seat.
        name (str):  Example: Alice Green.
        user_id (str):  Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    cause: PolicyFindingScheduleImpactedUserV2Cause
    name: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cause = self.cause.value

        name = self.name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cause": cause,
                "name": name,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cause = PolicyFindingScheduleImpactedUserV2Cause(d.pop("cause"))

        name = d.pop("name")

        user_id = d.pop("user_id")

        policy_finding_schedule_impacted_user_v2 = cls(
            cause=cause,
            name=name,
            user_id=user_id,
        )

        policy_finding_schedule_impacted_user_v2.additional_properties = d
        return policy_finding_schedule_impacted_user_v2

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
