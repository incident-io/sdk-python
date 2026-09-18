from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_config_update_payload_v2 import ScheduleConfigUpdatePayloadV2
    from ..models.schedule_holidays_public_config_payload_v2 import (
        ScheduleHolidaysPublicConfigPayloadV2,
    )
    from ..models.schedule_update_payload_v2_annotations import (
        ScheduleUpdatePayloadV2Annotations,
    )


T = TypeVar("T", bound="ScheduleUpdatePayloadV2")


@_attrs_define
class ScheduleUpdatePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users':
            [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}]}, 'holidays_public_config':
            {'country_codes': ['abc123']}, 'name': 'Primary On-call Schedule', 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'],
            'timezone': 'America/Los_Angeles'}

    Attributes:
        annotations (ScheduleUpdatePayloadV2Annotations | Unset): Annotations that can track metadata about the schedule
            Example: {'incident.io/terraform/version': 'version-of-terraform'}.
        config (ScheduleConfigUpdatePayloadV2 | Unset):  Example: {'rotations': [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users': [{'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals': [{'end_time': '17:00', 'start_time': '09:00',
            'weekday': 'monday'}]}]}.
        holidays_public_config (ScheduleHolidaysPublicConfigPayloadV2 | Unset):  Example: {'country_codes': ['abc123']}.
        name (str | Unset): Name of the schedule Example: Primary On-call Schedule.
        team_ids (list[str] | Unset): IDs of teams that own this schedule Example: ['01JPQA75EPNEES4479P16P4XAB'].
        timezone (str | Unset): Timezone of the schedule Example: America/Los_Angeles.
    """

    annotations: ScheduleUpdatePayloadV2Annotations | Unset = UNSET
    config: ScheduleConfigUpdatePayloadV2 | Unset = UNSET
    holidays_public_config: ScheduleHolidaysPublicConfigPayloadV2 | Unset = UNSET
    name: str | Unset = UNSET
    team_ids: list[str] | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        holidays_public_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.holidays_public_config, Unset):
            holidays_public_config = self.holidays_public_config.to_dict()

        name = self.name

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if config is not UNSET:
            field_dict["config"] = config
        if holidays_public_config is not UNSET:
            field_dict["holidays_public_config"] = holidays_public_config
        if name is not UNSET:
            field_dict["name"] = name
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_config_update_payload_v2 import (
            ScheduleConfigUpdatePayloadV2,
        )
        from ..models.schedule_holidays_public_config_payload_v2 import (
            ScheduleHolidaysPublicConfigPayloadV2,
        )
        from ..models.schedule_update_payload_v2_annotations import (
            ScheduleUpdatePayloadV2Annotations,
        )

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: ScheduleUpdatePayloadV2Annotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ScheduleUpdatePayloadV2Annotations.from_dict(_annotations)

        _config = d.pop("config", UNSET)
        config: ScheduleConfigUpdatePayloadV2 | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ScheduleConfigUpdatePayloadV2.from_dict(_config)

        _holidays_public_config = d.pop("holidays_public_config", UNSET)
        holidays_public_config: ScheduleHolidaysPublicConfigPayloadV2 | Unset
        if isinstance(_holidays_public_config, Unset):
            holidays_public_config = UNSET
        else:
            holidays_public_config = ScheduleHolidaysPublicConfigPayloadV2.from_dict(
                _holidays_public_config
            )

        name = d.pop("name", UNSET)

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        timezone = d.pop("timezone", UNSET)

        schedule_update_payload_v2 = cls(
            annotations=annotations,
            config=config,
            holidays_public_config=holidays_public_config,
            name=name,
            team_ids=team_ids,
            timezone=timezone,
        )

        schedule_update_payload_v2.additional_properties = d
        return schedule_update_payload_v2

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
