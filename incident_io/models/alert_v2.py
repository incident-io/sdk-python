from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_v2_status import AlertV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attribute_entry_v2 import AlertAttributeEntryV2
    from ..models.alert_tag_v2 import AlertTagV2


T = TypeVar("T", bound="AlertV2")


@_attrs_define(kw_only=True)
class AlertV2:
    """
    Example:
        {'alert_group_ids': ['01GW2G3V0S59R238FAHPDS1R66'], 'alert_source_id': '01GW2G3V0S59R238FAHPDS1R66',
            'attributes': [{'array_value': [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}],
            'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}], 'created_at': '2021-08-17T13:28:57.801578Z',
            'deduplication_key': '4293868629', 'description': 'CPU on the payments service has exceeded 75 percent for 5
            minutes', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'resolved_at': '2021-08-17T14:28:57.801578Z', 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'tags': [{'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}], 'title': '*errors.withMessage: PG::Error failed to connect',
            'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        alert_source_id (str): The ID of the alert source this alert fired on Example: 01GW2G3V0S59R238FAHPDS1R66.
        attributes (list[AlertAttributeEntryV2]): Attribute values parsed from the alerts payload Example:
            [{'array_value': [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}],
            'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}].
        created_at (datetime.datetime): When this entry was created Example: 2021-08-17T13:28:57.801578Z.
        deduplication_key (str): A deduplication key which uniquely references this alert from your alert source. For
            newly created HTTP sources, this field is required.
            If you send an event with the same deduplication_key multiple times, only one alert will be created in
            incident.io for this alert source config.
            You can filter on this field to find the alert created by an event you've sent us. Example: 4293868629.
        id (str): The ID of this alert Example: 01GW2G3V0S59R238FAHPDS1R66.
        status (AlertV2Status): Statuses of an alert Example: firing.
        title (str): The title of the alert, parsed from the alert payload according to the alert source configuration
            Example: *errors.withMessage: PG::Error failed to connect.
        updated_at (datetime.datetime): When this alert was last updated Example: 2021-08-17T13:28:57.801578Z.
        alert_group_ids (list[str] | Unset): The IDs of every alert group this alert belongs to. Empty when the alert is
            not part of any group. Example: ['01GW2G3V0S59R238FAHPDS1R66'].
        description (str | Unset): The description of the alert Example: CPU on the payments service has exceeded 75
            percent for 5 minutes.
        resolved_at (datetime.datetime | Unset): When this alert was resolved Example: 2021-08-17T14:28:57.801578Z.
        source_url (str | Unset): If applicable, a link to the alert in the upstream system Example: https://www.my-
            alerting-platform.com/alerts/my-alert-123.
        tags (list[AlertTagV2] | Unset): Tags someone has applied to this alert Example: [{'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'noisy'}].
    """

    alert_source_id: str
    attributes: list[AlertAttributeEntryV2]
    created_at: datetime.datetime
    deduplication_key: str
    id: str
    status: AlertV2Status
    title: str
    updated_at: datetime.datetime
    alert_group_ids: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    resolved_at: datetime.datetime | Unset = UNSET
    source_url: str | Unset = UNSET
    tags: list[AlertTagV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_source_id = self.alert_source_id

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        created_at = self.created_at.isoformat()

        deduplication_key = self.deduplication_key

        id = self.id

        status = self.status.value

        title = self.title

        updated_at = self.updated_at.isoformat()

        alert_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.alert_group_ids, Unset):
            alert_group_ids = self.alert_group_ids

        description = self.description

        resolved_at: str | Unset = UNSET
        if not isinstance(self.resolved_at, Unset):
            resolved_at = self.resolved_at.isoformat()

        source_url = self.source_url

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_source_id": alert_source_id,
                "attributes": attributes,
                "created_at": created_at,
                "deduplication_key": deduplication_key,
                "id": id,
                "status": status,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if alert_group_ids is not UNSET:
            field_dict["alert_group_ids"] = alert_group_ids
        if description is not UNSET:
            field_dict["description"] = description
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_attribute_entry_v2 import (
            AlertAttributeEntryV2,
        )
        from ..models.alert_tag_v2 import AlertTagV2

        d = dict(src_dict)
        alert_source_id = d.pop("alert_source_id")

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = AlertAttributeEntryV2.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        deduplication_key = d.pop("deduplication_key")

        id = d.pop("id")

        status = AlertV2Status(d.pop("status"))

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alert_group_ids = cast(list[str], d.pop("alert_group_ids", UNSET))

        description = d.pop("description", UNSET)

        _resolved_at = d.pop("resolved_at", UNSET)
        resolved_at: datetime.datetime | Unset
        if isinstance(_resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = datetime.datetime.fromisoformat(_resolved_at)

        source_url = d.pop("source_url", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[AlertTagV2] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = AlertTagV2.from_dict(tags_item_data)

                tags.append(tags_item)

        alert_v2 = cls(
            alert_source_id=alert_source_id,
            attributes=attributes,
            created_at=created_at,
            deduplication_key=deduplication_key,
            id=id,
            status=status,
            title=title,
            updated_at=updated_at,
            alert_group_ids=alert_group_ids,
            description=description,
            resolved_at=resolved_at,
            source_url=source_url,
            tags=tags,
        )

        alert_v2.additional_properties = d
        return alert_v2

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
