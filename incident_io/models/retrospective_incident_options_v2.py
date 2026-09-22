from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrospectiveIncidentOptionsV2")


@_attrs_define(kw_only=True)
class RetrospectiveIncidentOptionsV2:
    """
    Example:
        {'external_id': 123, 'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'slack_channel_id':
            'abc123'}

    Attributes:
        external_id (int | Unset): The external ID (e.g. the 123 in INC-123) to assign to the incident. This can be
            useful when importing incidents. If you want to use this field, you'll need to talk to us first. Example: 123.
        postmortem_document_url (str | Unset): The URL of the postmortem, if there is one Example:
            https://docs.google.com/my_doc_id.
        slack_channel_id (str | Unset): Pass the ID of a Slack channel to attach the incident to an existing channel. If
            not provided, no Slack channel will be created for this retrospective incident. Example: abc123.
    """

    external_id: int | Unset = UNSET
    postmortem_document_url: str | Unset = UNSET
    slack_channel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        postmortem_document_url = self.postmortem_document_url

        slack_channel_id = self.slack_channel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        external_id = d.pop("external_id", UNSET)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        slack_channel_id = d.pop("slack_channel_id", UNSET)

        retrospective_incident_options_v2 = cls(
            external_id=external_id,
            postmortem_document_url=postmortem_document_url,
            slack_channel_id=slack_channel_id,
        )

        retrospective_incident_options_v2.additional_properties = d
        return retrospective_incident_options_v2

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
