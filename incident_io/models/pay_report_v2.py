from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_report_v2_error_code import PayReportV2ErrorCode
from ..models.pay_report_v2_overlapping_shifts import PayReportV2OverlappingShifts
from ..models.pay_report_v2_status import PayReportV2Status
from ..models.pay_report_v2_unpaid_shifts import PayReportV2UnpaidShifts
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.pay_report_v2_total_pay_by_currency import (
        PayReportV2TotalPayByCurrency,
    )


T = TypeVar("T", bound="PayReportV2")


@_attrs_define
class PayReportV2:
    """A pay report values the time a set of users spent on-call over a date window, using the rates from a pay config.

    This is a summary: the headline totals, and the parameters the report was generated
    with. The shifts behind those totals, and the per-user and per-schedule breakdowns, come
    from downloading the report as CSV.

    Reports are immutable snapshots: once generated, changing the pay config or the
    schedules behind it will not change the report. Generate a new one instead.

    A report starts as a draft and becomes visible to everyone in your organisation when
    you publish it.

    Reports are generated in the background, so a report you have just asked for has no
    totals yet. Its status says whether they are still coming, and a report that failed
    carries the reason it will never have them.

        Example:
            {'created_at': '2026-04-01T09:00:00Z', 'creator': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}, 'end_date': '2026-03-31', 'error_code': 'invalid_request', 'error_message':
                "Schedule 'Primary Support' has no pay config to price its shifts with", 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
                'name': 'March 2026', 'overlapping_shifts': 'paid_per_schedule', 'published_at': '2026-04-01T09:00:00Z',
                'schedule_ids': ['01FCNDV6P870EA6S7TK1DSYDG0'], 'start_date': '2026-03-01', 'status': 'complete',
                'total_duration_seconds': 3600, 'total_pay_by_currency': {'GBP': 2400}, 'unpaid_shifts': 'included',
                'updated_at': '2026-04-01T09:00:00Z'}

        Attributes:
            created_at (datetime.datetime): When this report was created Example: 2026-04-01T09:00:00Z.
            end_date (str): Last date (YYYY-MM-DD) this report includes shifts from, inclusive Example: 2026-03-31.
            id (str): Unique identifier for this pay report Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
            name (str): Human readable name for this report Example: March 2026.
            overlapping_shifts (PayReportV2OverlappingShifts): How time spent on more than one schedule at once was paid
                Example: paid_per_schedule.
            schedule_ids (list[str]): The schedules this report covers Example: ['01FCNDV6P870EA6S7TK1DSYDG0'].
            start_date (str): First date (YYYY-MM-DD) this report includes shifts from, inclusive Example: 2026-03-01.
            status (PayReportV2Status): How far a report has got through being generated Example: generating.
            unpaid_shifts (PayReportV2UnpaidShifts): Whether shifts that priced to zero are part of the report Example:
                excluded.
            updated_at (datetime.datetime): When this report was last updated Example: 2026-04-01T09:00:00Z.
            creator (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
                test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
                Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
                'name': 'My little workflow'}}.
            error_code (PayReportV2ErrorCode | Unset): Why a report could not be generated Example: timed_out.
            error_message (str | Unset): What went wrong, written for whoever asked for the report. Only set on a failed
                report. Example: Schedule 'Primary Support' has no pay config to price its shifts with.
            published_at (datetime.datetime | Unset): When this report was published. Unset while the report is still a
                draft. Example: 2026-04-01T09:00:00Z.
            total_duration_seconds (int | Unset): Total time spent on-call across every shift in this report, in seconds.
                Unset until the report is complete, and for a legacy report, which we do not summarise. Example: 3600.
            total_pay_by_currency (PayReportV2TotalPayByCurrency | Unset): Total owed for this report, keyed by ISO 4217
                currency code, in the lowest denomination of that currency. Reports spanning pay configs with different
                currencies have an entry per currency, and those totals must not be summed. Unset until the report is complete,
                and for a legacy report, which we do not summarise. Example: {'GBP': 2400}.
    """

    created_at: datetime.datetime
    end_date: str
    id: str
    name: str
    overlapping_shifts: PayReportV2OverlappingShifts
    schedule_ids: list[str]
    start_date: str
    status: PayReportV2Status
    unpaid_shifts: PayReportV2UnpaidShifts
    updated_at: datetime.datetime
    creator: ActorV2 | Unset = UNSET
    error_code: PayReportV2ErrorCode | Unset = UNSET
    error_message: str | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    total_duration_seconds: int | Unset = UNSET
    total_pay_by_currency: PayReportV2TotalPayByCurrency | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        end_date = self.end_date

        id = self.id

        name = self.name

        overlapping_shifts = self.overlapping_shifts.value

        schedule_ids = self.schedule_ids

        start_date = self.start_date

        status = self.status.value

        unpaid_shifts = self.unpaid_shifts.value

        updated_at = self.updated_at.isoformat()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        error_message = self.error_message

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        total_duration_seconds = self.total_duration_seconds

        total_pay_by_currency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_pay_by_currency, Unset):
            total_pay_by_currency = self.total_pay_by_currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "end_date": end_date,
                "id": id,
                "name": name,
                "overlapping_shifts": overlapping_shifts,
                "schedule_ids": schedule_ids,
                "start_date": start_date,
                "status": status,
                "unpaid_shifts": unpaid_shifts,
                "updated_at": updated_at,
            }
        )
        if creator is not UNSET:
            field_dict["creator"] = creator
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if total_duration_seconds is not UNSET:
            field_dict["total_duration_seconds"] = total_duration_seconds
        if total_pay_by_currency is not UNSET:
            field_dict["total_pay_by_currency"] = total_pay_by_currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.pay_report_v2_total_pay_by_currency import (
            PayReportV2TotalPayByCurrency,
        )

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        end_date = d.pop("end_date")

        id = d.pop("id")

        name = d.pop("name")

        overlapping_shifts = PayReportV2OverlappingShifts(d.pop("overlapping_shifts"))

        schedule_ids = cast(list[str], d.pop("schedule_ids"))

        start_date = d.pop("start_date")

        status = PayReportV2Status(d.pop("status"))

        unpaid_shifts = PayReportV2UnpaidShifts(d.pop("unpaid_shifts"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _creator = d.pop("creator", UNSET)
        creator: ActorV2 | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ActorV2.from_dict(_creator)

        _error_code = d.pop("error_code", UNSET)
        error_code: PayReportV2ErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = PayReportV2ErrorCode(_error_code)

        error_message = d.pop("error_message", UNSET)

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        total_duration_seconds = d.pop("total_duration_seconds", UNSET)

        _total_pay_by_currency = d.pop("total_pay_by_currency", UNSET)
        total_pay_by_currency: PayReportV2TotalPayByCurrency | Unset
        if isinstance(_total_pay_by_currency, Unset):
            total_pay_by_currency = UNSET
        else:
            total_pay_by_currency = PayReportV2TotalPayByCurrency.from_dict(
                _total_pay_by_currency
            )

        pay_report_v2 = cls(
            created_at=created_at,
            end_date=end_date,
            id=id,
            name=name,
            overlapping_shifts=overlapping_shifts,
            schedule_ids=schedule_ids,
            start_date=start_date,
            status=status,
            unpaid_shifts=unpaid_shifts,
            updated_at=updated_at,
            creator=creator,
            error_code=error_code,
            error_message=error_message,
            published_at=published_at,
            total_duration_seconds=total_duration_seconds,
            total_pay_by_currency=total_pay_by_currency,
        )

        pay_report_v2.additional_properties = d
        return pay_report_v2

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
