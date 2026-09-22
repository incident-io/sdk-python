from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_reference_v2 import CatalogEntryReferenceV2


T = TypeVar("T", bound="CatalogEntryEngineParamBindingValueV2")


@_attrs_define(kw_only=True)
class CatalogEntryEngineParamBindingValueV2:
    """
    Example:
        {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'abc123', 'image_url': 'abc123', 'is_image_slack_icon': False,
            'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': 'abc123',
            'unavailable': False, 'value': 'abc123'}

    Attributes:
        label (str): Human readable label to be displayed for user to select Example: Lawrence Jones.
        sort_key (str): This field is deprecated. It will not be present in any responses, and will be removed in a
            future version Example: abc123.
        catalog_entry (CatalogEntryReferenceV2 | Unset):  Example: {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
        helptext (str | Unset): This field is deprecated. It will not be present in any responses, and will be removed
            in a future version Example: abc123.
        image_url (str | Unset): This field is deprecated. It will not be present in any responses, and will be removed
            in a future version Example: abc123.
        is_image_slack_icon (bool | Unset): This field is deprecated. It will not be present in any responses, and will
            be removed in a future version Example: False.
        literal (str | Unset): If set, this is the literal value of the step parameter Example: SEV123.
        reference (str | Unset): This field is deprecated. It will not be present in any responses, and will be removed
            in a future version Example: incident.severity.
        unavailable (bool | Unset): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version Example: False.
        value (str | Unset): This field is deprecated. It will not be present in any responses, and will be removed in a
            future version Example: abc123.
    """

    label: str
    sort_key: str
    catalog_entry: CatalogEntryReferenceV2 | Unset = UNSET
    helptext: str | Unset = UNSET
    image_url: str | Unset = UNSET
    is_image_slack_icon: bool | Unset = UNSET
    literal: str | Unset = UNSET
    reference: str | Unset = UNSET
    unavailable: bool | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        sort_key = self.sort_key

        catalog_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catalog_entry, Unset):
            catalog_entry = self.catalog_entry.to_dict()

        helptext = self.helptext

        image_url = self.image_url

        is_image_slack_icon = self.is_image_slack_icon

        literal = self.literal

        reference = self.reference

        unavailable = self.unavailable

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sort_key": sort_key,
            }
        )
        if catalog_entry is not UNSET:
            field_dict["catalog_entry"] = catalog_entry
        if helptext is not UNSET:
            field_dict["helptext"] = helptext
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if is_image_slack_icon is not UNSET:
            field_dict["is_image_slack_icon"] = is_image_slack_icon
        if literal is not UNSET:
            field_dict["literal"] = literal
        if reference is not UNSET:
            field_dict["reference"] = reference
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_entry_reference_v2 import (
            CatalogEntryReferenceV2,
        )

        d = dict(src_dict)
        label = d.pop("label")

        sort_key = d.pop("sort_key")

        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: CatalogEntryReferenceV2 | Unset
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = CatalogEntryReferenceV2.from_dict(_catalog_entry)

        helptext = d.pop("helptext", UNSET)

        image_url = d.pop("image_url", UNSET)

        is_image_slack_icon = d.pop("is_image_slack_icon", UNSET)

        literal = d.pop("literal", UNSET)

        reference = d.pop("reference", UNSET)

        unavailable = d.pop("unavailable", UNSET)

        value = d.pop("value", UNSET)

        catalog_entry_engine_param_binding_value_v2 = cls(
            label=label,
            sort_key=sort_key,
            catalog_entry=catalog_entry,
            helptext=helptext,
            image_url=image_url,
            is_image_slack_icon=is_image_slack_icon,
            literal=literal,
            reference=reference,
            unavailable=unavailable,
            value=value,
        )

        catalog_entry_engine_param_binding_value_v2.additional_properties = d
        return catalog_entry_engine_param_binding_value_v2

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
