from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_reference_payload_v2 import UserReferencePayloadV2


T = TypeVar("T", bound="SchedulesUpdateOverridePayloadV2")


@_attrs_define
class SchedulesUpdateOverridePayloadV2:
    """
    Example:
        {'end_at': '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:00:00.000000Z', 'user': {'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}

    Attributes:
        end_at (datetime.datetime): End time of the override Example: 2021-08-17T14:00:00.000000Z.
        layer_id (str): The layer this override applies to Example: 01G0J1EXE7AXZ2C93K61WBPYNH.
        rotation_id (str): The rotation this override applies to Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        start_at (datetime.datetime): Start time of the override Example: 2021-08-17T13:00:00.000000Z.
        user (UserReferencePayloadV2):  Example: {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}.
    """

    end_at: datetime.datetime
    layer_id: str
    rotation_id: str
    start_at: datetime.datetime
    user: UserReferencePayloadV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_at = self.end_at.isoformat()

        layer_id = self.layer_id

        rotation_id = self.rotation_id

        start_at = self.start_at.isoformat()

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "layer_id": layer_id,
                "rotation_id": rotation_id,
                "start_at": start_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_reference_payload_v2 import (
            UserReferencePayloadV2,
        )

        d = dict(src_dict)
        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        layer_id = d.pop("layer_id")

        rotation_id = d.pop("rotation_id")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        user = UserReferencePayloadV2.from_dict(d.pop("user"))

        schedules_update_override_payload_v2 = cls(
            end_at=end_at,
            layer_id=layer_id,
            rotation_id=rotation_id,
            start_at=start_at,
            user=user,
        )

        schedules_update_override_payload_v2.additional_properties = d
        return schedules_update_override_payload_v2

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
