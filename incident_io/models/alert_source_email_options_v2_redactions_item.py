from enum import StrEnum


class AlertSourceEmailOptionsV2RedactionsItem(StrEnum):
    CREDIT_CARD_NUMBERS = "credit_card_numbers"
    PHONE_NUMBERS = "phone_numbers"
    US_SOCIAL_SECURITY_NUMBERS = "us_social_security_numbers"

    def __str__(self) -> str:
        return str(self.value)
