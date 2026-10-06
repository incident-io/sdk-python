from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_form_lifecycle_element_v3_element_type import (
    IncidentFormLifecycleElementV3ElementType,
)
from ..models.incident_form_lifecycle_element_v3_required_if import (
    IncidentFormLifecycleElementV3RequiredIf,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_v3 import ConditionGroupV3
    from ..models.engine_param_binding_v3 import EngineParamBindingV3
    from ..models.incident_form_lifecycle_element_config_v3 import (
        IncidentFormLifecycleElementConfigV3,
    )


T = TypeVar("T", bound="IncidentFormLifecycleElementV3")


@_attrs_define(kw_only=True)
class IncidentFormLifecycleElementV3:
    """
    Example:
        {'can_select_no_value': False, 'config': {'require_comment': False}, 'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'default_value': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'description': 'Shown
            when the incident is major or above.', 'element_type': 'name', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_role_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'placeholder': "What's happening?", 'required_if': 'check_engine_config', 'required_if_condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference':
            'alert.priority'}}]}], 'show_if_condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}]}

    Attributes:
        element_type (IncidentFormLifecycleElementV3ElementType): What this element captures Example: name.
        can_select_no_value (bool | Unset): Whether the user can explicitly choose no value. Only meaningful for custom
            field elements. Example: False.
        config (IncidentFormLifecycleElementConfigV3 | Unset):  Example: {'require_comment': False}.
        custom_field_id (str | Unset): The custom field this element edits. Set only when element_type is custom_field.
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        default_value (EngineParamBindingV3 | Unset):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        description (str | Unset): Description shown beside this element, as markdown Example: Shown when the incident
            is major or above..
        id (str | Unset): Unique identifier for this element. divider and text elements are matched on this, because
            they have no natural key. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_role_id (str | Unset): The incident role this element assigns. Set only when element_type is
            incident_role. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_timestamp_id (str | Unset): The incident timestamp this element sets. Set only when element_type is
            timestamp. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        placeholder (str | Unset): Placeholder text shown in the empty field Example: What's happening?.
        required_if (IncidentFormLifecycleElementV3RequiredIf | Unset): When this element must be filled in Example:
            check_engine_config.
        required_if_condition_groups (list[ConditionGroupV3] | Unset): Condition groups that make this element required.
            Used when required_if is check_engine_config. Example: [{'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}].
        show_if_condition_groups (list[ConditionGroupV3] | Unset): The element is shown when any of these condition
            groups match. Unset means it is always shown. Example: [{'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}].
    """

    element_type: IncidentFormLifecycleElementV3ElementType
    can_select_no_value: bool | Unset = UNSET
    config: IncidentFormLifecycleElementConfigV3 | Unset = UNSET
    custom_field_id: str | Unset = UNSET
    default_value: EngineParamBindingV3 | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    incident_role_id: str | Unset = UNSET
    incident_timestamp_id: str | Unset = UNSET
    placeholder: str | Unset = UNSET
    required_if: IncidentFormLifecycleElementV3RequiredIf | Unset = UNSET
    required_if_condition_groups: list[ConditionGroupV3] | Unset = UNSET
    show_if_condition_groups: list[ConditionGroupV3] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_type = self.element_type.value

        can_select_no_value = self.can_select_no_value

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        custom_field_id = self.custom_field_id

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        description = self.description

        id = self.id

        incident_role_id = self.incident_role_id

        incident_timestamp_id = self.incident_timestamp_id

        placeholder = self.placeholder

        required_if: str | Unset = UNSET
        if not isinstance(self.required_if, Unset):
            required_if = self.required_if.value

        required_if_condition_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.required_if_condition_groups, Unset):
            required_if_condition_groups = []
            for (
                required_if_condition_groups_item_data
            ) in self.required_if_condition_groups:
                required_if_condition_groups_item = (
                    required_if_condition_groups_item_data.to_dict()
                )
                required_if_condition_groups.append(required_if_condition_groups_item)

        show_if_condition_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.show_if_condition_groups, Unset):
            show_if_condition_groups = []
            for show_if_condition_groups_item_data in self.show_if_condition_groups:
                show_if_condition_groups_item = (
                    show_if_condition_groups_item_data.to_dict()
                )
                show_if_condition_groups.append(show_if_condition_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_type": element_type,
            }
        )
        if can_select_no_value is not UNSET:
            field_dict["can_select_no_value"] = can_select_no_value
        if config is not UNSET:
            field_dict["config"] = config
        if custom_field_id is not UNSET:
            field_dict["custom_field_id"] = custom_field_id
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if incident_timestamp_id is not UNSET:
            field_dict["incident_timestamp_id"] = incident_timestamp_id
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if required_if is not UNSET:
            field_dict["required_if"] = required_if
        if required_if_condition_groups is not UNSET:
            field_dict["required_if_condition_groups"] = required_if_condition_groups
        if show_if_condition_groups is not UNSET:
            field_dict["show_if_condition_groups"] = show_if_condition_groups

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_v3 import ConditionGroupV3
        from ..models.engine_param_binding_v3 import (
            EngineParamBindingV3,
        )
        from ..models.incident_form_lifecycle_element_config_v3 import (
            IncidentFormLifecycleElementConfigV3,
        )

        d = dict(src_dict)
        element_type = IncidentFormLifecycleElementV3ElementType(d.pop("element_type"))

        can_select_no_value = d.pop("can_select_no_value", UNSET)

        _config = d.pop("config", UNSET)
        config: IncidentFormLifecycleElementConfigV3 | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = IncidentFormLifecycleElementConfigV3.from_dict(_config)

        custom_field_id = d.pop("custom_field_id", UNSET)

        _default_value = d.pop("default_value", UNSET)
        default_value: EngineParamBindingV3 | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = EngineParamBindingV3.from_dict(_default_value)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        incident_role_id = d.pop("incident_role_id", UNSET)

        incident_timestamp_id = d.pop("incident_timestamp_id", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        _required_if = d.pop("required_if", UNSET)
        required_if: IncidentFormLifecycleElementV3RequiredIf | Unset
        if isinstance(_required_if, Unset):
            required_if = UNSET
        else:
            required_if = IncidentFormLifecycleElementV3RequiredIf(_required_if)

        _required_if_condition_groups = d.pop("required_if_condition_groups", UNSET)
        required_if_condition_groups: list[ConditionGroupV3] | Unset = UNSET
        if _required_if_condition_groups is not UNSET:
            required_if_condition_groups = []
            for required_if_condition_groups_item_data in _required_if_condition_groups:
                required_if_condition_groups_item = ConditionGroupV3.from_dict(
                    required_if_condition_groups_item_data
                )

                required_if_condition_groups.append(required_if_condition_groups_item)

        _show_if_condition_groups = d.pop("show_if_condition_groups", UNSET)
        show_if_condition_groups: list[ConditionGroupV3] | Unset = UNSET
        if _show_if_condition_groups is not UNSET:
            show_if_condition_groups = []
            for show_if_condition_groups_item_data in _show_if_condition_groups:
                show_if_condition_groups_item = ConditionGroupV3.from_dict(
                    show_if_condition_groups_item_data
                )

                show_if_condition_groups.append(show_if_condition_groups_item)

        incident_form_lifecycle_element_v3 = cls(
            element_type=element_type,
            can_select_no_value=can_select_no_value,
            config=config,
            custom_field_id=custom_field_id,
            default_value=default_value,
            description=description,
            id=id,
            incident_role_id=incident_role_id,
            incident_timestamp_id=incident_timestamp_id,
            placeholder=placeholder,
            required_if=required_if,
            required_if_condition_groups=required_if_condition_groups,
            show_if_condition_groups=show_if_condition_groups,
        )

        incident_form_lifecycle_element_v3.additional_properties = d
        return incident_form_lifecycle_element_v3

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
