from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageV1")


@_attrs_define(kw_only=True)
class ImageV1:
    """
    Example:
        {'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'url': 'https://storage.googleapis.com/incident-io/images/...'}

    Attributes:
        id (str): Unique identifier for the image Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        url (str): Pre-signed URL to fetch the image, valid for 10 minutes Example:
            https://storage.googleapis.com/incident-io/images/....
    """

    id: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        image_v1 = cls(
            id=id,
            url=url,
        )

        image_v1.additional_properties = d
        return image_v1

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
