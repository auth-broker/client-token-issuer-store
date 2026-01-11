from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateOAuth2Flow")


@_attrs_define
class TemplateOAuth2Flow:
    """Automate browser login to capture auth code via OIDC with PKCE.

    Attributes:
        idp_prefix (str):
        timeout (Union[None, Unset, int]):
        type_ (Union[Literal['TEMPLATE'], Unset]):  Default: 'TEMPLATE'.
    """

    idp_prefix: str
    timeout: Union[None, Unset, int] = UNSET
    type_: Union[Literal["TEMPLATE"], Unset] = "TEMPLATE"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp_prefix = self.idp_prefix

        timeout: Union[None, Unset, int]
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idp_prefix": idp_prefix,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idp_prefix = d.pop("idp_prefix")

        def _parse_timeout(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        type_ = cast(Union[Literal["TEMPLATE"], Unset], d.pop("type", UNSET))
        if type_ != "TEMPLATE" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'TEMPLATE', got '{type_}'")

        template_o_auth_2_flow = cls(
            idp_prefix=idp_prefix,
            timeout=timeout,
            type_=type_,
        )

        template_o_auth_2_flow.additional_properties = d
        return template_o_auth_2_flow

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
