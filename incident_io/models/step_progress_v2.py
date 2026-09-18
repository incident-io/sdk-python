from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_progress_v2_status import StepProgressV2Status
from ..models.step_progress_v2_webhook_delivery_state import (
    StepProgressV2WebhookDeliveryState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_delivery_v2 import WebhookDeliveryV2


T = TypeVar("T", bound="StepProgressV2")


@_attrs_define
class StepProgressV2:
    """
    Example:
        {'completed_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been
            notified.', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'status': 'complete',
            'step': 'slack.post_message', 'webhook_delivery': {'duration_ms': 412, 'endpoint':
            'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx', 'request': {'body':
            '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}', 'body_truncated': False, 'headers': {'Content-Type':
            'application/json'}}, 'response': {'body': '{"error":"unprocessable"}', 'body_truncated': False, 'headers':
            {'Content-Type': 'application/json'}}, 'status_code': 500}, 'webhook_delivery_state': 'expired'}

    Attributes:
        status (StepProgressV2Status): Status of the step Example: complete.
        step (str): Name of the step Example: slack.post_message.
        completed_at (datetime.datetime | Unset): Status of the step Example: 2021-08-17T13:28:57.801578Z.
        error (str | Unset): The cause of an errored step Example: Something went wrong and our engineers have been
            notified..
        incident_id (str | Unset): If this step ran for a specific incident (e.g. in a loop), the incident ID Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_reference (str | Unset): If this step ran for a specific incident (e.g. in a loop), the incident
            reference Example: INC-123.
        webhook_delivery (WebhookDeliveryV2 | Unset):  Example: {'duration_ms': 412, 'endpoint':
            'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx', 'request': {'body':
            '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}', 'body_truncated': False, 'headers': {'Content-Type':
            'application/json'}}, 'response': {'body': '{"error":"unprocessable"}', 'body_truncated': False, 'headers':
            {'Content-Type': 'application/json'}}, 'status_code': 500}.
        webhook_delivery_state (StepProgressV2WebhookDeliveryState | Unset): Whether this step's delivery can be shown,
            for a webhook.send step. Absent for all other step types Example: expired.
    """

    status: StepProgressV2Status
    step: str
    completed_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    incident_id: str | Unset = UNSET
    incident_reference: str | Unset = UNSET
    webhook_delivery: WebhookDeliveryV2 | Unset = UNSET
    webhook_delivery_state: StepProgressV2WebhookDeliveryState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        step = self.step

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        error = self.error

        incident_id = self.incident_id

        incident_reference = self.incident_reference

        webhook_delivery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_delivery, Unset):
            webhook_delivery = self.webhook_delivery.to_dict()

        webhook_delivery_state: str | Unset = UNSET
        if not isinstance(self.webhook_delivery_state, Unset):
            webhook_delivery_state = self.webhook_delivery_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "step": step,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if error is not UNSET:
            field_dict["error"] = error
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if incident_reference is not UNSET:
            field_dict["incident_reference"] = incident_reference
        if webhook_delivery is not UNSET:
            field_dict["webhook_delivery"] = webhook_delivery
        if webhook_delivery_state is not UNSET:
            field_dict["webhook_delivery_state"] = webhook_delivery_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_delivery_v2 import WebhookDeliveryV2

        d = dict(src_dict)
        status = StepProgressV2Status(d.pop("status"))

        step = d.pop("step")

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        error = d.pop("error", UNSET)

        incident_id = d.pop("incident_id", UNSET)

        incident_reference = d.pop("incident_reference", UNSET)

        _webhook_delivery = d.pop("webhook_delivery", UNSET)
        webhook_delivery: WebhookDeliveryV2 | Unset
        if isinstance(_webhook_delivery, Unset):
            webhook_delivery = UNSET
        else:
            webhook_delivery = WebhookDeliveryV2.from_dict(_webhook_delivery)

        _webhook_delivery_state = d.pop("webhook_delivery_state", UNSET)
        webhook_delivery_state: StepProgressV2WebhookDeliveryState | Unset
        if isinstance(_webhook_delivery_state, Unset):
            webhook_delivery_state = UNSET
        else:
            webhook_delivery_state = StepProgressV2WebhookDeliveryState(
                _webhook_delivery_state
            )

        step_progress_v2 = cls(
            status=status,
            step=step,
            completed_at=completed_at,
            error=error,
            incident_id=incident_id,
            incident_reference=incident_reference,
            webhook_delivery=webhook_delivery,
            webhook_delivery_state=webhook_delivery_state,
        )

        step_progress_v2.additional_properties = d
        return step_progress_v2

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
