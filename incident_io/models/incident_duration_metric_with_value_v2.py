from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_duration_metric_with_value_v2_status import (
    IncidentDurationMetricWithValueV2Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_duration_metric_v2 import IncidentDurationMetricV2


T = TypeVar("T", bound="IncidentDurationMetricWithValueV2")


@_attrs_define
class IncidentDurationMetricWithValueV2:
    """
    Example:
        {'duration_metric': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}, 'status': 'success',
            'value_seconds': 10800}

    Attributes:
        duration_metric (IncidentDurationMetricV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}.
        status (IncidentDurationMetricWithValueV2Status): Whether value_seconds matches this incident's current
            timestamps ('success'), or why it doesn't Example: success.
        value_seconds (int | Unset): The duration we last calculated for this metric, omitted if we've never calculated
            one. If status isn't 'success', this incident's timestamps have changed since and no longer match this value
            Example: 10800.
    """

    duration_metric: IncidentDurationMetricV2
    status: IncidentDurationMetricWithValueV2Status
    value_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_metric = self.duration_metric.to_dict()

        status = self.status.value

        value_seconds = self.value_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_metric": duration_metric,
                "status": status,
            }
        )
        if value_seconds is not UNSET:
            field_dict["value_seconds"] = value_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_duration_metric_v2 import (
            IncidentDurationMetricV2,
        )

        d = dict(src_dict)
        duration_metric = IncidentDurationMetricV2.from_dict(d.pop("duration_metric"))

        status = IncidentDurationMetricWithValueV2Status(d.pop("status"))

        value_seconds = d.pop("value_seconds", UNSET)

        incident_duration_metric_with_value_v2 = cls(
            duration_metric=duration_metric,
            status=status,
            value_seconds=value_seconds,
        )

        incident_duration_metric_with_value_v2.additional_properties = d
        return incident_duration_metric_with_value_v2

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
