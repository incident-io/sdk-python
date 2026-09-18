from enum import StrEnum


class EscalationUserResponseOptionsV2AvailableActionsItem(StrEnum):
    ACK = "ack"
    NACK = "nack"
    SNOOZE = "snooze"

    def __str__(self) -> str:
        return str(self.value)
