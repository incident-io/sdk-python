from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageComponentAvailabilityV2")


@_attrs_define(kw_only=True)
class StatusPageComponentAvailabilityV2:
    """Availability of a status page component over a requested time window.

    Example:
        {'availability_percent': '99.94', 'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'data_available_since':
            '2025-06-01T00:00:00Z', 'end_at': '2026-02-01T00:00:00Z', 'start_at': '2026-01-01T00:00:00Z', 'status_page_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        component_id (str): ID of the component. This may be found by calling the ShowStatusPageStructure endpoint.
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
        data_available_since (datetime.datetime): Earliest time we have status data for this component. Before this,
            availability is unknown rather than assumed operational. Example: 2025-06-01T00:00:00Z.
        end_at (datetime.datetime): End of the requested availability window Example: 2026-02-01T00:00:00Z.
        start_at (datetime.datetime): Start of the requested availability window Example: 2026-01-01T00:00:00Z.
        status_page_id (str): ID of the status page Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        availability_percent (str | Unset): Availability over the window as a percentage, floored (for example "99.94").
            Omitted when we have no data covering the window. Example: 99.94.
    """

    component_id: str
    data_available_since: datetime.datetime
    end_at: datetime.datetime
    start_at: datetime.datetime
    status_page_id: str
    availability_percent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        data_available_since = self.data_available_since.isoformat()

        end_at = self.end_at.isoformat()

        start_at = self.start_at.isoformat()

        status_page_id = self.status_page_id

        availability_percent = self.availability_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "data_available_since": data_available_since,
                "end_at": end_at,
                "start_at": start_at,
                "status_page_id": status_page_id,
            }
        )
        if availability_percent is not UNSET:
            field_dict["availability_percent"] = availability_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        data_available_since = datetime.datetime.fromisoformat(
            d.pop("data_available_since")
        )

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        status_page_id = d.pop("status_page_id")

        availability_percent = d.pop("availability_percent", UNSET)

        status_page_component_availability_v2 = cls(
            component_id=component_id,
            data_available_since=data_available_since,
            end_at=end_at,
            start_at=start_at,
            status_page_id=status_page_id,
            availability_percent=availability_percent,
        )

        status_page_component_availability_v2.additional_properties = d
        return status_page_component_availability_v2

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
