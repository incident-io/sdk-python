from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actions_update_payload_v3_status import ActionsUpdatePayloadV3Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsUpdatePayloadV3")


@_attrs_define(kw_only=True)
class ActionsUpdatePayloadV3:
    """
    Example:
        {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade', 'status': 'outstanding'}

    Attributes:
        description (str): Description of the action. Supports Markdown. Example: Call the fire brigade.
        status (ActionsUpdatePayloadV3Status): Status of the action. Setting this to `deleted` is not allowed; use the
            delete endpoint instead. Example: outstanding.
        assignee_id (str | Unset): ID of the user this action is assigned to. Set to null to unassign. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    description: str
    status: ActionsUpdatePayloadV3Status
    assignee_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        status = self.status.value

        assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "status": status,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        status = ActionsUpdatePayloadV3Status(d.pop("status"))

        assignee_id = d.pop("assignee_id", UNSET)

        actions_update_payload_v3 = cls(
            description=description,
            status=status,
            assignee_id=assignee_id,
        )

        actions_update_payload_v3.additional_properties = d
        return actions_update_payload_v3

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
