from enum import StrEnum


class WebhooksPrivateIncidentFollowUpUpdatedV1ResponseBodyEventType(StrEnum):
    PRIVATE_ALERT_ALERT_CREATED_V1 = "private_alert.alert_created_v1"
    PRIVATE_ALERT_ALERT_RESOLVED_V1 = "private_alert.alert_resolved_v1"
    PRIVATE_ESCALATION_ESCALATION_CREATED_V1 = (
        "private_escalation.escalation_created_v1"
    )
    PRIVATE_ESCALATION_ESCALATION_STATUS_UPDATED_V1 = (
        "private_escalation.escalation_status_updated_v1"
    )
    PRIVATE_INCIDENT_ACTION_CREATED_V1 = "private_incident.action_created_v1"
    PRIVATE_INCIDENT_ACTION_UPDATED_V1 = "private_incident.action_updated_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_CREATED_V1 = "private_incident.follow_up_created_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_CREATED_V2 = "private_incident.follow_up_created_v2"
    PRIVATE_INCIDENT_FOLLOW_UP_UPDATED_V1 = "private_incident.follow_up_updated_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_UPDATED_V2 = "private_incident.follow_up_updated_v2"
    PRIVATE_INCIDENT_INCIDENT_CREATED_V2 = "private_incident.incident_created_v2"
    PRIVATE_INCIDENT_INCIDENT_UPDATED_V2 = "private_incident.incident_updated_v2"
    PRIVATE_INCIDENT_MEMBERSHIP_GRANTED_V1 = "private_incident.membership_granted_v1"
    PRIVATE_INCIDENT_MEMBERSHIP_REVOKED_V1 = "private_incident.membership_revoked_v1"
    PRIVATE_INCIDENT_POSTMORTEM_DOCUMENT_STATUS_UPDATED_V1 = (
        "private_incident.postmortem_document_status_updated_v1"
    )
    PUBLIC_ALERT_ALERT_CREATED_V1 = "public_alert.alert_created_v1"
    PUBLIC_ALERT_ALERT_RESOLVED_V1 = "public_alert.alert_resolved_v1"
    PUBLIC_ESCALATION_ESCALATION_CREATED_V1 = "public_escalation.escalation_created_v1"
    PUBLIC_ESCALATION_ESCALATION_STATUS_UPDATED_V1 = (
        "public_escalation.escalation_status_updated_v1"
    )
    PUBLIC_INCIDENT_ACTION_CREATED_V1 = "public_incident.action_created_v1"
    PUBLIC_INCIDENT_ACTION_UPDATED_V1 = "public_incident.action_updated_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_CREATED_V1 = "public_incident.follow_up_created_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_CREATED_V2 = "public_incident.follow_up_created_v2"
    PUBLIC_INCIDENT_FOLLOW_UP_UPDATED_V1 = "public_incident.follow_up_updated_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_UPDATED_V2 = "public_incident.follow_up_updated_v2"
    PUBLIC_INCIDENT_INCIDENT_CREATED_V2 = "public_incident.incident_created_v2"
    PUBLIC_INCIDENT_INCIDENT_STATUS_UPDATED_V2 = (
        "public_incident.incident_status_updated_v2"
    )
    PUBLIC_INCIDENT_INCIDENT_UPDATED_V2 = "public_incident.incident_updated_v2"
    PUBLIC_INCIDENT_POSTMORTEM_DOCUMENT_STATUS_UPDATED_V1 = (
        "public_incident.postmortem_document_status_updated_v1"
    )
    SCHEDULE_CREATED_V1 = "schedule.created_v1"
    SCHEDULE_DELETED_V1 = "schedule.deleted_v1"
    SCHEDULE_SHIFT_CHANGE_V1 = "schedule.shift_change_v1"
    SCHEDULE_UPDATED_V1 = "schedule.updated_v1"
    STATUS_PAGE_INCIDENT_UPDATE_SHARED_V1 = "status_page_incident.update_shared_v1"

    def __str__(self) -> str:
        return str(self.value)
