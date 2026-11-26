from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_grouping_default_branch_v3 import AlertGroupingDefaultBranchV3


T = TypeVar("T", bound="TeamGroupingPreferencesUpdatePayloadV3")


@_attrs_define(kw_only=True)
class TeamGroupingPreferencesUpdatePayloadV3:
    """
    Example:
        {'default': {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters describe
            the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}}, 'version': 4}

    Attributes:
        default (AlertGroupingDefaultBranchV3): The fallback branch: how to group the alerts that no conditional branch
            matches Example: {'settings': {'ai_enabled': False, 'ai_instructions': 'Alerts from the old and new clusters
            describe the same outage, so group them together.', 'enabled': True, 'grouping_keys': [{'reference':
            'alert.title'}], 'window_seconds': 1800, 'window_type': 'rolling'}}.
        version (int): The version this update will create. It must be one more than the preference's latest version,
            otherwise the update is rejected - guarding against concurrent edits. Example: 4.
    """

    default: AlertGroupingDefaultBranchV3
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_grouping_default_branch_v3 import (
            AlertGroupingDefaultBranchV3,
        )

        d = dict(src_dict)
        default = AlertGroupingDefaultBranchV3.from_dict(d.pop("default"))

        version = d.pop("version")

        team_grouping_preferences_update_payload_v3 = cls(
            default=default,
            version=version,
        )

        team_grouping_preferences_update_payload_v3.additional_properties = d
        return team_grouping_preferences_update_payload_v3

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
