from enum import StrEnum


class ErrorResponseType(StrEnum):
    API_ERROR = "api_error"
    AUTHENTICATION_ERROR = "authentication_error"
    CLIENT_TIMEOUT = "client_timeout"
    CONFLICT = "conflict"
    INVALID_REQUEST_ERROR = "invalid_request_error"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    NOT_ACCEPTABLE = "not_acceptable"
    NOT_FOUND = "not_found"
    PAYLOAD_TOO_LARGE = "payload_too_large"
    PRECONDITION_FAILED = "precondition_failed"
    RATE_LIMIT_REACHED = "rate_limit_reached"
    REQUEST_TIMEOUT = "request_timeout"
    RESOURCE_FORBIDDEN = "resource_forbidden"
    TOO_MANY_REQUESTS = "too_many_requests"
    VALIDATION_ERROR = "validation_error"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "ErrorResponseType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
