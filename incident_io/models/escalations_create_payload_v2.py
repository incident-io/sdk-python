from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationsCreatePayloadV2")


@_attrs_define(kw_only=True)
class EscalationsCreatePayloadV2:
    """
    Example:
        {'description': 'Database CPU has been above 90% for 5 minutes', 'escalation_path_id':
            '01H0J1EXE7AXZ2C93K61WBPYEH', 'idempotency_key': '2024-01-15-abc123', 'incident_id':
            '01H0J1EXE7AXZ2C93K61WBPYEH', 'title': 'Production database experiencing high CPU', 'user_ids':
            ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}

    Attributes:
        idempotency_key (str): Unique key to prevent duplicate escalations. If this key has already been used, the
            existing escalation will be returned. Example: 2024-01-15-abc123.
        title (str): The title of the escalation. This message will be included in all notifications about this
            escalation. Example: Production database experiencing high CPU.
        description (str | Unset): Additional details about the escalation Example: Database CPU has been above 90% for
            5 minutes.
        escalation_path_id (str | Unset): ID of the escalation path to follow Example: 01H0J1EXE7AXZ2C93K61WBPYEH.
        incident_id (str | Unset): ID of an incident to associate with this escalation. The linked incident will appear
            in the escalation's related_incidents field. Example: 01H0J1EXE7AXZ2C93K61WBPYEH.
        user_ids (list[str] | Unset): IDs of users to escalate directly to Example: ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI'].
    """

    idempotency_key: str
    title: str
    description: str | Unset = UNSET
    escalation_path_id: str | Unset = UNSET
    incident_id: str | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        title = self.title

        description = self.description

        escalation_path_id = self.escalation_path_id

        incident_id = self.incident_id

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if escalation_path_id is not UNSET:
            field_dict["escalation_path_id"] = escalation_path_id
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        escalation_path_id = d.pop("escalation_path_id", UNSET)

        incident_id = d.pop("incident_id", UNSET)

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        escalations_create_payload_v2 = cls(
            idempotency_key=idempotency_key,
            title=title,
            description=description,
            escalation_path_id=escalation_path_id,
            incident_id=incident_id,
            user_ids=user_ids,
        )

        escalations_create_payload_v2.additional_properties = d
        return escalations_create_payload_v2

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
