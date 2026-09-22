from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDelayV2")


@_attrs_define(kw_only=True)
class WorkflowDelayV2:
    """
    Example:
        {'conditions_apply_over_delay': False, 'for_seconds': 60}

    Attributes:
        conditions_apply_over_delay (bool): If this workflow is delayed, whether the conditions should be rechecked
            between trigger firing and execution Example: False.
        for_seconds (int): Delay in seconds between trigger firing and running the workflow Example: 60.
    """

    conditions_apply_over_delay: bool
    for_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions_apply_over_delay = self.conditions_apply_over_delay

        for_seconds = self.for_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions_apply_over_delay": conditions_apply_over_delay,
                "for_seconds": for_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        conditions_apply_over_delay = d.pop("conditions_apply_over_delay")

        for_seconds = d.pop("for_seconds")

        workflow_delay_v2 = cls(
            conditions_apply_over_delay=conditions_apply_over_delay,
            for_seconds=for_seconds,
        )

        workflow_delay_v2.additional_properties = d
        return workflow_delay_v2

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
