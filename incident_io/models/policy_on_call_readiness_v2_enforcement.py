from enum import StrEnum


class PolicyOnCallReadinessV2Enforcement(StrEnum):
    ADVISORY = "advisory"
    BLOCKING = "blocking"

    def __str__(self) -> str:
        return str(self.value)
