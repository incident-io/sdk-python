from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_progress_slim_v2 import StepProgressSlimV2


T = TypeVar("T", bound="WorkflowRunSlimV2")


@_attrs_define
class WorkflowRunSlimV2:
    """
    Example:
        {'cancelled_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'enqueued_at':
            '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been notified.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123',
            'progress': [{'completed_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers
            have been notified.', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'status':
            'complete', 'step': 'slack.post_message', 'webhook_delivery': {'duration_ms': 412, 'endpoint':
            'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx', 'status_code': 500},
            'webhook_delivery_state': 'expired'}], 'scheduled_at': '2021-08-17T13:28:57.801578Z', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'workflow_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_name': 'Announce incident
            updates', 'workflow_version_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_version_number': 3}

    Attributes:
        created_at (datetime.datetime): When the resource was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier for the workflow run Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        progress (list[StepProgressSlimV2]): Status of each step as it is worked Example: [{'completed_at':
            '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been notified.',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'status': 'complete', 'step':
            'slack.post_message', 'webhook_delivery': {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident',
            'method': 'POST', 'outcome': 'non_2xx', 'status_code': 500}, 'webhook_delivery_state': 'expired'}].
        scheduled_at (datetime.datetime): When the run was scheduled for Example: 2021-08-17T13:28:57.801578Z.
        updated_at (datetime.datetime): When the resource was last updated Example: 2021-08-17T13:28:57.801578Z.
        workflow_id (str): Unique identifier for the underlying workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        workflow_version_id (str): Unique identifier of the workflow version Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        workflow_version_number (int): Monotonically incrementing version number for the version that ran Example: 3.
        cancelled_at (datetime.datetime | Unset): If the run was cancelled, this is when Example:
            2021-08-17T13:28:57.801578Z.
        enqueued_at (datetime.datetime | Unset): When the run was enqueued for execution Example:
            2021-08-17T13:28:57.801578Z.
        error (str | Unset): Error produced by the workflow, if it failed Example: Something went wrong and our
            engineers have been notified..
        incident_id (str | Unset): If this run was against a specific incident, this is the ID of that incident Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        incident_reference (str | Unset): If this run was against a specific incident, this is the reference of that
            incident Example: INC-123.
        workflow_name (str | Unset): Name of the underlying workflow Example: Announce incident updates.
    """

    created_at: datetime.datetime
    id: str
    progress: list[StepProgressSlimV2]
    scheduled_at: datetime.datetime
    updated_at: datetime.datetime
    workflow_id: str
    workflow_version_id: str
    workflow_version_number: int
    cancelled_at: datetime.datetime | Unset = UNSET
    enqueued_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    incident_id: str | Unset = UNSET
    incident_reference: str | Unset = UNSET
    workflow_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        progress = []
        for progress_item_data in self.progress:
            progress_item = progress_item_data.to_dict()
            progress.append(progress_item)

        scheduled_at = self.scheduled_at.isoformat()

        updated_at = self.updated_at.isoformat()

        workflow_id = self.workflow_id

        workflow_version_id = self.workflow_version_id

        workflow_version_number = self.workflow_version_number

        cancelled_at: str | Unset = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat()

        enqueued_at: str | Unset = UNSET
        if not isinstance(self.enqueued_at, Unset):
            enqueued_at = self.enqueued_at.isoformat()

        error = self.error

        incident_id = self.incident_id

        incident_reference = self.incident_reference

        workflow_name = self.workflow_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "progress": progress,
                "scheduled_at": scheduled_at,
                "updated_at": updated_at,
                "workflow_id": workflow_id,
                "workflow_version_id": workflow_version_id,
                "workflow_version_number": workflow_version_number,
            }
        )
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if enqueued_at is not UNSET:
            field_dict["enqueued_at"] = enqueued_at
        if error is not UNSET:
            field_dict["error"] = error
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if incident_reference is not UNSET:
            field_dict["incident_reference"] = incident_reference
        if workflow_name is not UNSET:
            field_dict["workflow_name"] = workflow_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.step_progress_slim_v2 import StepProgressSlimV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        progress = []
        _progress = d.pop("progress")
        for progress_item_data in _progress:
            progress_item = StepProgressSlimV2.from_dict(progress_item_data)

            progress.append(progress_item)

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        workflow_id = d.pop("workflow_id")

        workflow_version_id = d.pop("workflow_version_id")

        workflow_version_number = d.pop("workflow_version_number")

        _cancelled_at = d.pop("cancelled_at", UNSET)
        cancelled_at: datetime.datetime | Unset
        if isinstance(_cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = datetime.datetime.fromisoformat(_cancelled_at)

        _enqueued_at = d.pop("enqueued_at", UNSET)
        enqueued_at: datetime.datetime | Unset
        if isinstance(_enqueued_at, Unset):
            enqueued_at = UNSET
        else:
            enqueued_at = datetime.datetime.fromisoformat(_enqueued_at)

        error = d.pop("error", UNSET)

        incident_id = d.pop("incident_id", UNSET)

        incident_reference = d.pop("incident_reference", UNSET)

        workflow_name = d.pop("workflow_name", UNSET)

        workflow_run_slim_v2 = cls(
            created_at=created_at,
            id=id,
            progress=progress,
            scheduled_at=scheduled_at,
            updated_at=updated_at,
            workflow_id=workflow_id,
            workflow_version_id=workflow_version_id,
            workflow_version_number=workflow_version_number,
            cancelled_at=cancelled_at,
            enqueued_at=enqueued_at,
            error=error,
            incident_id=incident_id,
            incident_reference=incident_reference,
            workflow_name=workflow_name,
        )

        workflow_run_slim_v2.additional_properties = d
        return workflow_run_slim_v2

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
