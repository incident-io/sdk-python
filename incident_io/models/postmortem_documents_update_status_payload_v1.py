from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postmortem_documents_update_status_payload_v1_status import (
    PostmortemDocumentsUpdateStatusPayloadV1Status,
)

T = TypeVar("T", bound="PostmortemDocumentsUpdateStatusPayloadV1")


@_attrs_define(kw_only=True)
class PostmortemDocumentsUpdateStatusPayloadV1:
    """
    Example:
        {'status': 'completed'}

    Attributes:
        status (PostmortemDocumentsUpdateStatusPayloadV1Status): The new status to set the post-mortem document to
            Example: completed.
    """

    status: PostmortemDocumentsUpdateStatusPayloadV1Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = PostmortemDocumentsUpdateStatusPayloadV1Status(d.pop("status"))

        postmortem_documents_update_status_payload_v1 = cls(
            status=status,
        )

        postmortem_documents_update_status_payload_v1.additional_properties = d
        return postmortem_documents_update_status_payload_v1

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
