from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_response_type import ErrorResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_debug import ErrorDebug
    from ..models.error_rate_limit import ErrorRateLimit
    from ..models.error_single import ErrorSingle


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Example:
        {'debug': {'message': 'Something broke: and something else: and something else', 'stacktrace':
            ['thing.go:123']}, 'errors': [{'code': 'trial_expired', 'message': 'Default incident call link must be a valid
            URL', 'metadata': {'abc123': 'abc123'}, 'source': {'field': 'default_call_url', 'pointer':
            '/settings/default_call_url'}}], 'rate_limit': {'limit': 100, 'name': 'client_ip', 'remaining': 98,
            'retry_after': '2020-01-01T00:00:00Z'}, 'request_id': '2T1p0e3j', 'status': 408, 'type':
            'invalid_request_error'}

    Attributes:
        errors (list[ErrorSingle]): List of errors that caused this request to fail Example: [{'code': 'trial_expired',
            'message': 'Default incident call link must be a valid URL', 'metadata': {'abc123': 'abc123'}, 'source':
            {'field': 'default_call_url', 'pointer': '/settings/default_call_url'}}].
        request_id (str): Unique identifier of the request Example: 2T1p0e3j.
        status (int): HTTP status of the response Example: 408.
        type_ (ErrorResponseType): Machine-readable identifier for the general category of error Example:
            invalid_request_error.
        debug (ErrorDebug | Unset):  Example: {'message': 'Something broke: and something else: and something else',
            'stacktrace': ['thing.go:123']}.
        rate_limit (ErrorRateLimit | Unset):  Example: {'limit': 100, 'name': 'client_ip', 'remaining': 98,
            'retry_after': '2020-01-01T00:00:00Z'}.
    """

    errors: list[ErrorSingle]
    request_id: str
    status: int
    type_: ErrorResponseType
    debug: ErrorDebug | Unset = UNSET
    rate_limit: ErrorRateLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        request_id = self.request_id

        status = self.status

        type_ = self.type_.value

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "request_id": request_id,
                "status": status,
                "type": type_,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_debug import ErrorDebug
        from ..models.error_rate_limit import ErrorRateLimit
        from ..models.error_single import ErrorSingle

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = ErrorSingle.from_dict(errors_item_data)

            errors.append(errors_item)

        request_id = d.pop("request_id")

        status = d.pop("status")

        type_ = ErrorResponseType(d.pop("type"))

        _debug = d.pop("debug", UNSET)
        debug: ErrorDebug | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = ErrorDebug.from_dict(_debug)

        _rate_limit = d.pop("rate_limit", UNSET)
        rate_limit: ErrorRateLimit | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = ErrorRateLimit.from_dict(_rate_limit)

        error_response = cls(
            errors=errors,
            request_id=request_id,
            status=status,
            type_=type_,
            debug=debug,
            rate_limit=rate_limit,
        )

        error_response.additional_properties = d
        return error_response

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
