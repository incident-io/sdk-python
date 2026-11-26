from enum import StrEnum


class AlertRuleActionV3Type(StrEnum):
    CREATE_INCIDENT = "create_incident"
    ESCALATE = "escalate"
    INVESTIGATE = "investigate"
    POST_MICROSOFT_TEAMS = "post_microsoft_teams"
    POST_SLACK = "post_slack"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AlertRuleActionV3Type":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
