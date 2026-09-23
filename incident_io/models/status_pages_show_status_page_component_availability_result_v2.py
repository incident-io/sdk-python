from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_component_availability_v2 import (
        StatusPageComponentAvailabilityV2,
    )


T = TypeVar("T", bound="StatusPagesShowStatusPageComponentAvailabilityResultV2")


@_attrs_define(kw_only=True)
class StatusPagesShowStatusPageComponentAvailabilityResultV2:
    """
    Example:
        {'availability': {'availability_percent': '99.94', 'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'data_available_since': '2025-06-01T00:00:00Z', 'end_at': '2026-02-01T00:00:00Z', 'start_at':
            '2026-01-01T00:00:00Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0'}}

    Attributes:
        availability (StatusPageComponentAvailabilityV2): Availability of a status page component over a requested time
            window. Example: {'availability_percent': '99.94', 'component_id': '01FCNDV6P870EA6S7TK1DSYDG1',
            'data_available_since': '2025-06-01T00:00:00Z', 'end_at': '2026-02-01T00:00:00Z', 'start_at':
            '2026-01-01T00:00:00Z', 'status_page_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    availability: StatusPageComponentAvailabilityV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability = self.availability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availability": availability,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_component_availability_v2 import (
            StatusPageComponentAvailabilityV2,
        )

        d = dict(src_dict)
        availability = StatusPageComponentAvailabilityV2.from_dict(
            d.pop("availability")
        )

        status_pages_show_status_page_component_availability_result_v2 = cls(
            availability=availability,
        )

        status_pages_show_status_page_component_availability_result_v2.additional_properties = d
        return status_pages_show_status_page_component_availability_result_v2

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
