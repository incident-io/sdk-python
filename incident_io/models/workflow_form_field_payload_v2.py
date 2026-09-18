from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowFormFieldPayloadV2")


@_attrs_define
class WorkflowFormFieldPayloadV2:
    """
    Example:
        {'array': True, 'description': 'The customer affected by this incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'key': 'affected_customer', 'required': True, 'title': 'Affected customer', 'type': 'User'}

    Attributes:
        key (str): The key used to reference this field in the workflow scope Example: affected_customer.
        title (str): Human readable title shown in the form Example: Affected customer.
        type_ (str): The engine resource type of this field Example: User.
        array (bool | Unset): Whether this field holds a list of values rather than a single value Example: True.
        description (str | Unset): Optional help text shown beneath the field Example: The customer affected by this
            incident.
        id (str | Unset): Stable identifier for this field; omit to create a new field Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        required (bool | Unset): Whether this field must be filled in when running the workflow Example: True.
    """

    key: str
    title: str
    type_: str
    array: bool | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        type_ = self.type_

        array = self.array

        description = self.description

        id = self.id

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
                "type": type_,
            }
        )
        if array is not UNSET:
            field_dict["array"] = array
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        type_ = d.pop("type")

        array = d.pop("array", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        required = d.pop("required", UNSET)

        workflow_form_field_payload_v2 = cls(
            key=key,
            title=title,
            type_=type_,
            array=array,
            description=description,
            id=id,
            required=required,
        )

        workflow_form_field_payload_v2.additional_properties = d
        return workflow_form_field_payload_v2

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
