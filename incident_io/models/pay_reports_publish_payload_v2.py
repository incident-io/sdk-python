from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pay_reports_publish_payload_v2_send_user_breakdowns import (
    PayReportsPublishPayloadV2SendUserBreakdowns,
)

T = TypeVar("T", bound="PayReportsPublishPayloadV2")


@_attrs_define(kw_only=True)
class PayReportsPublishPayloadV2:
    """
    Example:
        {'cc_emails': ['finance@example.com'], 'send_user_breakdowns': 'skip'}

    Attributes:
        cc_emails (list[str]): Email addresses to send a copy of the report to Example: ['finance@example.com'].
        send_user_breakdowns (PayReportsPublishPayloadV2SendUserBreakdowns): Whether each user in the report is emailed
            their own pay breakdown Example: skip.
    """

    cc_emails: list[str]
    send_user_breakdowns: PayReportsPublishPayloadV2SendUserBreakdowns
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cc_emails = self.cc_emails

        send_user_breakdowns = self.send_user_breakdowns.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cc_emails": cc_emails,
                "send_user_breakdowns": send_user_breakdowns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cc_emails = cast(list[str], d.pop("cc_emails"))

        send_user_breakdowns = PayReportsPublishPayloadV2SendUserBreakdowns(
            d.pop("send_user_breakdowns")
        )

        pay_reports_publish_payload_v2 = cls(
            cc_emails=cc_emails,
            send_user_breakdowns=send_user_breakdowns,
        )

        pay_reports_publish_payload_v2.additional_properties = d
        return pay_reports_publish_payload_v2

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
