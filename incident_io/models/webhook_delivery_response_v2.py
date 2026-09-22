from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_delivery_response_v2_headers import (
        WebhookDeliveryResponseV2Headers,
    )


T = TypeVar("T", bound="WebhookDeliveryResponseV2")


@_attrs_define(kw_only=True)
class WebhookDeliveryResponseV2:
    """
    Example:
        {'body': '{"error":"unprocessable"}', 'body_truncated': False, 'headers': {'Content-Type': 'application/json'}}

    Attributes:
        body_truncated (bool): Whether the body was truncated, in which case it may not be valid JSON Example: False.
        headers (WebhookDeliveryResponseV2Headers): Headers returned by the endpoint, excluding any whose name resembles
            a credential Example: {'Content-Type': 'application/json'}.
        body (str | Unset): The response body returned by the endpoint Example: {"error":"unprocessable"}.
    """

    body_truncated: bool
    headers: WebhookDeliveryResponseV2Headers
    body: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_truncated = self.body_truncated

        headers = self.headers.to_dict()

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body_truncated": body_truncated,
                "headers": headers,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_delivery_response_v2_headers import (
            WebhookDeliveryResponseV2Headers,
        )

        d = dict(src_dict)
        body_truncated = d.pop("body_truncated")

        headers = WebhookDeliveryResponseV2Headers.from_dict(d.pop("headers"))

        body = d.pop("body", UNSET)

        webhook_delivery_response_v2 = cls(
            body_truncated=body_truncated,
            headers=headers,
            body=body,
        )

        webhook_delivery_response_v2.additional_properties = d
        return webhook_delivery_response_v2

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
