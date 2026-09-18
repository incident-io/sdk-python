from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentTemplateValidateWarningV1")


@_attrs_define
class IncidentTemplateValidateWarningV1:
    """Something suspect about a template config that isn't severe enough to reject it.

    Example:
        {'detail': 'Creating a new template with this name will fail. Updating the template that already has it keeps
            working.', 'summary': 'An incident template with this name already exists'}

    Attributes:
        detail (str): More detail about the warning and what to do about it Example: Creating a new template with this
            name will fail. Updating the template that already has it keeps working..
        summary (str): A short description of the warning Example: An incident template with this name already exists.
    """

    detail: str
    summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        detail = d.pop("detail")

        summary = d.pop("summary")

        incident_template_validate_warning_v1 = cls(
            detail=detail,
            summary=summary,
        )

        incident_template_validate_warning_v1.additional_properties = d
        return incident_template_validate_warning_v1

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
