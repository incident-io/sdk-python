from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_route_slim_v3 import AlertRouteSlimV3
    from ..models.pagination_meta_result_v3 import PaginationMetaResultV3


T = TypeVar("T", bound="AlertRoutesListResultV3")


@_attrs_define(kw_only=True)
class AlertRoutesListResultV3:
    """
    Example:
        {'alert_routes': [{'enabled': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Production incidents'}],
            'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        alert_routes (list[AlertRouteSlimV3]):  Example: [{'enabled': False, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Production incidents'}].
        pagination_meta (PaginationMetaResultV3):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    alert_routes: list[AlertRouteSlimV3]
    pagination_meta: PaginationMetaResultV3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_routes = []
        for alert_routes_item_data in self.alert_routes:
            alert_routes_item = alert_routes_item_data.to_dict()
            alert_routes.append(alert_routes_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_routes": alert_routes,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_route_slim_v3 import AlertRouteSlimV3
        from ..models.pagination_meta_result_v3 import (
            PaginationMetaResultV3,
        )

        d = dict(src_dict)
        alert_routes = []
        _alert_routes = d.pop("alert_routes")
        for alert_routes_item_data in _alert_routes:
            alert_routes_item = AlertRouteSlimV3.from_dict(alert_routes_item_data)

            alert_routes.append(alert_routes_item)

        pagination_meta = PaginationMetaResultV3.from_dict(d.pop("pagination_meta"))

        alert_routes_list_result_v3 = cls(
            alert_routes=alert_routes,
            pagination_meta=pagination_meta,
        )

        alert_routes_list_result_v3.additional_properties = d
        return alert_routes_list_result_v3

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
