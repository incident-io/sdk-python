from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_target_v2_type import AuditLogTargetV2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTargetV2")


@_attrs_define
class AuditLogTargetV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'John Doe', 'type': 'user'}

    Attributes:
        id (str): The ID of the target Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        type_ (AuditLogTargetV2Type): The type of target Example: user.
        name (str | Unset): The name of the target Example: John Doe.
    """

    id: str
    type_: AuditLogTargetV2Type
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = AuditLogTargetV2Type(d.pop("type"))

        name = d.pop("name", UNSET)

        audit_log_target_v2 = cls(
            id=id,
            type_=type_,
            name=name,
        )

        audit_log_target_v2.additional_properties = d
        return audit_log_target_v2

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
