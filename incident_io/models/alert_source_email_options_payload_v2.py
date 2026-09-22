from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_source_email_options_payload_v2_redactions_item import (
    AlertSourceEmailOptionsPayloadV2RedactionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSourceEmailOptionsPayloadV2")


@_attrs_define(kw_only=True)
class AlertSourceEmailOptionsPayloadV2:
    """
    Example:
        {'redactions': ['credit_card_numbers'], 'transform_expression': "return {\\n  title: $.subject,\\n  description:
            $.text,\\n  status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',\\n  deduplication_key:
            $.header_message_id,\\n}"}

    Attributes:
        redactions (list[AlertSourceEmailOptionsPayloadV2RedactionsItem]): Which PII types to automatically redact from
            incoming email content before storage Example: ['credit_card_numbers'].
        transform_expression (str | Unset): JavaScript expression to transform email fields into structured alert fields
            Example: return {
              title: $.subject,
              description: $.text,
              status: $.subject.startsWith('[RESOLVED]') ? 'resolved' : 'firing',
              deduplication_key: $.header_message_id,
            }.
    """

    redactions: list[AlertSourceEmailOptionsPayloadV2RedactionsItem]
    transform_expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redactions = []
        for redactions_item_data in self.redactions:
            redactions_item = redactions_item_data.value
            redactions.append(redactions_item)

        transform_expression = self.transform_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redactions": redactions,
            }
        )
        if transform_expression is not UNSET:
            field_dict["transform_expression"] = transform_expression

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        redactions = []
        _redactions = d.pop("redactions")
        for redactions_item_data in _redactions:
            redactions_item = AlertSourceEmailOptionsPayloadV2RedactionsItem(
                redactions_item_data
            )

            redactions.append(redactions_item)

        transform_expression = d.pop("transform_expression", UNSET)

        alert_source_email_options_payload_v2 = cls(
            redactions=redactions,
            transform_expression=transform_expression,
        )

        alert_source_email_options_payload_v2.additional_properties = d
        return alert_source_email_options_payload_v2

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
