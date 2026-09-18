from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.identity_v1 import IdentityV1


T = TypeVar("T", bound="UtilitiesIdentityResultV1")


@_attrs_define
class UtilitiesIdentityResultV1:
    """
    Example:
        {'identity': {'dashboard_url': 'https://app.incident.io/my-org', 'name': 'Alertmanager token', 'roles':
            ['viewer'], 'team_roles': ['catalog_editor'], 'teams': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name':
            'Platform'}]}}

    Attributes:
        identity (IdentityV1):  Example: {'dashboard_url': 'https://app.incident.io/my-org', 'name': 'Alertmanager
            token', 'roles': ['viewer'], 'team_roles': ['catalog_editor'], 'teams': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Platform'}]}.
    """

    identity: IdentityV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identity": identity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.identity_v1 import IdentityV1

        d = dict(src_dict)
        identity = IdentityV1.from_dict(d.pop("identity"))

        utilities_identity_result_v1 = cls(
            identity=identity,
        )

        utilities_identity_result_v1.additional_properties = d
        return utilities_identity_result_v1

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
