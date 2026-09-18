from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_events_create_http_payload_v2_status import (
    AlertEventsCreateHTTPPayloadV2Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_events_create_http_payload_v2_metadata import (
        AlertEventsCreateHTTPPayloadV2Metadata,
    )


T = TypeVar("T", bound="AlertEventsCreateHTTPPayloadV2")


@_attrs_define
class AlertEventsCreateHTTPPayloadV2:
    """
    Example:
        {'deduplication_key': '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']}, 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage:
            PG::Error failed to connect'}

    Attributes:
        status (AlertEventsCreateHTTPPayloadV2Status): Current status of this alert Example: firing.
        title (str): The title of the alert, parsed from the alert payload according to the alert source configuration
            Example: *errors.withMessage: PG::Error failed to connect.
        deduplication_key (str | Unset): A deduplication key which uniquely references this alert from your alert
            source. For newly created HTTP sources, this field is required.
            If you send an event with the same deduplication_key multiple times, only one alert will be created in
            incident.io for this alert source config.
            You can filter on this field to find the alert created by an event you've sent us. Example: 4293868629.
        description (str | Unset): Description that optionally adds more detail to title. Supports markdown. Example:
            We've detected a number of timeouts on hello.world.com, the service may be down. To fix....
        metadata (AlertEventsCreateHTTPPayloadV2Metadata | Unset): Any additional metadata that you've configured your
            alert source to parse Example: {'service': 'hello.world.com', 'team': ['my-team']}.
        source_url (str | Unset): If applicable, a link to the alert in the upstream system Example: https://www.my-
            alerting-platform.com/alerts/my-alert-123.
    """

    status: AlertEventsCreateHTTPPayloadV2Status
    title: str
    deduplication_key: str | Unset = UNSET
    description: str | Unset = UNSET
    metadata: AlertEventsCreateHTTPPayloadV2Metadata | Unset = UNSET
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        title = self.title

        deduplication_key = self.deduplication_key

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "title": title,
            }
        )
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_events_create_http_payload_v2_metadata import (
            AlertEventsCreateHTTPPayloadV2Metadata,
        )

        d = dict(src_dict)
        status = AlertEventsCreateHTTPPayloadV2Status(d.pop("status"))

        title = d.pop("title")

        deduplication_key = d.pop("deduplication_key", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AlertEventsCreateHTTPPayloadV2Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AlertEventsCreateHTTPPayloadV2Metadata.from_dict(_metadata)

        source_url = d.pop("source_url", UNSET)

        alert_events_create_http_payload_v2 = cls(
            status=status,
            title=title,
            deduplication_key=deduplication_key,
            description=description,
            metadata=metadata,
            source_url=source_url,
        )

        alert_events_create_http_payload_v2.additional_properties = d
        return alert_events_create_http_payload_v2

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
