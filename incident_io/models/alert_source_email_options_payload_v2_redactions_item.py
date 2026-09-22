from enum import StrEnum


class AlertSourceEmailOptionsPayloadV2RedactionsItem(StrEnum):
    CREDIT_CARD_NUMBERS = "credit_card_numbers"
    PHONE_NUMBERS = "phone_numbers"
    US_SOCIAL_SECURITY_NUMBERS = "us_social_security_numbers"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "AlertSourceEmailOptionsPayloadV2RedactionsItem":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
