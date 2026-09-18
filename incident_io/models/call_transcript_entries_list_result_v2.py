from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_transcript_entry_v2 import CallTranscriptEntryV2
    from ..models.pagination_meta_result_v2 import PaginationMetaResultV2


T = TypeVar("T", bound="CallTranscriptEntriesListResultV2")


@_attrs_define
class CallTranscriptEntriesListResultV2:
    """
    Example:
        {'call_transcript_entries': [{'content': 'I think we should roll back the deploy.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'medium': 'spoken', 'participant_name': 'Alice Smith', 'timestamp':
            '2021-08-17T13:28:57.801578Z'}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        call_transcript_entries (list[CallTranscriptEntryV2]):  Example: [{'content': 'I think we should roll back the
            deploy.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'medium': 'spoken', 'participant_name': 'Alice Smith',
            'timestamp': '2021-08-17T13:28:57.801578Z'}].
        pagination_meta (PaginationMetaResultV2 | Unset):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}.
    """

    call_transcript_entries: list[CallTranscriptEntryV2]
    pagination_meta: PaginationMetaResultV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_transcript_entries = []
        for call_transcript_entries_item_data in self.call_transcript_entries:
            call_transcript_entries_item = call_transcript_entries_item_data.to_dict()
            call_transcript_entries.append(call_transcript_entries_item)

        pagination_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_transcript_entries": call_transcript_entries,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_transcript_entry_v2 import (
            CallTranscriptEntryV2,
        )
        from ..models.pagination_meta_result_v2 import (
            PaginationMetaResultV2,
        )

        d = dict(src_dict)
        call_transcript_entries = []
        _call_transcript_entries = d.pop("call_transcript_entries")
        for call_transcript_entries_item_data in _call_transcript_entries:
            call_transcript_entries_item = CallTranscriptEntryV2.from_dict(
                call_transcript_entries_item_data
            )

            call_transcript_entries.append(call_transcript_entries_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: PaginationMetaResultV2 | Unset
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResultV2.from_dict(_pagination_meta)

        call_transcript_entries_list_result_v2 = cls(
            call_transcript_entries=call_transcript_entries,
            pagination_meta=pagination_meta,
        )

        call_transcript_entries_list_result_v2.additional_properties = d
        return call_transcript_entries_list_result_v2

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
