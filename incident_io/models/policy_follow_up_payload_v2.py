from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.policy_due_date_config_payload_v2 import PolicyDueDateConfigPayloadV2


T = TypeVar("T", bound="PolicyFollowUpPayloadV2")


@_attrs_define
class PolicyFollowUpPayloadV2:
    """Set when policy_type is follow_up.

    Example:
        {'due_date_config': {'applies_from': '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London',
            'calculation_type': 'weekdays', 'days': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'requirements': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'run_on_private_incidents': False}

    Attributes:
        requirements (list[ConditionGroupPayloadV2]): Conditions a follow-up must satisfy to be compliant, e.g. 'is
            exported to Jira' Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        due_date_config (PolicyDueDateConfigPayloadV2 | Unset):  Example: {'applies_from':
            '2021-08-17T13:28:57.801578Z', 'calculation_timezone': 'Europe/London', 'calculation_type': 'weekdays', 'days':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        run_on_private_incidents (bool | Unset): Requires the policies.run_on_private scope Example: False.
    """

    requirements: list[ConditionGroupPayloadV2]
    due_date_config: PolicyDueDateConfigPayloadV2 | Unset = UNSET
    run_on_private_incidents: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requirements = []
        for requirements_item_data in self.requirements:
            requirements_item = requirements_item_data.to_dict()
            requirements.append(requirements_item)

        due_date_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.due_date_config, Unset):
            due_date_config = self.due_date_config.to_dict()

        run_on_private_incidents = self.run_on_private_incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requirements": requirements,
            }
        )
        if due_date_config is not UNSET:
            field_dict["due_date_config"] = due_date_config
        if run_on_private_incidents is not UNSET:
            field_dict["run_on_private_incidents"] = run_on_private_incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.condition_group_payload_v2 import (
            ConditionGroupPayloadV2,
        )
        from ..models.policy_due_date_config_payload_v2 import (
            PolicyDueDateConfigPayloadV2,
        )

        d = dict(src_dict)
        requirements = []
        _requirements = d.pop("requirements")
        for requirements_item_data in _requirements:
            requirements_item = ConditionGroupPayloadV2.from_dict(
                requirements_item_data
            )

            requirements.append(requirements_item)

        _due_date_config = d.pop("due_date_config", UNSET)
        due_date_config: PolicyDueDateConfigPayloadV2 | Unset
        if isinstance(_due_date_config, Unset):
            due_date_config = UNSET
        else:
            due_date_config = PolicyDueDateConfigPayloadV2.from_dict(_due_date_config)

        run_on_private_incidents = d.pop("run_on_private_incidents", UNSET)

        policy_follow_up_payload_v2 = cls(
            requirements=requirements,
            due_date_config=due_date_config,
            run_on_private_incidents=run_on_private_incidents,
        )

        policy_follow_up_payload_v2.additional_properties = d
        return policy_follow_up_payload_v2

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
