from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.secret_v2 import SecretV2


T = TypeVar("T", bound="SecretsUpdateResultV2")


@_attrs_define
class SecretsUpdateResultV2:
    """
    Example:
        {'secret': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Auth token for the PagerDuty outgoing
            webhook', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123', 'name': 'PagerDuty webhook token',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 3}}

    Attributes:
        secret (SecretV2): A secret is a named credential that workflows can reference, for example
            an auth token for an outgoing webhook.

            Its value can be set and rotated but never read back: the API stores it
            encrypted and only ever returns masked metadata (the last four characters of
            the current value). Update the value with the rotate action, which appends a
            new version and retires the previous one. Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Auth token for the PagerDuty outgoing webhook', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123',
            'name': 'PagerDuty webhook token', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 3}.
    """

    secret: SecretV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.secret_v2 import SecretV2

        d = dict(src_dict)
        secret = SecretV2.from_dict(d.pop("secret"))

        secrets_update_result_v2 = cls(
            secret=secret,
        )

        secrets_update_result_v2.additional_properties = d
        return secrets_update_result_v2

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
