from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_route_target_v2 import CallRouteTargetV2


T = TypeVar("T", bound="CallRoutePathNodeLevelV2")


@_attrs_define
class CallRoutePathNodeLevelV2:
    """The targets a level pages.

    We call each target for 30 seconds, rotating to the next after 60 seconds, and
    move to the next node if nobody acknowledges within 5 minutes. Those timings are
    fixed for call routes.

        Example:
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id':
                '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule', 'urgency': 'high'}]}

        Attributes:
            targets (list[CallRouteTargetV2]): The users and schedules to page Example: [{'id': 'lawrencejones',
                'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
                'urgency': 'high'}].
    """

    targets: list[CallRouteTargetV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_route_target_v2 import CallRouteTargetV2

        d = dict(src_dict)
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = CallRouteTargetV2.from_dict(targets_item_data)

            targets.append(targets_item)

        call_route_path_node_level_v2 = cls(
            targets=targets,
        )

        call_route_path_node_level_v2.additional_properties = d
        return call_route_path_node_level_v2

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
