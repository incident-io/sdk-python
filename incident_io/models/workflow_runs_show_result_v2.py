from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_run_v2 import WorkflowRunV2


T = TypeVar("T", bound="WorkflowRunsShowResultV2")


@_attrs_define
class WorkflowRunsShowResultV2:
    """
    Example:
        {'workflow_run': {'cancelled_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z',
            'enqueued_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been
            notified.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_reference': 'INC-123', 'progress': [{'completed_at': '2021-08-17T13:28:57.801578Z', 'error':
            'Something went wrong and our engineers have been notified.', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_reference': 'INC-123', 'status': 'complete', 'step': 'slack.post_message', 'webhook_delivery':
            {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx',
            'request': {'body': '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}', 'body_truncated': False, 'headers':
            {'Content-Type': 'application/json'}}, 'response': {'body': '{"error":"unprocessable"}', 'body_truncated':
            False, 'headers': {'Content-Type': 'application/json'}}, 'status_code': 500}, 'webhook_delivery_state':
            'expired'}], 'scheduled_at': '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z',
            'workflow_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_name': 'Announce incident updates',
            'workflow_version_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_version_number': 3}}

    Attributes:
        workflow_run (WorkflowRunV2):  Example: {'cancelled_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'enqueued_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and
            our engineers have been notified.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'progress': [{'completed_at':
            '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been notified.',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'status': 'complete', 'step':
            'slack.post_message', 'webhook_delivery': {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident',
            'method': 'POST', 'outcome': 'non_2xx', 'request': {'body': '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}',
            'body_truncated': False, 'headers': {'Content-Type': 'application/json'}}, 'response': {'body':
            '{"error":"unprocessable"}', 'body_truncated': False, 'headers': {'Content-Type': 'application/json'}},
            'status_code': 500}, 'webhook_delivery_state': 'expired'}], 'scheduled_at': '2021-08-17T13:28:57.801578Z',
            'updated_at': '2021-08-17T13:28:57.801578Z', 'workflow_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_name':
            'Announce incident updates', 'workflow_version_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_version_number': 3}.
    """

    workflow_run: WorkflowRunV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_run = self.workflow_run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow_run": workflow_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_run_v2 import WorkflowRunV2

        d = dict(src_dict)
        workflow_run = WorkflowRunV2.from_dict(d.pop("workflow_run"))

        workflow_runs_show_result_v2 = cls(
            workflow_run=workflow_run,
        )

        workflow_runs_show_result_v2.additional_properties = d
        return workflow_runs_show_result_v2

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
