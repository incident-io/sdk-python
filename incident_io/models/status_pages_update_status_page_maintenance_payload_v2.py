from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusPagesUpdateStatusPageMaintenancePayloadV2")


@_attrs_define
class StatusPagesUpdateStatusPageMaintenancePayloadV2:
    """
    Example:
        {'end_at': '2025-01-28T12:00:00Z', 'name': 'Routine infrastructure upgrade', 'start_at': '2025-01-28T10:00:00Z'}

    Attributes:
        end_at (datetime.datetime): The time the maintenance window ends Example: 2025-01-28T12:00:00Z.
        name (str): A title for the maintenance window Example: Routine infrastructure upgrade.
        start_at (datetime.datetime): The time the maintenance window starts Example: 2025-01-28T10:00:00Z.
    """

    end_at: datetime.datetime
    name: str
    start_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        name = self.name

        start_at = self.start_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "name": name,
                "start_at": start_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        name = d.pop("name")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        status_pages_update_status_page_maintenance_payload_v2 = cls(
            end_at=end_at,
            name=name,
            start_at=start_at,
        )

        status_pages_update_status_page_maintenance_payload_v2.additional_properties = d
        return status_pages_update_status_page_maintenance_payload_v2

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
