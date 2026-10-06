from enum import StrEnum


class IncidentFormLifecycleElementPayloadV3ElementType(StrEnum):
    ANNOUNCE_RETRO_INCIDENT = "announce_retro_incident"
    CUSTOM_FIELD = "custom_field"
    DIVIDER = "divider"
    ENTER_POST_INCIDENT_FLOW = "enter_post_incident_flow"
    INCIDENT_ATTACHMENTS = "incident_attachments"
    INCIDENT_ROLE = "incident_role"
    INCIDENT_TYPE = "incident_type"
    INVESTIGATION_FEEDBACK = "investigation_feedback"
    NAME = "name"
    NEXT_UPDATE_IN = "next_update_in"
    SEVERITY = "severity"
    SLACK_CHANNEL = "slack_channel"
    STATUS = "status"
    SUMMARY = "summary"
    TEXT = "text"
    TIMESTAMP = "timestamp"
    TRIAGE = "triage"
    UPDATE_MESSAGE = "update_message"
    VISIBILITY = "visibility"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(
        cls, value: object
    ) -> "IncidentFormLifecycleElementPayloadV3ElementType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
