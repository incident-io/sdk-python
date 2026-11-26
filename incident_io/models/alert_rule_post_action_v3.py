from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_rule_post_action_v3_channel_visibility import (
    AlertRulePostActionV3ChannelVisibility,
)
from ..models.alert_rule_post_action_v3_mode import AlertRulePostActionV3Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRulePostActionV3")


@_attrs_define(kw_only=True)
class AlertRulePostActionV3:
    """Post the alert to chat channels

    Example:
        {'channel_visibility': 'public', 'channels': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'mode': 'per_alert'}

    Attributes:
        channels (EngineParamBindingPayloadV3):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        mode (AlertRulePostActionV3Mode): per_alert posts one message per alert. group_summary posts one message for the
            alert's group, and one per alert that is not grouped. Example: per_alert.
        channel_visibility (AlertRulePostActionV3ChannelVisibility | Unset): Whether the channels are public, or one
            private Slack channel entered by its ID. private needs channels to be exactly one literal Slack channel ID, and
            only post_slack supports it. Defaults to public. Example: public.
    """

    channels: EngineParamBindingPayloadV3
    mode: AlertRulePostActionV3Mode
    channel_visibility: AlertRulePostActionV3ChannelVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = self.channels.to_dict()

        mode = self.mode.value

        channel_visibility: str | Unset = UNSET
        if not isinstance(self.channel_visibility, Unset):
            channel_visibility = self.channel_visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channels": channels,
                "mode": mode,
            }
        )
        if channel_visibility is not UNSET:
            field_dict["channel_visibility"] = channel_visibility

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.engine_param_binding_payload_v3 import (
            EngineParamBindingPayloadV3,
        )

        d = dict(src_dict)
        channels = EngineParamBindingPayloadV3.from_dict(d.pop("channels"))

        mode = AlertRulePostActionV3Mode(d.pop("mode"))

        _channel_visibility = d.pop("channel_visibility", UNSET)
        channel_visibility: AlertRulePostActionV3ChannelVisibility | Unset
        if isinstance(_channel_visibility, Unset):
            channel_visibility = UNSET
        else:
            channel_visibility = AlertRulePostActionV3ChannelVisibility(
                _channel_visibility
            )

        alert_rule_post_action_v3 = cls(
            channels=channels,
            mode=mode,
            channel_visibility=channel_visibility,
        )

        alert_rule_post_action_v3.additional_properties = d
        return alert_rule_post_action_v3

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
