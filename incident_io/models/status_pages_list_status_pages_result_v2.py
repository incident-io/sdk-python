from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2
    from ..models.status_page_v2 import StatusPageV2


T = TypeVar("T", bound="StatusPagesListStatusPagesResultV2")


@_attrs_define
class StatusPagesListStatusPagesResultV2:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'status_pages': [{'description':
            'This status page is our public status page.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Our public status
            page', 'public_url': 'https://statuspage.incident.io/our-public-status-page'}]}

    Attributes:
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        status_pages (list[StatusPageV2]):  Example: [{'description': 'This status page is our public status page.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Our public status page', 'public_url':
            'https://statuspage.incident.io/our-public-status-page'}].
    """

    pagination_meta: PaginationMetaResultV2
    status_pages: list[StatusPageV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        status_pages = []
        for status_pages_item_data in self.status_pages:
            status_pages_item = status_pages_item_data.to_dict()
            status_pages.append(status_pages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "status_pages": status_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )
        from ..models.status_page_v2 import StatusPageV2

        d = dict(src_dict)
        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        status_pages = []
        _status_pages = d.pop("status_pages")
        for status_pages_item_data in _status_pages:
            status_pages_item = StatusPageV2.from_dict(status_pages_item_data)

            status_pages.append(status_pages_item)

        status_pages_list_status_pages_result_v2 = cls(
            pagination_meta=pagination_meta,
            status_pages=status_pages,
        )

        status_pages_list_status_pages_result_v2.additional_properties = d
        return status_pages_list_status_pages_result_v2

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
