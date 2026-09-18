from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_single_metadata import ErrorSingleMetadata
    from ..models.error_source import ErrorSource


T = TypeVar("T", bound="ErrorSingle")


@_attrs_define
class ErrorSingle:
    """
    Example:
        {'code': 'trial_expired', 'message': 'Default incident call link must be a valid URL', 'metadata': {'abc123':
            'abc123'}, 'source': {'field': 'default_call_url', 'pointer': '/settings/default_call_url'}}

    Attributes:
        code (str): Machine-readable identifier for this specific error Example: trial_expired.
        message (str): Human readable description of the error Example: Default incident call link must be a valid URL.
        metadata (ErrorSingleMetadata | Unset): Additional metadata about the error, keyed by a string identifier
            Example: {'abc123': 'abc123'}.
        source (ErrorSource | Unset):  Example: {'field': 'default_call_url', 'pointer': '/settings/default_call_url'}.
    """

    code: str
    message: str
    metadata: ErrorSingleMetadata | Unset = UNSET
    source: ErrorSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_single_metadata import ErrorSingleMetadata
        from ..models.error_source import ErrorSource

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _metadata = d.pop("metadata", UNSET)
        metadata: ErrorSingleMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ErrorSingleMetadata.from_dict(_metadata)

        _source = d.pop("source", UNSET)
        source: ErrorSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ErrorSource.from_dict(_source)

        error_single = cls(
            code=code,
            message=message,
            metadata=metadata,
            source=source,
        )

        error_single.additional_properties = d
        return error_single

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
