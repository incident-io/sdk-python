from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogInvestigationTriggerMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogInvestigationTriggerMetadataV2:
    """
    Example:
        {'blocks': 'false', 'enabled': 'true', 'frequency': 'once', 'moment': 'initial_searches', 'plugin_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'skill': 'orient', 'task_set': 'true'}

    Attributes:
        blocks (str): Whether the investigation waits for the trigger to finish before moving on (true, false) Example:
            false.
        enabled (str): Whether the trigger fires (true, false) Example: true.
        frequency (str): How often the trigger fires across one investigation Example: once.
        moment (str): When in an investigation the trigger runs Example: initial_searches.
        task_set (str): Whether the trigger hands the agent a task of its own (true, false) Example: true.
        plugin_id (str | Unset): The extension plugin holding the skill the trigger runs, absent for a trigger that only
            gives a task Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        skill (str | Unset): The skill directory the trigger runs, absent when the trigger leaves the choice of skill to
            the investigation Example: orient.
    """

    blocks: str
    enabled: str
    frequency: str
    moment: str
    task_set: str
    plugin_id: str | Unset = UNSET
    skill: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks = self.blocks

        enabled = self.enabled

        frequency = self.frequency

        moment = self.moment

        task_set = self.task_set

        plugin_id = self.plugin_id

        skill = self.skill

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blocks": blocks,
                "enabled": enabled,
                "frequency": frequency,
                "moment": moment,
                "task_set": task_set,
            }
        )
        if plugin_id is not UNSET:
            field_dict["plugin_id"] = plugin_id
        if skill is not UNSET:
            field_dict["skill"] = skill

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        blocks = d.pop("blocks")

        enabled = d.pop("enabled")

        frequency = d.pop("frequency")

        moment = d.pop("moment")

        task_set = d.pop("task_set")

        plugin_id = d.pop("plugin_id", UNSET)

        skill = d.pop("skill", UNSET)

        audit_log_investigation_trigger_metadata_v2 = cls(
            blocks=blocks,
            enabled=enabled,
            frequency=frequency,
            moment=moment,
            task_set=task_set,
            plugin_id=plugin_id,
            skill=skill,
        )

        audit_log_investigation_trigger_metadata_v2.additional_properties = d
        return audit_log_investigation_trigger_metadata_v2

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
