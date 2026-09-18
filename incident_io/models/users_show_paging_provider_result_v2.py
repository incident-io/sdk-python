from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.users_show_paging_provider_result_v2_preferred_escalation_provider import (
    UsersShowPagingProviderResultV2PreferredEscalationProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersShowPagingProviderResultV2")


@_attrs_define
class UsersShowPagingProviderResultV2:
    """
    Example:
        {'preferred_escalation_provider': 'native'}

    Attributes:
        preferred_escalation_provider (UsersShowPagingProviderResultV2PreferredEscalationProvider | Unset): The user's
            effective escalation provider. Example: native.
    """

    preferred_escalation_provider: (
        UsersShowPagingProviderResultV2PreferredEscalationProvider | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preferred_escalation_provider: str | Unset = UNSET
        if not isinstance(self.preferred_escalation_provider, Unset):
            preferred_escalation_provider = self.preferred_escalation_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preferred_escalation_provider is not UNSET:
            field_dict["preferred_escalation_provider"] = preferred_escalation_provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _preferred_escalation_provider = d.pop("preferred_escalation_provider", UNSET)
        preferred_escalation_provider: (
            UsersShowPagingProviderResultV2PreferredEscalationProvider | Unset
        )
        if isinstance(_preferred_escalation_provider, Unset):
            preferred_escalation_provider = UNSET
        else:
            preferred_escalation_provider = (
                UsersShowPagingProviderResultV2PreferredEscalationProvider(
                    _preferred_escalation_provider
                )
            )

        users_show_paging_provider_result_v2 = cls(
            preferred_escalation_provider=preferred_escalation_provider,
        )

        users_show_paging_provider_result_v2.additional_properties = d
        return users_show_paging_provider_result_v2

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
