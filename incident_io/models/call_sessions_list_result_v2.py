from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_session_v2 import CallSessionV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="CallSessionsListResultV2")


@_attrs_define(kw_only=True)
class CallSessionsListResultV2:
    """
    Example:
        {'call_sessions': [{'ended_at': '2021-08-17T14:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'started_at': '2021-08-17T13:28:57.801578Z'}], 'pagination_meta':
            {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        call_sessions (list[CallSessionV2]):  Example: [{'ended_at': '2021-08-17T14:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'started_at':
            '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    call_sessions: list[CallSessionV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_sessions = []
        for call_sessions_item_data in self.call_sessions:
            call_sessions_item = call_sessions_item_data.to_dict()
            call_sessions.append(call_sessions_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_sessions": call_sessions,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_session_v2 import CallSessionV2
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        call_sessions = []
        _call_sessions = d.pop("call_sessions")
        for call_sessions_item_data in _call_sessions:
            call_sessions_item = CallSessionV2.from_dict(call_sessions_item_data)

            call_sessions.append(call_sessions_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        call_sessions_list_result_v2 = cls(
            call_sessions=call_sessions,
            pagination_meta=pagination_meta,
        )

        call_sessions_list_result_v2.additional_properties = d
        return call_sessions_list_result_v2

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
