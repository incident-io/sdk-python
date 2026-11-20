from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogMobileKeyCreatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogMobileKeyCreatedMetadataV2:
    """
    Example:
        {'device_name': "Bob's iPhone", 'model_name': 'iPhone 15', 'platform': 'ios', 'sign_in_method': 'saml'}

    Attributes:
        platform (str): The device platform, such as ios or android Example: ios.
        sign_in_method (str): How the user signed in: saml, qr_code, email_otp, or sso for a sign-in redirect without
            SAML Example: saml.
        device_name (str | Unset): The name of the device, absent when the app did not send one Example: Bob's iPhone.
        model_name (str | Unset): The model of the device, absent when the app did not send one Example: iPhone 15.
    """

    platform: str
    sign_in_method: str
    device_name: str | Unset = UNSET
    model_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        sign_in_method = self.sign_in_method

        device_name = self.device_name

        model_name = self.model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "sign_in_method": sign_in_method,
            }
        )
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if model_name is not UNSET:
            field_dict["model_name"] = model_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = d.pop("platform")

        sign_in_method = d.pop("sign_in_method")

        device_name = d.pop("device_name", UNSET)

        model_name = d.pop("model_name", UNSET)

        audit_log_mobile_key_created_metadata_v2 = cls(
            platform=platform,
            sign_in_method=sign_in_method,
            device_name=device_name,
            model_name=model_name,
        )

        audit_log_mobile_key_created_metadata_v2.additional_properties = d
        return audit_log_mobile_key_created_metadata_v2

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
