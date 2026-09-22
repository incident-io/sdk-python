from enum import StrEnum


class WorkflowsCreateWorkflowPayloadV2RunsOnIncidents(StrEnum):
    NEWLY_CREATED = "newly_created"
    NEWLY_CREATED_AND_ACTIVE = "newly_created_and_active"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "WorkflowsCreateWorkflowPayloadV2RunsOnIncidents":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
