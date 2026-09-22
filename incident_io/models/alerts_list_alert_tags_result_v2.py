from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_tag_v2 import AlertTagV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="AlertsListAlertTagsResultV2")


@_attrs_define(kw_only=True)
class AlertsListAlertTagsResultV2:
    """
    Example:
        {'alert_tags': [{'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        alert_tags (list[AlertTagV2]):  Example: [{'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}].
        pagination_meta (PaginationMetaResultV2):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    alert_tags: list[AlertTagV2]
    pagination_meta: PaginationMetaResultV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_tags = []
        for alert_tags_item_data in self.alert_tags:
            alert_tags_item = alert_tags_item_data.to_dict()
            alert_tags.append(alert_tags_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_tags": alert_tags,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_tag_v2 import AlertTagV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        alert_tags = []
        _alert_tags = d.pop("alert_tags")
        for alert_tags_item_data in _alert_tags:
            alert_tags_item = AlertTagV2.from_dict(alert_tags_item_data)

            alert_tags.append(alert_tags_item)

        pagination_meta = PaginationMetaResultV2.from_dict(d.pop("pagination_meta"))

        alerts_list_alert_tags_result_v2 = cls(
            alert_tags=alert_tags,
            pagination_meta=pagination_meta,
        )

        alerts_list_alert_tags_result_v2.additional_properties = d
        return alerts_list_alert_tags_result_v2

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
