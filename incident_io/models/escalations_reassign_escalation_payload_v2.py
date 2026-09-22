from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationsReassignEscalationPayloadV2")


@_attrs_define(kw_only=True)
class EscalationsReassignEscalationPayloadV2:
    """
    Example:
        {'description': 'Database CPU has been above 90% for 5 minutes', 'escalation_path_id':
            '01H0J1EXE7AXZ2C93K61WBPYEH', 'resolve_original': True, 'title': 'Production database experiencing high CPU',
            'user_ids': ['01H0J1EXE7AXZ2C93K61WBPYEH', '01H0J1EXE7AXZ2C93K61WBPYEI']}

    Attributes:
        description (str | Unset): Additional details about the new escalation. Defaults to the original's description.
            Example: Database CPU has been above 90% for 5 minutes.
        escalation_path_id (str | Unset): ID of the escalation path to reassign to Example: 01H0J1EXE7AXZ2C93K61WBPYEH.
        resolve_original (bool | Unset): Whether to resolve the original escalation, stopping it paging its targets.
            Defaults to true. Default: True. Example: True.
        title (str | Unset): The title of the new escalation. Defaults to the original's title. Example: Production
            database experiencing high CPU.
        user_ids (list[str] | Unset): IDs of users to reassign directly to Example: ['01H0J1EXE7AXZ2C93K61WBPYEH',
            '01H0J1EXE7AXZ2C93K61WBPYEI'].
    """

    description: str | Unset = UNSET
    escalation_path_id: str | Unset = UNSET
    resolve_original: bool | Unset = True
    title: str | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        escalation_path_id = self.escalation_path_id

        resolve_original = self.resolve_original

        title = self.title

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if escalation_path_id is not UNSET:
            field_dict["escalation_path_id"] = escalation_path_id
        if resolve_original is not UNSET:
            field_dict["resolve_original"] = resolve_original
        if title is not UNSET:
            field_dict["title"] = title
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        escalation_path_id = d.pop("escalation_path_id", UNSET)

        resolve_original = d.pop("resolve_original", UNSET)

        title = d.pop("title", UNSET)

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        escalations_reassign_escalation_payload_v2 = cls(
            description=description,
            escalation_path_id=escalation_path_id,
            resolve_original=resolve_original,
            title=title,
            user_ids=user_ids,
        )

        escalations_reassign_escalation_payload_v2.additional_properties = d
        return escalations_reassign_escalation_payload_v2

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
