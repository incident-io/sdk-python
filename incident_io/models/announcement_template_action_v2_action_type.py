from enum import StrEnum


class AnnouncementTemplateActionV2ActionType(StrEnum):
    ANNOUNCEMENT_POST_ACTIONS_CREATE_CHANNEL = (
        "announcement_post_actions_create_channel"
    )
    ANNOUNCEMENT_POST_ACTIONS_ESCALATE = "announcement_post_actions_escalate"
    ANNOUNCEMENT_POST_ACTIONS_HOMEPAGE = "announcement_post_actions_homepage"
    ANNOUNCEMENT_POST_ACTIONS_INTERNAL_STATUS_PAGE = (
        "announcement_post_actions_internal_status_page"
    )
    ANNOUNCEMENT_POST_ACTIONS_JIRA_TICKET = "announcement_post_actions_jira_ticket"
    ANNOUNCEMENT_POST_ACTIONS_JOIN_CALL = "announcement_post_actions_join_call"
    ANNOUNCEMENT_POST_ACTIONS_POSTMORTEM = "announcement_post_actions_postmortem"
    ANNOUNCEMENT_POST_ACTIONS_PUBLIC_STATUS_PAGE = (
        "announcement_post_actions_public_status_page"
    )
    ANNOUNCEMENT_POST_ACTIONS_REQUEST_ACCESS = (
        "announcement_post_actions_request_access"
    )
    ANNOUNCEMENT_POST_ACTIONS_SHARE_UPDATE = "announcement_post_actions_share_update"
    ANNOUNCEMENT_POST_ACTIONS_SUBSCRIBE = "announcement_post_actions_subscribe"
    ANNOUNCEMENT_POST_ACTIONS_TRIAGE = "announcement_post_actions_triage"
    ANNOUNCEMENT_POST_ACTIONS_UPDATE_STATUS = "announcement_post_actions_update_status"
    ANNOUNCEMENT_POST_ACTIONS_VIEW_ALERT = "announcement_post_actions_view_alert"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AnnouncementTemplateActionV2ActionType":
        """Accept a value added to the API after this SDK was built."""
        if not isinstance(value, str):
            return super()._missing_(value)  # type: ignore[return-value]
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
