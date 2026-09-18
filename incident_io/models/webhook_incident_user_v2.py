from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookIncidentUserV2")


@_attrs_define
class WebhookIncidentUserV2:
    """
    Example:
        {'actor_user_id': 'abc123', 'incident_id': 'abc123', 'user_id': 'abc123'}

    Attributes:
        incident_id (str): The ID of the incident Example: abc123.
        user_id (str): The ID of the user Example: abc123.
        actor_user_id (str | Unset): The ID of the user who performed this action. If the action was not taken by a
            user, for example it was taken by a Workflow, this will be empty. Example: abc123.
    """

    incident_id: str
    user_id: str
    actor_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        user_id = self.user_id

        actor_user_id = self.actor_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "user_id": user_id,
            }
        )
        if actor_user_id is not UNSET:
            field_dict["actor_user_id"] = actor_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        user_id = d.pop("user_id")

        actor_user_id = d.pop("actor_user_id", UNSET)

        webhook_incident_user_v2 = cls(
            incident_id=incident_id,
            user_id=user_id,
            actor_user_id=actor_user_id,
        )

        webhook_incident_user_v2.additional_properties = d
        return webhook_incident_user_v2

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
