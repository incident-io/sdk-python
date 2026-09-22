from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v1 import ActorV1
    from ..models.api_key_role_v1 import APIKeyRoleV1
    from ..models.api_key_team_role_v1 import APIKeyTeamRoleV1


T = TypeVar("T", bound="APIKeyV1")


@_attrs_define(kw_only=True)
class APIKeyV1:
    """
    Example:
        {'comments': 'Requested in https://example.slack.com/archives/C123/p456', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'last_used_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'My test API key', 'roles': [{'description': 'can view data, like public
            incidents and organization settings', 'name': 'viewer'}], 'team_ids': ['abc123'], 'team_roles': [{'description':
            'can view data, like public incidents and organization settings', 'name': 'catalog_editor'}],
            'token_last_issued_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the API key was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV1):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        id (str): Unique identifier for this API key Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of the API key, for the user's reference Example: My test API key.
        roles (list[APIKeyRoleV1]): The account-level roles assigned to this API key Example: [{'description': 'can view
            data, like public incidents and organization settings', 'name': 'viewer'}].
        team_ids (list[str]): IDs of teams that this API key is scoped to Example: ['abc123'].
        team_roles (list[APIKeyTeamRoleV1]): The team-level roles assigned to this API key Example: [{'description':
            'can view data, like public incidents and organization settings', 'name': 'catalog_editor'}].
        token_last_issued_at (datetime.datetime): When the current token for this API was last issued. This is the last
            time the token was rotated, or when it was initially created. Older tokens may remain valid for up to an hour
            after they have been rotated, configured when you call the rotate endpoint. Example:
            2021-08-17T13:28:57.801578Z.
        comments (str | Unset): Freeform notes about this API key Example: Requested in
            https://example.slack.com/archives/C123/p456.
        last_used_at (datetime.datetime | Unset): When the key was last used to authenticate a request Example:
            2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    creator: ActorV1
    id: str
    name: str
    roles: list[APIKeyRoleV1]
    team_ids: list[str]
    team_roles: list[APIKeyTeamRoleV1]
    token_last_issued_at: datetime.datetime
    comments: str | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        id = self.id

        name = self.name

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        team_ids = self.team_ids

        team_roles = []
        for team_roles_item_data in self.team_roles:
            team_roles_item = team_roles_item_data.to_dict()
            team_roles.append(team_roles_item)

        token_last_issued_at = self.token_last_issued_at.isoformat()

        comments = self.comments

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "id": id,
                "name": name,
                "roles": roles,
                "team_ids": team_ids,
                "team_roles": team_roles,
                "token_last_issued_at": token_last_issued_at,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.actor_v1 import ActorV1
        from ..models.api_key_role_v1 import APIKeyRoleV1
        from ..models.api_key_team_role_v1 import APIKeyTeamRoleV1

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        creator = ActorV1.from_dict(d.pop("creator"))

        id = d.pop("id")

        name = d.pop("name")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = APIKeyRoleV1.from_dict(roles_item_data)

            roles.append(roles_item)

        team_ids = cast(list[str], d.pop("team_ids"))

        team_roles = []
        _team_roles = d.pop("team_roles")
        for team_roles_item_data in _team_roles:
            team_roles_item = APIKeyTeamRoleV1.from_dict(team_roles_item_data)

            team_roles.append(team_roles_item)

        token_last_issued_at = datetime.datetime.fromisoformat(
            d.pop("token_last_issued_at")
        )

        comments = d.pop("comments", UNSET)

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = datetime.datetime.fromisoformat(_last_used_at)

        api_key_v1 = cls(
            created_at=created_at,
            creator=creator,
            id=id,
            name=name,
            roles=roles,
            team_ids=team_ids,
            team_roles=team_roles,
            token_last_issued_at=token_last_issued_at,
            comments=comments,
            last_used_at=last_used_at,
        )

        api_key_v1.additional_properties = d
        return api_key_v1

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
