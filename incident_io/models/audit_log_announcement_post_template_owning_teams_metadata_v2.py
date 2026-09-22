from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogAnnouncementPostTemplateOwningTeamsMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogAnnouncementPostTemplateOwningTeamsMetadataV2:
    """
    Example:
        {'after_owning_team_ids': '01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG2', 'before_owning_team_ids':
            '01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG1'}

    Attributes:
        after_owning_team_ids (str): Catalog entry IDs of the owning teams after the change, comma separated Example:
            01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG2.
        before_owning_team_ids (str): Catalog entry IDs of the owning teams before the change, comma separated Example:
            01FCNDV6P870EA6S7TK1DSYDG0,01FCNDV6P870EA6S7TK1DSYDG1.
    """

    after_owning_team_ids: str
    before_owning_team_ids: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_owning_team_ids = self.after_owning_team_ids

        before_owning_team_ids = self.before_owning_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_owning_team_ids": after_owning_team_ids,
                "before_owning_team_ids": before_owning_team_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_owning_team_ids = d.pop("after_owning_team_ids")

        before_owning_team_ids = d.pop("before_owning_team_ids")

        audit_log_announcement_post_template_owning_teams_metadata_v2 = cls(
            after_owning_team_ids=after_owning_team_ids,
            before_owning_team_ids=before_owning_team_ids,
        )

        audit_log_announcement_post_template_owning_teams_metadata_v2.additional_properties = d
        return audit_log_announcement_post_template_owning_teams_metadata_v2

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
