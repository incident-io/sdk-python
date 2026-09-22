from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadMetadataV2")


@_attrs_define(kw_only=True)
class WorkloadMetadataV2:
    """
    Example:
        {'data_synced_at': '2021-08-17T13:00:00Z'}

    Attributes:
        data_synced_at (datetime.datetime | Unset): The time the workload figures are calculated up to. Workload is
            complete up to this time. Null if we have not calculated any workload for this incident yet. Example:
            2021-08-17T13:00:00Z.
    """

    data_synced_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_synced_at: str | Unset = UNSET
        if not isinstance(self.data_synced_at, Unset):
            data_synced_at = self.data_synced_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_synced_at is not UNSET:
            field_dict["data_synced_at"] = data_synced_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _data_synced_at = d.pop("data_synced_at", UNSET)
        data_synced_at: datetime.datetime | Unset
        if isinstance(_data_synced_at, Unset):
            data_synced_at = UNSET
        else:
            data_synced_at = datetime.datetime.fromisoformat(_data_synced_at)

        workload_metadata_v2 = cls(
            data_synced_at=data_synced_at,
        )

        workload_metadata_v2.additional_properties = d
        return workload_metadata_v2

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
