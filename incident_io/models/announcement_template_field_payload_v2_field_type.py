from enum import StrEnum


class AnnouncementTemplateFieldPayloadV2FieldType(StrEnum):
    ANNOUNCEMENT_POST_FIELDS_CREATOR = "announcement_post_fields_creator"
    ANNOUNCEMENT_POST_FIELDS_CUSTOM_FIELD = "announcement_post_fields_custom_field"
    ANNOUNCEMENT_POST_FIELDS_DESCRIPTION = "announcement_post_fields_description"
    ANNOUNCEMENT_POST_FIELDS_INCIDENT_TYPE = "announcement_post_fields_incident_type"
    ANNOUNCEMENT_POST_FIELDS_RICH_TEXT = "announcement_post_fields_rich_text"
    ANNOUNCEMENT_POST_FIELDS_ROLE = "announcement_post_fields_role"
    ANNOUNCEMENT_POST_FIELDS_SEVERITY = "announcement_post_fields_severity"
    ANNOUNCEMENT_POST_FIELDS_SLACK = "announcement_post_fields_slack"
    ANNOUNCEMENT_POST_FIELDS_STATUS = "announcement_post_fields_status"
    ANNOUNCEMENT_POST_FIELDS_TIMESTAMP = "announcement_post_fields_timestamp"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AnnouncementTemplateFieldPayloadV2FieldType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
