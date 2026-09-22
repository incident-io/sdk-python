from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_result_with_total_v2 import (
        PaginationMetaResultWithTotalV2,
    )
    from ..models.workflow_run_slim_v2 import WorkflowRunSlimV2


T = TypeVar("T", bound="WorkflowRunsListResultV2")


@_attrs_define(kw_only=True)
class WorkflowRunsListResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238},
            'workflow_runs': [{'cancelled_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z',
            'enqueued_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been
            notified.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_reference': 'INC-123', 'progress': [{'completed_at': '2021-08-17T13:28:57.801578Z', 'error':
            'Something went wrong and our engineers have been notified.', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_reference': 'INC-123', 'status': 'complete', 'step': 'slack.post_message', 'webhook_delivery':
            {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx',
            'status_code': 500}, 'webhook_delivery_state': 'expired'}], 'scheduled_at': '2021-08-17T13:28:57.801578Z',
            'updated_at': '2021-08-17T13:28:57.801578Z', 'workflow_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_name':
            'Announce incident updates', 'workflow_version_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_version_number':
            3}]}

    Attributes:
        workflow_runs (list[WorkflowRunSlimV2]):  Example: [{'cancelled_at': '2021-08-17T13:28:57.801578Z',
            'created_at': '2021-08-17T13:28:57.801578Z', 'enqueued_at': '2021-08-17T13:28:57.801578Z', 'error': 'Something
            went wrong and our engineers have been notified.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'progress': [{'completed_at':
            '2021-08-17T13:28:57.801578Z', 'error': 'Something went wrong and our engineers have been notified.',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_reference': 'INC-123', 'status': 'complete', 'step':
            'slack.post_message', 'webhook_delivery': {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident',
            'method': 'POST', 'outcome': 'non_2xx', 'status_code': 500}, 'webhook_delivery_state': 'expired'}],
            'scheduled_at': '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'workflow_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_name': 'Announce incident updates', 'workflow_version_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'workflow_version_number': 3}].
        pagination_meta (PaginationMetaResultWithTotalV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25, 'total_record_count': 238}.
    """

    workflow_runs: list[WorkflowRunSlimV2]
    pagination_meta: PaginationMetaResultWithTotalV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_runs = []
        for workflow_runs_item_data in self.workflow_runs:
            workflow_runs_item = workflow_runs_item_data.to_dict()
            workflow_runs.append(workflow_runs_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow_runs": workflow_runs,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_with_total_v2 import (
            PaginationMetaResultWithTotalV2,
        )
        from ..models.workflow_run_slim_v2 import WorkflowRunSlimV2

        d = dict(src_dict)
        workflow_runs = []
        _workflow_runs = d.pop("workflow_runs")
        for workflow_runs_item_data in _workflow_runs:
            workflow_runs_item = WorkflowRunSlimV2.from_dict(workflow_runs_item_data)

            workflow_runs.append(workflow_runs_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultWithTotalV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultWithTotalV2.from_dict(
                _pagination_meta
            )

        workflow_runs_list_result_v2 = cls(
            workflow_runs=workflow_runs,
            pagination_meta=pagination_meta,
        )

        workflow_runs_list_result_v2.additional_properties = d
        return workflow_runs_list_result_v2

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
