from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.severity_v1 import SeverityV1


T = TypeVar("T", bound="SeveritiesCreateResultV1")


@_attrs_define
class SeveritiesCreateResultV1:
    """
    Example:
        {'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        severity (SeverityV1):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low
            impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    severity: SeverityV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.severity_v1 import SeverityV1

        d = dict(src_dict)
        severity = SeverityV1.from_dict(d.pop("severity"))

        severities_create_result_v1 = cls(
            severity=severity,
        )

        severities_create_result_v1.additional_properties = d
        return severities_create_result_v1

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
