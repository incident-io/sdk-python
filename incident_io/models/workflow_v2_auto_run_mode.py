from enum import StrEnum


class WorkflowV2AutoRunMode(StrEnum):
    CONFIRM_BEFORE_RUNNING = "confirm_before_running"
    RUN_AUTOMATICALLY = "run_automatically"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "WorkflowV2AutoRunMode":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
