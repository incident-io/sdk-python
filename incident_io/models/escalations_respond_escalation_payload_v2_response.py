from enum import StrEnum


class EscalationsRespondEscalationPayloadV2Response(StrEnum):
    ACK = "ack"
    NACK = "nack"
    SNOOZE = "snooze"

    def __str__(self) -> str:
        return str(self.value)
