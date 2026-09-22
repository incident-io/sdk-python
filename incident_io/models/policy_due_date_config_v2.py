from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_due_date_config_v2_calculation_type import (
    PolicyDueDateConfigV2CalculationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="PolicyDueDateConfigV2")


@_attrs_define(kw_only=True)
class PolicyDueDateConfigV2:
    """
    Example:
        {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type':
            'weekdays', 'days': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        calculation_type (PolicyDueDateConfigV2CalculationType):  Example: weekdays.
        days (EngineParamBindingV2):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}.
        incident_timestamp_id (str): Timestamp the due date counts from Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        applies_from (datetime.datetime | Unset): If set, the policy only applies to resources from this timestamp
            onwards Example: 2021-08-17T13:28:57.801578Z.
        calculation_timezone (str | Unset): Timezone the due date is calculated in. Only meaningful when
            calculation_type is weekdays. Example: Europe/London.
    """

    calculation_type: PolicyDueDateConfigV2CalculationType
    days: EngineParamBindingV2
    incident_timestamp_id: str
    applies_from: datetime.datetime | Unset = UNSET
    calculation_timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_type = self.calculation_type.value

        days = self.days.to_dict()

        incident_timestamp_id = self.incident_timestamp_id

        applies_from: str | Unset = UNSET
        if not isinstance(self.applies_from, Unset):
            applies_from = self.applies_from.isoformat()

        calculation_timezone = self.calculation_timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculation_type": calculation_type,
                "days": days,
                "incident_timestamp_id": incident_timestamp_id,
            }
        )
        if applies_from is not UNSET:
            field_dict["applies_from"] = applies_from
        if calculation_timezone is not UNSET:
            field_dict["calculation_timezone"] = calculation_timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_v2 import (
            EngineParamBindingV2,
        )

        d = dict(src_dict)
        calculation_type = PolicyDueDateConfigV2CalculationType(
            d.pop("calculation_type")
        )

        days = EngineParamBindingV2.from_dict(d.pop("days"))

        incident_timestamp_id = d.pop("incident_timestamp_id")

        _applies_from = d.pop("applies_from", UNSET)
        applies_from: datetime.datetime | Unset
        if isinstance(_applies_from, Unset):
            applies_from = UNSET
        else:
            applies_from = datetime.datetime.fromisoformat(_applies_from)

        calculation_timezone = d.pop("calculation_timezone", UNSET)

        policy_due_date_config_v2 = cls(
            calculation_type=calculation_type,
            days=days,
            incident_timestamp_id=incident_timestamp_id,
            applies_from=applies_from,
            calculation_timezone=calculation_timezone,
        )

        policy_due_date_config_v2.additional_properties = d
        return policy_due_date_config_v2

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
