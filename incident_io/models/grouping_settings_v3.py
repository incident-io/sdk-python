from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grouping_settings_v3_window_type import GroupingSettingsV3WindowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grouping_key_v3 import GroupingKeyV3


T = TypeVar("T", bound="GroupingSettingsV3")


@_attrs_define
class GroupingSettingsV3:
    """
    Example:
        {'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800, 'window_type':
            'rolling'}

    Attributes:
        enabled (bool): Whether grouping is enabled Example: True.
        grouping_keys (list[GroupingKeyV3] | Unset): Which attributes should this alert route use to group alerts? Only
            set when grouping is enabled. Example: [{'reference': 'alert.title'}].
        window_seconds (int | Unset): How long the grouping window is, in seconds. Must be between 60 (1 minute) and
            172800 (48 hours). Only set when grouping is enabled. Example: 1800.
        window_type (GroupingSettingsV3WindowType | Unset): Controls how the grouping window behaves. 'rolling' keeps
            the window open for window_seconds after the most recent alert, so the group stays open as long as alerts keep
            arriving. 'fixed' opens the window when the first alert arrives and always closes window_seconds later,
            regardless of any subsequent alerts. Only set when grouping is enabled. Example: rolling.
    """

    enabled: bool
    grouping_keys: list[GroupingKeyV3] | Unset = UNSET
    window_seconds: int | Unset = UNSET
    window_type: GroupingSettingsV3WindowType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        grouping_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grouping_keys, Unset):
            grouping_keys = []
            for grouping_keys_item_data in self.grouping_keys:
                grouping_keys_item = grouping_keys_item_data.to_dict()
                grouping_keys.append(grouping_keys_item)

        window_seconds = self.window_seconds

        window_type: str | Unset = UNSET
        if not isinstance(self.window_type, Unset):
            window_type = self.window_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if grouping_keys is not UNSET:
            field_dict["grouping_keys"] = grouping_keys
        if window_seconds is not UNSET:
            field_dict["window_seconds"] = window_seconds
        if window_type is not UNSET:
            field_dict["window_type"] = window_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grouping_key_v3 import GroupingKeyV3

        d = dict(src_dict)
        enabled = d.pop("enabled")

        _grouping_keys = d.pop("grouping_keys", UNSET)
        grouping_keys: list[GroupingKeyV3] | Unset = UNSET
        if _grouping_keys is not UNSET:
            grouping_keys = []
            for grouping_keys_item_data in _grouping_keys:
                grouping_keys_item = GroupingKeyV3.from_dict(grouping_keys_item_data)

                grouping_keys.append(grouping_keys_item)

        window_seconds = d.pop("window_seconds", UNSET)

        _window_type = d.pop("window_type", UNSET)
        window_type: GroupingSettingsV3WindowType | Unset
        if isinstance(_window_type, Unset):
            window_type = UNSET
        else:
            window_type = GroupingSettingsV3WindowType(_window_type)

        grouping_settings_v3 = cls(
            enabled=enabled,
            grouping_keys=grouping_keys,
            window_seconds=window_seconds,
            window_type=window_type,
        )

        grouping_settings_v3.additional_properties = d
        return grouping_settings_v3

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
