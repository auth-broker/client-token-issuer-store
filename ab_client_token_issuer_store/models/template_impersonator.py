from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateImpersonator")


@_attrs_define
class TemplateImpersonator:
    """Automate browser login to capture auth code via OIDC with PKCE.

    Attributes:
        tool (Union[Literal['TEMPLATE'], Unset]):  Default: 'TEMPLATE'.
    """

    tool: Union[Literal["TEMPLATE"], Unset] = "TEMPLATE"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool = self.tool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tool is not UNSET:
            field_dict["tool"] = tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool = cast(Union[Literal["TEMPLATE"], Unset], d.pop("tool", UNSET))
        if tool != "TEMPLATE" and not isinstance(tool, Unset):
            raise ValueError(f"tool must match const 'TEMPLATE', got '{tool}'")

        template_impersonator = cls(
            tool=tool,
        )

        template_impersonator.additional_properties = d
        return template_impersonator

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
