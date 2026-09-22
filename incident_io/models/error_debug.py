from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ErrorDebug")


@_attrs_define(kw_only=True)
class ErrorDebug:
    """
    Example:
        {'message': 'Something broke: and something else: and something else', 'stacktrace': ['thing.go:123']}

    Attributes:
        message (str): Original internal error message Example: Something broke: and something else: and something else.
        stacktrace (list[str]): Stacktrace of the error, if applicable Example: ['thing.go:123'].
    """

    message: str
    stacktrace: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        stacktrace = self.stacktrace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "stacktrace": stacktrace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message = d.pop("message")

        stacktrace = cast(list[str], d.pop("stacktrace"))

        error_debug = cls(
            message=message,
            stacktrace=stacktrace,
        )

        error_debug.additional_properties = d
        return error_debug

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
