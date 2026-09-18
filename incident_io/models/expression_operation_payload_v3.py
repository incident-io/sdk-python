from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expression_operation_payload_v3_operation_type import (
    ExpressionOperationPayloadV3OperationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_branches_opts_payload_v3 import (
        ExpressionBranchesOptsPayloadV3,
    )
    from ..models.expression_cast_opts_payload_v3 import ExpressionCastOptsPayloadV3
    from ..models.expression_concatenate_opts_payload_v3 import (
        ExpressionConcatenateOptsPayloadV3,
    )
    from ..models.expression_filter_opts_payload_v3 import ExpressionFilterOptsPayloadV3
    from ..models.expression_navigate_opts_payload_v3 import (
        ExpressionNavigateOptsPayloadV3,
    )
    from ..models.expression_parse_opts_payload_v3 import ExpressionParseOptsPayloadV3


T = TypeVar("T", bound="ExpressionOperationPayloadV3")


@_attrs_define
class ExpressionOperationPayloadV3:
    """
    Example:
        {'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'concatenate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}

    Attributes:
        operation_type (ExpressionOperationPayloadV3OperationType): The type of the operation Example: navigate.
        branches (ExpressionBranchesOptsPayloadV3 | Unset):  Example: {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'alert.priority'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}.
        cast (ExpressionCastOptsPayloadV3 | Unset):  Example: {'returns': {'array': True, 'type': 'IncidentStatus'}}.
        concatenate (ExpressionConcatenateOptsPayloadV3 | Unset):  Example: {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}.
        filter_ (ExpressionFilterOptsPayloadV3 | Unset):  Example: {'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'alert.priority'}]}]}.
        navigate (ExpressionNavigateOptsPayloadV3 | Unset):  Example: {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}.
        parse (ExpressionParseOptsPayloadV3 | Unset):  Example: {'returns': {'array': True, 'type': 'IncidentStatus'},
            'source': 'metadata.annotations["github.com/repo"]'}.
    """

    operation_type: ExpressionOperationPayloadV3OperationType
    branches: ExpressionBranchesOptsPayloadV3 | Unset = UNSET
    cast: ExpressionCastOptsPayloadV3 | Unset = UNSET
    concatenate: ExpressionConcatenateOptsPayloadV3 | Unset = UNSET
    filter_: ExpressionFilterOptsPayloadV3 | Unset = UNSET
    navigate: ExpressionNavigateOptsPayloadV3 | Unset = UNSET
    parse: ExpressionParseOptsPayloadV3 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_type = self.operation_type.value

        branches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        cast: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cast, Unset):
            cast = self.cast.to_dict()

        concatenate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.concatenate, Unset):
            concatenate = self.concatenate.to_dict()

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        navigate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.navigate, Unset):
            navigate = self.navigate.to_dict()

        parse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parse, Unset):
            parse = self.parse.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_type": operation_type,
            }
        )
        if branches is not UNSET:
            field_dict["branches"] = branches
        if cast is not UNSET:
            field_dict["cast"] = cast
        if concatenate is not UNSET:
            field_dict["concatenate"] = concatenate
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if navigate is not UNSET:
            field_dict["navigate"] = navigate
        if parse is not UNSET:
            field_dict["parse"] = parse

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.expression_branches_opts_payload_v3 import (
            ExpressionBranchesOptsPayloadV3,
        )
        from ..models.expression_cast_opts_payload_v3 import (
            ExpressionCastOptsPayloadV3,
        )
        from ..models.expression_concatenate_opts_payload_v3 import (
            ExpressionConcatenateOptsPayloadV3,
        )
        from ..models.expression_filter_opts_payload_v3 import (
            ExpressionFilterOptsPayloadV3,
        )
        from ..models.expression_navigate_opts_payload_v3 import (
            ExpressionNavigateOptsPayloadV3,
        )
        from ..models.expression_parse_opts_payload_v3 import (
            ExpressionParseOptsPayloadV3,
        )

        d = dict(src_dict)
        operation_type = ExpressionOperationPayloadV3OperationType(
            d.pop("operation_type")
        )

        _branches = d.pop("branches", UNSET)
        branches: ExpressionBranchesOptsPayloadV3 | Unset
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = ExpressionBranchesOptsPayloadV3.from_dict(_branches)

        _cast = d.pop("cast", UNSET)
        cast: ExpressionCastOptsPayloadV3 | Unset
        if isinstance(_cast, Unset):
            cast = UNSET
        else:
            cast = ExpressionCastOptsPayloadV3.from_dict(_cast)

        _concatenate = d.pop("concatenate", UNSET)
        concatenate: ExpressionConcatenateOptsPayloadV3 | Unset
        if isinstance(_concatenate, Unset):
            concatenate = UNSET
        else:
            concatenate = ExpressionConcatenateOptsPayloadV3.from_dict(_concatenate)

        _filter_ = d.pop("filter", UNSET)
        filter_: ExpressionFilterOptsPayloadV3 | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ExpressionFilterOptsPayloadV3.from_dict(_filter_)

        _navigate = d.pop("navigate", UNSET)
        navigate: ExpressionNavigateOptsPayloadV3 | Unset
        if isinstance(_navigate, Unset):
            navigate = UNSET
        else:
            navigate = ExpressionNavigateOptsPayloadV3.from_dict(_navigate)

        _parse = d.pop("parse", UNSET)
        parse: ExpressionParseOptsPayloadV3 | Unset
        if isinstance(_parse, Unset):
            parse = UNSET
        else:
            parse = ExpressionParseOptsPayloadV3.from_dict(_parse)

        expression_operation_payload_v3 = cls(
            operation_type=operation_type,
            branches=branches,
            cast=cast,
            concatenate=concatenate,
            filter_=filter_,
            navigate=navigate,
            parse=parse,
        )

        expression_operation_payload_v3.additional_properties = d
        return expression_operation_payload_v3

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
