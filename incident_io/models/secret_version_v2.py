from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2


T = TypeVar("T", bound="SecretVersionV2")


@_attrs_define(kw_only=True)
class SecretVersionV2:
    """A single version of a secret's value. Only metadata is exposed; the value itself is never returned.

    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'created_by': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
            'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'last_four_chars': 'c123', 'version': 3}

    Attributes:
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        version (int): The version number, incremented on each rotation Example: 3.
        created_by (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
        last_four_chars (str | Unset): The last four characters of this version's value, for masked display. Absent when
            the value was four characters or shorter. Example: c123.
    """

    created_at: datetime.datetime
    version: int
    created_by: ActorV2 | Unset = UNSET
    last_four_chars: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        version = self.version

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        last_four_chars = self.last_four_chars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "version": version,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_four_chars is not UNSET:
            field_dict["last_four_chars"] = last_four_chars

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        version = d.pop("version")

        _created_by = d.pop("created_by", UNSET)
        created_by: ActorV2 | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ActorV2.from_dict(_created_by)

        last_four_chars = d.pop("last_four_chars", UNSET)

        secret_version_v2 = cls(
            created_at=created_at,
            version=version,
            created_by=created_by,
            last_four_chars=last_four_chars,
        )

        secret_version_v2.additional_properties = d
        return secret_version_v2

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
