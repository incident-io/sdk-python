from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_slim_v2_outcome import WebhookDeliverySlimV2Outcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDeliverySlimV2")


@_attrs_define(kw_only=True)
class WebhookDeliverySlimV2:
    """
    Example:
        {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx',
            'status_code': 500}

    Attributes:
        endpoint (str): The interpolated URL the request was sent to. Redirects are followed, so this is the URL
            requested rather than the URL that ultimately served it Example: https://example.com/hooks/incident.
        method (str): HTTP method used for the request Example: POST.
        outcome (WebhookDeliverySlimV2Outcome): The result of the delivery attempt. Only success and non_2xx have a
            response Example: non_2xx.
        duration_ms (int | Unset): Time taken by the request, in milliseconds Example: 412.
        status_code (int | Unset): HTTP status code returned by the endpoint. Absent when no response was received
            Example: 500.
    """

    endpoint: str
    method: str
    outcome: WebhookDeliverySlimV2Outcome
    duration_ms: int | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        method = self.method

        outcome = self.outcome.value

        duration_ms = self.duration_ms

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "method": method,
                "outcome": outcome,
            }
        )
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        method = d.pop("method")

        outcome = WebhookDeliverySlimV2Outcome(d.pop("outcome"))

        duration_ms = d.pop("duration_ms", UNSET)

        status_code = d.pop("status_code", UNSET)

        webhook_delivery_slim_v2 = cls(
            endpoint=endpoint,
            method=method,
            outcome=outcome,
            duration_ms=duration_ms,
            status_code=status_code,
        )

        webhook_delivery_slim_v2.additional_properties = d
        return webhook_delivery_slim_v2

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
