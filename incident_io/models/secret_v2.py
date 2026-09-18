from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretV2")


@_attrs_define
class SecretV2:
    """A secret is a named credential that workflows can reference, for example
    an auth token for an outgoing webhook.

    Its value can be set and rotated but never read back: the API stores it
    encrypted and only ever returns masked metadata (the last four characters of
    the current value). Update the value with the rotate action, which appends a
    new version and retires the previous one.

        Example:
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Auth token for the PagerDuty outgoing webhook',
                'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123', 'name': 'PagerDuty webhook token',
                'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 3}

        Attributes:
            created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            id (str): Unique identifier for this secret Example: 01FCNDV6P870EA6S7TK1DSYDG0.
            name (str): Human-readable name, unique within the organisation amongst unarchived secrets Example: PagerDuty
                webhook token.
            owning_team_ids (list[str]): IDs of the teams that own this secret. Empty means the secret is owned by the whole
                organisation. Example: ['01G0J1EXE7AXZ2C93K61WBPYEH'].
            updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
            version (int): The current version number, incremented on each rotation Example: 3.
            description (str | Unset): Optional description of what this secret is for Example: Auth token for the PagerDuty
                outgoing webhook.
            last_four_chars (str | Unset): The last four characters of the current value, for masked display. Absent when
                the value is four characters or shorter. Example: c123.
    """

    created_at: datetime.datetime
    id: str
    name: str
    owning_team_ids: list[str]
    updated_at: datetime.datetime
    version: int
    description: str | Unset = UNSET
    last_four_chars: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        owning_team_ids = self.owning_team_ids

        updated_at = self.updated_at.isoformat()

        version = self.version

        description = self.description

        last_four_chars = self.last_four_chars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "owning_team_ids": owning_team_ids,
                "updated_at": updated_at,
                "version": version,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if last_four_chars is not UNSET:
            field_dict["last_four_chars"] = last_four_chars

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        owning_team_ids = cast(list[str], d.pop("owning_team_ids"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        description = d.pop("description", UNSET)

        last_four_chars = d.pop("last_four_chars", UNSET)

        secret_v2 = cls(
            created_at=created_at,
            id=id,
            name=name,
            owning_team_ids=owning_team_ids,
            updated_at=updated_at,
            version=version,
            description=description,
            last_four_chars=last_four_chars,
        )

        secret_v2.additional_properties = d
        return secret_v2

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
