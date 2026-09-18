from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_source_email_options_v2_redactions_item import (
    AlertSourceEmailOptionsV2RedactionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSourceEmailOptionsV2")


@_attrs_define
class AlertSourceEmailOptionsV2:
    """
    Example:
        {'email_address': 'lawrence@example.com', 'redactions': ['credit_card_numbers'], 'transform_expression': "return
            {\\n  title: $.subject,\\n  description: $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' :
            'firing',\\n  deduplication_key: $.header_message_id,\\n}"}

    Attributes:
        email_address (str): Email address this alert source receives alerts to Example: lawrence@example.com.
        redactions (list[AlertSourceEmailOptionsV2RedactionsItem]): Which PII types to automatically redact from
            incoming email content before storage Example: ['credit_card_numbers'].
        transform_expression (str | Unset): JavaScript expression to transform email fields into structured alert fields
            Example: return {
              title: $.subject,
              description: $.text,
              status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',
              deduplication_key: $.header_message_id,
            }.
    """

    email_address: str
    redactions: list[AlertSourceEmailOptionsV2RedactionsItem]
    transform_expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        redactions = []
        for redactions_item_data in self.redactions:
            redactions_item = redactions_item_data.value
            redactions.append(redactions_item)

        transform_expression = self.transform_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_address": email_address,
                "redactions": redactions,
            }
        )
        if transform_expression is not UNSET:
            field_dict["transform_expression"] = transform_expression

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email_address = d.pop("email_address")

        redactions = []
        _redactions = d.pop("redactions")
        for redactions_item_data in _redactions:
            redactions_item = AlertSourceEmailOptionsV2RedactionsItem(
                redactions_item_data
            )

            redactions.append(redactions_item)

        transform_expression = d.pop("transform_expression", UNSET)

        alert_source_email_options_v2 = cls(
            email_address=email_address,
            redactions=redactions,
            transform_expression=transform_expression,
        )

        alert_source_email_options_v2.additional_properties = d
        return alert_source_email_options_v2

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
