from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_reports_create_payload_v2_overlapping_shifts import (
    PayReportsCreatePayloadV2OverlappingShifts,
)
from ..models.pay_reports_create_payload_v2_unpaid_shifts import (
    PayReportsCreatePayloadV2UnpaidShifts,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_payload_v2 import ExpressionPayloadV2
    from ..models.pay_report_rotation_filter_v2 import PayReportRotationFilterV2


T = TypeVar("T", bound="PayReportsCreatePayloadV2")


@_attrs_define(kw_only=True)
class PayReportsCreatePayloadV2:
    """
    Example:
        {'end_date': '2026-03-31', 'name': 'March 2026', 'overlapping_shifts': 'paid_per_schedule',
            'pay_config_expression': {'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns':
            {'array': True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'},
            'pay_config_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rotation_filters': [{'rotation_ids': ['primary'], 'schedule_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}], 'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'], 'start_date': '2026-03-01',
            'unpaid_shifts': 'excluded'}

    Attributes:
        end_date (str): Last date (YYYY-MM-DD) to include shifts from, inclusive Example: 2026-03-31.
        name (str): Human readable name for this report Example: March 2026.
        schedule_ids (list[str]): Which schedules to report on Example: ['01FCNDV6P870EA6S7TK1DSYDG0'].
        start_date (str): First date (YYYY-MM-DD) to include shifts from, inclusive Example: 2026-03-01.
        overlapping_shifts (PayReportsCreatePayloadV2OverlappingShifts | Unset): Time on more than one of these
            schedules at once can be paid once or per schedule. Paying it once requires the advanced on-call plan. Example:
            paid_per_schedule.
        pay_config_expression (ExpressionPayloadV2 | Unset):  Example: {'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'concatenate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}.
        pay_config_id (str | Unset): The pay config to price every shift with. Provide this or pay_config_expression,
            and not both. Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        rotation_filters (list[PayReportRotationFilterV2] | Unset): Narrows some of these schedules to a subset of their
            rotations. A schedule that does not appear here includes every rotation. Example: [{'rotation_ids': ['primary'],
            'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}].
        unpaid_shifts (PayReportsCreatePayloadV2UnpaidShifts | Unset): Whether shifts that price to zero count towards
            total_duration_seconds Example: excluded.
    """

    end_date: str
    name: str
    schedule_ids: list[str]
    start_date: str
    overlapping_shifts: PayReportsCreatePayloadV2OverlappingShifts | Unset = UNSET
    pay_config_expression: ExpressionPayloadV2 | Unset = UNSET
    pay_config_id: str | Unset = UNSET
    rotation_filters: list[PayReportRotationFilterV2] | Unset = UNSET
    unpaid_shifts: PayReportsCreatePayloadV2UnpaidShifts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        name = self.name

        schedule_ids = self.schedule_ids

        start_date = self.start_date

        overlapping_shifts: str | Unset = UNSET
        if not isinstance(self.overlapping_shifts, Unset):
            overlapping_shifts = self.overlapping_shifts.value

        pay_config_expression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pay_config_expression, Unset):
            pay_config_expression = self.pay_config_expression.to_dict()

        pay_config_id = self.pay_config_id

        rotation_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rotation_filters, Unset):
            rotation_filters = []
            for rotation_filters_item_data in self.rotation_filters:
                rotation_filters_item = rotation_filters_item_data.to_dict()
                rotation_filters.append(rotation_filters_item)

        unpaid_shifts: str | Unset = UNSET
        if not isinstance(self.unpaid_shifts, Unset):
            unpaid_shifts = self.unpaid_shifts.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_date": end_date,
                "name": name,
                "schedule_ids": schedule_ids,
                "start_date": start_date,
            }
        )
        if overlapping_shifts is not UNSET:
            field_dict["overlapping_shifts"] = overlapping_shifts
        if pay_config_expression is not UNSET:
            field_dict["pay_config_expression"] = pay_config_expression
        if pay_config_id is not UNSET:
            field_dict["pay_config_id"] = pay_config_id
        if rotation_filters is not UNSET:
            field_dict["rotation_filters"] = rotation_filters
        if unpaid_shifts is not UNSET:
            field_dict["unpaid_shifts"] = unpaid_shifts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.expression_payload_v2 import ExpressionPayloadV2
        from ..models.pay_report_rotation_filter_v2 import (
            PayReportRotationFilterV2,
        )

        d = dict(src_dict)
        end_date = d.pop("end_date")

        name = d.pop("name")

        schedule_ids = cast(list[str], d.pop("schedule_ids"))

        start_date = d.pop("start_date")

        _overlapping_shifts = d.pop("overlapping_shifts", UNSET)
        overlapping_shifts: PayReportsCreatePayloadV2OverlappingShifts | Unset
        if isinstance(_overlapping_shifts, Unset):
            overlapping_shifts = UNSET
        else:
            overlapping_shifts = PayReportsCreatePayloadV2OverlappingShifts(
                _overlapping_shifts
            )

        _pay_config_expression = d.pop("pay_config_expression", UNSET)
        pay_config_expression: ExpressionPayloadV2 | Unset
        if isinstance(_pay_config_expression, Unset):
            pay_config_expression = UNSET
        else:
            pay_config_expression = ExpressionPayloadV2.from_dict(
                _pay_config_expression
            )

        pay_config_id = d.pop("pay_config_id", UNSET)

        _rotation_filters = d.pop("rotation_filters", UNSET)
        rotation_filters: list[PayReportRotationFilterV2] | Unset = UNSET
        if _rotation_filters is not UNSET:
            rotation_filters = []
            for rotation_filters_item_data in _rotation_filters:
                rotation_filters_item = PayReportRotationFilterV2.from_dict(
                    rotation_filters_item_data
                )

                rotation_filters.append(rotation_filters_item)

        _unpaid_shifts = d.pop("unpaid_shifts", UNSET)
        unpaid_shifts: PayReportsCreatePayloadV2UnpaidShifts | Unset
        if isinstance(_unpaid_shifts, Unset):
            unpaid_shifts = UNSET
        else:
            unpaid_shifts = PayReportsCreatePayloadV2UnpaidShifts(_unpaid_shifts)

        pay_reports_create_payload_v2 = cls(
            end_date=end_date,
            name=name,
            schedule_ids=schedule_ids,
            start_date=start_date,
            overlapping_shifts=overlapping_shifts,
            pay_config_expression=pay_config_expression,
            pay_config_id=pay_config_id,
            rotation_filters=rotation_filters,
            unpaid_shifts=unpaid_shifts,
        )

        pay_reports_create_payload_v2.additional_properties = d
        return pay_reports_create_payload_v2

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
