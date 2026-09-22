from enum import StrEnum


class WebhookDeliveryV2Outcome(StrEnum):
    NETWORK_ERROR = "network_error"
    NON_2XX = "non_2xx"
    SUCCESS = "success"
    TIMEOUT = "timeout"
    TLS_ERROR = "tls_error"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "WebhookDeliveryV2Outcome":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
