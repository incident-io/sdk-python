from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ErrorRateLimit")


@_attrs_define(kw_only=True)
class ErrorRateLimit:
    """
    Example:
        {'limit': 100, 'name': 'client_ip', 'remaining': 98, 'retry_after': '2020-01-01T00:00:00Z'}

    Attributes:
        limit (int): The maximum number of requests that the consumer is permitted to make per minute Example: 100.
        name (str): Which rate limit was exceeded Example: client_ip.
        remaining (int): The number of requests remaining in the current rate limit window Example: 98.
        retry_after (str): When the client can retry, as an RFC3339 timestamp in UTC. Prefer the Retry-After response
            header, which carries the same instant as a number of seconds Example: 2020-01-01T00:00:00Z.
    """

    limit: int
    name: str
    remaining: int
    retry_after: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        name = self.name

        remaining = self.remaining

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "name": name,
                "remaining": remaining,
                "retry_after": retry_after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        limit = d.pop("limit")

        name = d.pop("name")

        remaining = d.pop("remaining")

        retry_after = d.pop("retry_after")

        error_rate_limit = cls(
            limit=limit,
            name=name,
            remaining=remaining,
            retry_after=retry_after,
        )

        error_rate_limit.additional_properties = d
        return error_rate_limit

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
