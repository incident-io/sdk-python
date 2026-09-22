from enum import StrEnum


class EscalationPathTargetWithBindingPayloadV2ScheduleMode(StrEnum):
    ALL_USERS = "all_users"
    ALL_USERS_FOR_ROTA = "all_users_for_rota"
    CURRENTLY_ON_CALL = "currently_on_call"
    CURRENTLY_ON_CALL_FOR_ROTA = "currently_on_call_for_rota"
    NEXT_ON_CALL = "next_on_call"
    NEXT_ON_CALL_FOR_ROTA = "next_on_call_for_rota"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "EscalationPathTargetWithBindingPayloadV2ScheduleMode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
