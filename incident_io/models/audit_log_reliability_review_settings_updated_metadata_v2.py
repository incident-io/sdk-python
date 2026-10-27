from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogReliabilityReviewSettingsUpdatedMetadataV2")


@_attrs_define(kw_only=True)
class AuditLogReliabilityReviewSettingsUpdatedMetadataV2:
    """
    Example:
        {'added_user_ids': '01FCNDV6P870EA6S7TK1DSYDG0', 'after_automatic_reviews': 'once_per_pull_request',
            'after_draft_reviews': 'skip', 'after_reviewed_authors': 'selected_users', 'before_automatic_reviews':
            'every_push', 'before_draft_reviews': 'review', 'before_reviewed_authors': 'everyone', 'changed':
            'automatic_reviews', 'removed_user_ids': '01FCNDV6P870EA6S7TK1DSYDG1'}

    Attributes:
        changed (str): What the update changed, comma separated (automatic_reviews, draft_reviews, reviewed_authors,
            reviewed_users) Example: automatic_reviews.
        added_user_ids (str | Unset): The users added to those whose pull requests are reviewed, comma separated
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        after_automatic_reviews (str | Unset): Which pushes to a pull request are reviewed after the change (every_push,
            once_per_pull_request) Example: once_per_pull_request.
        after_draft_reviews (str | Unset): Whether draft pull requests are reviewed after the change (review, skip)
            Example: skip.
        after_reviewed_authors (str | Unset): Whose pull requests are reviewed after the change (everyone,
            selected_users) Example: selected_users.
        before_automatic_reviews (str | Unset): Which pushes to a pull request were reviewed before the change
            (every_push, once_per_pull_request) Example: every_push.
        before_draft_reviews (str | Unset): Whether draft pull requests were reviewed before the change (review, skip)
            Example: review.
        before_reviewed_authors (str | Unset): Whose pull requests were reviewed before the change (everyone,
            selected_users) Example: everyone.
        removed_user_ids (str | Unset): The users removed from those whose pull requests are reviewed, comma separated
            Example: 01FCNDV6P870EA6S7TK1DSYDG1.
    """

    changed: str
    added_user_ids: str | Unset = UNSET
    after_automatic_reviews: str | Unset = UNSET
    after_draft_reviews: str | Unset = UNSET
    after_reviewed_authors: str | Unset = UNSET
    before_automatic_reviews: str | Unset = UNSET
    before_draft_reviews: str | Unset = UNSET
    before_reviewed_authors: str | Unset = UNSET
    removed_user_ids: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        added_user_ids = self.added_user_ids

        after_automatic_reviews = self.after_automatic_reviews

        after_draft_reviews = self.after_draft_reviews

        after_reviewed_authors = self.after_reviewed_authors

        before_automatic_reviews = self.before_automatic_reviews

        before_draft_reviews = self.before_draft_reviews

        before_reviewed_authors = self.before_reviewed_authors

        removed_user_ids = self.removed_user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
            }
        )
        if added_user_ids is not UNSET:
            field_dict["added_user_ids"] = added_user_ids
        if after_automatic_reviews is not UNSET:
            field_dict["after_automatic_reviews"] = after_automatic_reviews
        if after_draft_reviews is not UNSET:
            field_dict["after_draft_reviews"] = after_draft_reviews
        if after_reviewed_authors is not UNSET:
            field_dict["after_reviewed_authors"] = after_reviewed_authors
        if before_automatic_reviews is not UNSET:
            field_dict["before_automatic_reviews"] = before_automatic_reviews
        if before_draft_reviews is not UNSET:
            field_dict["before_draft_reviews"] = before_draft_reviews
        if before_reviewed_authors is not UNSET:
            field_dict["before_reviewed_authors"] = before_reviewed_authors
        if removed_user_ids is not UNSET:
            field_dict["removed_user_ids"] = removed_user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed = d.pop("changed")

        added_user_ids = d.pop("added_user_ids", UNSET)

        after_automatic_reviews = d.pop("after_automatic_reviews", UNSET)

        after_draft_reviews = d.pop("after_draft_reviews", UNSET)

        after_reviewed_authors = d.pop("after_reviewed_authors", UNSET)

        before_automatic_reviews = d.pop("before_automatic_reviews", UNSET)

        before_draft_reviews = d.pop("before_draft_reviews", UNSET)

        before_reviewed_authors = d.pop("before_reviewed_authors", UNSET)

        removed_user_ids = d.pop("removed_user_ids", UNSET)

        audit_log_reliability_review_settings_updated_metadata_v2 = cls(
            changed=changed,
            added_user_ids=added_user_ids,
            after_automatic_reviews=after_automatic_reviews,
            after_draft_reviews=after_draft_reviews,
            after_reviewed_authors=after_reviewed_authors,
            before_automatic_reviews=before_automatic_reviews,
            before_draft_reviews=before_draft_reviews,
            before_reviewed_authors=before_reviewed_authors,
            removed_user_ids=removed_user_ids,
        )

        audit_log_reliability_review_settings_updated_metadata_v2.additional_properties = d
        return audit_log_reliability_review_settings_updated_metadata_v2

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
