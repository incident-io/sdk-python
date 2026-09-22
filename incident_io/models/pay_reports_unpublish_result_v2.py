from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pay_report_v2 import PayReportV2


T = TypeVar("T", bound="PayReportsUnpublishResultV2")


@_attrs_define(kw_only=True)
class PayReportsUnpublishResultV2:
    """
    Example:
        {'pay_report': {'created_at': '2026-04-01T09:00:00Z', 'creator': {'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}}, 'end_date': '2026-03-31', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'March 2026', 'overlapping_shifts': 'paid_per_schedule', 'published_at':
            '2026-04-01T09:00:00Z', 'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'], 'start_date': '2026-03-01', 'status':
            'complete', 'total_duration_seconds': 3600, 'total_pay_by_currency': {'GBP': 2400}, 'unpaid_shifts': 'included',
            'updated_at': '2026-04-01T09:00:00Z'}}

    Attributes:
        pay_report (PayReportV2): A pay report values the time a set of users spent on-call over a date window, using
            the rates from a pay config.

            This is a summary: the headline totals, and the parameters the report was generated
            with. The shifts behind those totals, and the per-user and per-schedule breakdowns, come
            from downloading the report as CSV.

            Reports are immutable snapshots: once generated, changing the pay config or the
            schedules behind it will not change the report. Generate a new one instead.

            A report starts as a draft and becomes visible to everyone in your organisation when
            you publish it.

            Reports are generated in the background, so a report you have just asked for has no
            totals yet. Its status says whether they are still coming, and a report that failed
            carries the reason it will never have them. Example: {'created_at': '2026-04-01T09:00:00Z', 'creator': {'alert':
            {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'end_date': '2026-03-31',
            'error_code': 'invalid_request', 'error_message': "Schedule 'Primary Support' has no pay config to price its
            shifts with", 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'March 2026', 'overlapping_shifts':
            'paid_per_schedule', 'published_at': '2026-04-01T09:00:00Z', 'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'],
            'start_date': '2026-03-01', 'status': 'complete', 'total_duration_seconds': 3600, 'total_pay_by_currency':
            {'GBP': 2400}, 'unpaid_shifts': 'included', 'updated_at': '2026-04-01T09:00:00Z'}.
    """

    pay_report: PayReportV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pay_report = self.pay_report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pay_report": pay_report,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_report_v2 import PayReportV2

        d = dict(src_dict)
        pay_report = PayReportV2.from_dict(d.pop("pay_report"))

        pay_reports_unpublish_result_v2 = cls(
            pay_report=pay_report,
        )

        pay_reports_unpublish_result_v2.additional_properties = d
        return pay_reports_unpublish_result_v2

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
