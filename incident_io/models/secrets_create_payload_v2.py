from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretsCreatePayloadV2")


@_attrs_define
class SecretsCreatePayloadV2:
    """
    Example:
        {'description': 'Auth token for the PagerDuty outgoing webhook', 'name': 'PagerDuty webhook token',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'value': 'sk_live_abc123'}

    Attributes:
        name (str): Human-readable name, unique within the organisation amongst unarchived secrets Example: PagerDuty
            webhook token.
        value (str): The secret's plaintext value. It's stored encrypted and never returned by the API. Example:
            sk_live_abc123.
        description (str | Unset): Optional description of what this secret is for Example: Auth token for the PagerDuty
            outgoing webhook.
        owning_team_ids (list[str] | Unset): IDs of the teams that own this secret. When empty or omitted, the secret is
            owned by the whole organisation. Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    name: str
    value: str
    description: str | Unset = UNSET
    owning_team_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        description = self.description

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
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

        value = d.pop("value")

        description = d.pop("description", UNSET)

        owning_team_ids = cast(list[str], d.pop("owning_team_ids", UNSET))

        secrets_create_payload_v2 = cls(
            name=name,
            value=value,
            description=description,
            owning_team_ids=owning_team_ids,
        )

        secrets_create_payload_v2.additional_properties = d
        return secrets_create_payload_v2

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
