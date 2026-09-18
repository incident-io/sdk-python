from enum import StrEnum


class WebhookDeliverySlimV2Outcome(StrEnum):
    NETWORK_ERROR = "network_error"
    NON_2XX = "non_2xx"
    SUCCESS = "success"
    TIMEOUT = "timeout"
    TLS_ERROR = "tls_error"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
