from enum import StrEnum


class IncidentFormLifecycleElementV3RequiredIf(StrEnum):
    ALWAYS_REQUIRE = "always_require"
    CHECK_ENGINE_CONFIG = "check_engine_config"
    NEVER_REQUIRE = "never_require"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "IncidentFormLifecycleElementV3RequiredIf":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
