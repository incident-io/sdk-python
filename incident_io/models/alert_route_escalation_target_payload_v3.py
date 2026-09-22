from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRouteEscalationTargetPayloadV3")


@_attrs_define(kw_only=True)
class AlertRouteEscalationTargetPayloadV3:
    """
    Example:
        {'escalation_paths': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'users': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        escalation_paths (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        users (EngineParamBindingPayloadV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    escalation_paths: EngineParamBindingPayloadV3 | Unset = UNSET
    users: EngineParamBindingPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation_paths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.escalation_paths, Unset):
            escalation_paths = self.escalation_paths.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if escalation_paths is not UNSET:
            field_dict["escalation_paths"] = escalation_paths
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        _escalation_paths = d.pop("escalation_paths", UNSET)
        escalation_paths: EngineParamBindingPayloadV3 | Unset
        if isinstance(_escalation_paths, Unset):
            escalation_paths = UNSET
        else:
            escalation_paths = EngineParamBindingPayloadV3.from_dict(_escalation_paths)

        _users = d.pop("users", UNSET)
        users: EngineParamBindingPayloadV3 | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = EngineParamBindingPayloadV3.from_dict(_users)

        alert_route_escalation_target_payload_v3 = cls(
            escalation_paths=escalation_paths,
            users=users,
        )

        alert_route_escalation_target_payload_v3.additional_properties = d
        return alert_route_escalation_target_payload_v3

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
