from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertNotesUpdatePayloadV1")


@_attrs_define(kw_only=True)
class AlertNotesUpdatePayloadV1:
    """
    Example:
        {'content': 'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-api`.\\n\\n- Error
            rate: ~12% on `/checkout`\\n- Region: `eu-west-1`\\n- See [dashboard](https://grafana.example.com/d/abc)\\n'}

    Attributes:
        content (str): Markdown body of the note Example: Customer reports **checkout 500s** starting ~14:32 UTC.
            Investigating `payments-api`.

            - Error rate: ~12% on `/checkout`
            - Region: `eu-west-1`
            - See [dashboard](https://grafana.example.com/d/abc)
            .
    """

    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content = d.pop("content")

        alert_notes_update_payload_v1 = cls(
            content=content,
        )

        alert_notes_update_payload_v1.additional_properties = d
        return alert_notes_update_payload_v1

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
