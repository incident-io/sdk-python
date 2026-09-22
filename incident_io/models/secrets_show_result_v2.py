from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.secret_v2 import SecretV2
    from ..models.secret_version_v2 import SecretVersionV2


T = TypeVar("T", bound="SecretsShowResultV2")


@_attrs_define(kw_only=True)
class SecretsShowResultV2:
    """
    Example:
        {'secret': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Auth token for the PagerDuty outgoing
            webhook', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_four_chars': 'c123', 'name': 'PagerDuty webhook token',
            'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'updated_at': '2021-08-17T13:28:57.801578Z', 'version': 3},
            'versions': [{'created_at': '2021-08-17T13:28:57.801578Z', 'created_by': {'alert': {'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'last_four_chars': 'c123',
            'version': 3}]}

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
        versions (list[SecretVersionV2]): The secret's versions, newest first Example: [{'created_at':
            '2021-08-17T13:28:57.801578Z', 'created_by': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}, 'last_four_chars': 'c123', 'version': 3}].
    """

    secret: SecretV2
    versions: list[SecretVersionV2]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret.to_dict()

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.secret_v2 import SecretV2
        from ..models.secret_version_v2 import SecretVersionV2

        d = dict(src_dict)
        secret = SecretV2.from_dict(d.pop("secret"))

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = SecretVersionV2.from_dict(versions_item_data)

            versions.append(versions_item)

        secrets_show_result_v2 = cls(
            secret=secret,
            versions=versions,
        )

        secrets_show_result_v2.additional_properties = d
        return secrets_show_result_v2

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
