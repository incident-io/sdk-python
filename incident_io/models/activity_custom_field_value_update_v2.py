from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.custom_field_type_info_v2 import CustomFieldTypeInfoV2
    from ..models.custom_field_value_v2 import CustomFieldValueV2


T = TypeVar("T", bound="ActivityCustomFieldValueUpdateV2")


@_attrs_define(kw_only=True)
class ActivityCustomFieldValueUpdateV2:
    """
    Example:
        {'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'new_values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}], 'new_values_count': 4, 'previous_values':
            [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}], 'previous_values_count': 3, 'updater': {'alert':
            {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}}

    Attributes:
        custom_field (CustomFieldTypeInfoV2 | Unset):  Example: {'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}]}.
        new_values (list[CustomFieldValueV2] | Unset): Values after the change, up to 100 of them Example:
            [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}].
        new_values_count (int | Unset): How many values there are now, which can exceed the array above Example: 4.
        previous_values (list[CustomFieldValueV2] | Unset): Values before the change, up to 100 of them Example:
            [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}].
        previous_values_count (int | Unset): How many values there were before, which can exceed the array above
            Example: 3.
        updater (ActorV2 | Unset):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    custom_field: CustomFieldTypeInfoV2 | Unset = UNSET
    new_values: list[CustomFieldValueV2] | Unset = UNSET
    new_values_count: int | Unset = UNSET
    previous_values: list[CustomFieldValueV2] | Unset = UNSET
    previous_values_count: int | Unset = UNSET
    updater: ActorV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        new_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.new_values, Unset):
            new_values = []
            for new_values_item_data in self.new_values:
                new_values_item = new_values_item_data.to_dict()
                new_values.append(new_values_item)

        new_values_count = self.new_values_count

        previous_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.previous_values, Unset):
            previous_values = []
            for previous_values_item_data in self.previous_values:
                previous_values_item = previous_values_item_data.to_dict()
                previous_values.append(previous_values_item)

        previous_values_count = self.previous_values_count

        updater: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_field is not UNSET:
            field_dict["custom_field"] = custom_field
        if new_values is not UNSET:
            field_dict["new_values"] = new_values
        if new_values_count is not UNSET:
            field_dict["new_values_count"] = new_values_count
        if previous_values is not UNSET:
            field_dict["previous_values"] = previous_values
        if previous_values_count is not UNSET:
            field_dict["previous_values_count"] = previous_values_count
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v2 import ActorV2
        from ..models.custom_field_type_info_v2 import (
            CustomFieldTypeInfoV2,
        )
        from ..models.custom_field_value_v2 import CustomFieldValueV2

        d = dict(src_dict)
        _custom_field = d.pop("custom_field", UNSET)
        custom_field: CustomFieldTypeInfoV2 | Unset
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = CustomFieldTypeInfoV2.from_dict(_custom_field)

        _new_values = d.pop("new_values", UNSET)
        new_values: list[CustomFieldValueV2] | Unset = UNSET
        if _new_values is not UNSET:
            new_values = []
            for new_values_item_data in _new_values:
                new_values_item = CustomFieldValueV2.from_dict(new_values_item_data)

                new_values.append(new_values_item)

        new_values_count = d.pop("new_values_count", UNSET)

        _previous_values = d.pop("previous_values", UNSET)
        previous_values: list[CustomFieldValueV2] | Unset = UNSET
        if _previous_values is not UNSET:
            previous_values = []
            for previous_values_item_data in _previous_values:
                previous_values_item = CustomFieldValueV2.from_dict(
                    previous_values_item_data
                )

                previous_values.append(previous_values_item)

        previous_values_count = d.pop("previous_values_count", UNSET)

        _updater = d.pop("updater", UNSET)
        updater: ActorV2 | Unset
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_custom_field_value_update_v2 = cls(
            custom_field=custom_field,
            new_values=new_values,
            new_values_count=new_values_count,
            previous_values=previous_values,
            previous_values_count=previous_values_count,
            updater=updater,
        )

        activity_custom_field_value_update_v2.additional_properties = d
        return activity_custom_field_value_update_v2

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
