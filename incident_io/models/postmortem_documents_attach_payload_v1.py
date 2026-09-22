from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postmortem_documents_attach_payload_v1_document_provider import (
    PostmortemDocumentsAttachPayloadV1DocumentProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostmortemDocumentsAttachPayloadV1")


@_attrs_define(kw_only=True)
class PostmortemDocumentsAttachPayloadV1:
    """
    Example:
        {'document_provider': 'notion', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'permalink':
            'https://www.notion.so/INC-123-database-is-sad'}

    Attributes:
        incident_id (str): The unique identifier of the incident to attach the post-mortem document to Example:
            01FCNDV6P870EA6S7TK1DSYD5H.
        permalink (str): A URL pointing to the externally-hosted post-mortem document Example:
            https://www.notion.so/INC-123-database-is-sad.
        document_provider (PostmortemDocumentsAttachPayloadV1DocumentProvider | Unset): The provider hosting the
            document. Set this when it can't be inferred from the permalink so the link renders correctly. Example: notion.
    """

    incident_id: str
    permalink: str
    document_provider: PostmortemDocumentsAttachPayloadV1DocumentProvider | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        permalink = self.permalink

        document_provider: str | Unset = UNSET
        if not isinstance(self.document_provider, Unset):
            document_provider = self.document_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "permalink": permalink,
            }
        )
        if document_provider is not UNSET:
            field_dict["document_provider"] = document_provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        permalink = d.pop("permalink")

        _document_provider = d.pop("document_provider", UNSET)
        document_provider: PostmortemDocumentsAttachPayloadV1DocumentProvider | Unset
        if isinstance(_document_provider, Unset):
            document_provider = UNSET
        else:
            document_provider = PostmortemDocumentsAttachPayloadV1DocumentProvider(
                _document_provider
            )

        postmortem_documents_attach_payload_v1 = cls(
            incident_id=incident_id,
            permalink=permalink,
            document_provider=document_provider,
        )

        postmortem_documents_attach_payload_v1.additional_properties = d
        return postmortem_documents_attach_payload_v1

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
