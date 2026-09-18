from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_status_v1 import IncidentStatusV1


T = TypeVar("T", bound="IncidentStatusesCreateResultV1")


@_attrs_define
class IncidentStatusesCreateResultV1:
    """
    Example:
        {'incident_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact
            has been **fully mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_status (IncidentStatusV1):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    incident_status: IncidentStatusV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_status = self.incident_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_status": incident_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_status_v1 import IncidentStatusV1

        d = dict(src_dict)
        incident_status = IncidentStatusV1.from_dict(d.pop("incident_status"))

        incident_statuses_create_result_v1 = cls(
            incident_status=incident_status,
        )

        incident_statuses_create_result_v1.additional_properties = d
        return incident_statuses_create_result_v1

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
