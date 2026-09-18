from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretsUpdatePayloadV2")


@_attrs_define
class SecretsUpdatePayloadV2:
    """
    Example:
        {'description': 'Auth token for the PagerDuty outgoing webhook', 'name': 'PagerDuty webhook token',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        name (str): Human-readable name, unique within the organisation amongst unarchived secrets Example: PagerDuty
            webhook token.
        description (str | Unset): Optional description of what this secret is for Example: Auth token for the PagerDuty
            outgoing webhook.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this secret. When omitted, the existing owning
            teams are left unchanged. Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    name: str
    description: str | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        secrets_update_payload_v2 = cls(
            name=name,
            description=description,
            owning_team_ids=owning_team_ids,
        )

        secrets_update_payload_v2.additional_properties = d
        return secrets_update_payload_v2

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
