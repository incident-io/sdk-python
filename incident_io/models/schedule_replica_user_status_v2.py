from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleReplicaUserStatusV2")


@_attrs_define(kw_only=True)
class ScheduleReplicaUserStatusV2:
    """
    Example:
        {'external_user_id': 'PJYTRGS', 'user_id': '01G0J1EXE7AXZ2C93K61WBPYEH'}

    Attributes:
        user_id (str): The incident.io user ID for a user who appears in the schedule rotation. Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        external_user_id (str | Unset): The corresponding user ID in the external provider (e.g. a PagerDuty user ID).
            If set, the user has been successfully mapped to an external user and will be included in the replica. If null,
            the user could not be resolved and syncing may produce errors. Example: PJYTRGS.
    """

    user_id: str
    external_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        external_user_id = self.external_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if external_user_id is not UNSET:
            field_dict["external_user_id"] = external_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        external_user_id = d.pop("external_user_id", UNSET)

        schedule_replica_user_status_v2 = cls(
            user_id=user_id,
            external_user_id=external_user_id,
        )

        schedule_replica_user_status_v2.additional_properties = d
        return schedule_replica_user_status_v2

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
