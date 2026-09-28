from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_v2 import StatusPageV2


T = TypeVar("T", bound="StatusPagesShowStatusPageResultV2")


@_attrs_define(kw_only=True)
class StatusPagesShowStatusPageResultV2:
    """
    Example:
        {'status_page': {'description': 'This status page is our public status page.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Our public status page', 'public_url':
            'https://statuspage.incident.io/our-public-status-page'}}

    Attributes:
        status_page (StatusPageV2):  Example: {'description': 'This status page is our public status page.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Our public status page', 'public_url':
            'https://statuspage.incident.io/our-public-status-page'}.
    """

    status_page: StatusPageV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page = self.status_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page": status_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_page_v2 import StatusPageV2

        d = dict(src_dict)
        status_page = StatusPageV2.from_dict(d.pop("status_page"))

        status_pages_show_status_page_result_v2 = cls(
            status_page=status_page,
        )

        status_pages_show_status_page_result_v2.additional_properties = d
        return status_pages_show_status_page_result_v2

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
