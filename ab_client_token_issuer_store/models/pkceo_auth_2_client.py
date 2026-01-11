from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_config import OIDCConfig


T = TypeVar("T", bound="PKCEOAuth2Client")


@_attrs_define
class PKCEOAuth2Client:
    """
    Attributes:
        config (OIDCConfig):
        type_ (Union[Literal['PKCE'], Unset]):  Default: 'PKCE'.
    """

    config: "OIDCConfig"
    type_: Union[Literal["PKCE"], Unset] = "PKCE"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_config import OIDCConfig

        d = dict(src_dict)
        config = OIDCConfig.from_dict(d.pop("config"))

        type_ = cast(Union[Literal["PKCE"], Unset], d.pop("type", UNSET))
        if type_ != "PKCE" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'PKCE', got '{type_}'")

        pkceo_auth_2_client = cls(
            config=config,
            type_=type_,
        )

        pkceo_auth_2_client.additional_properties = d
        return pkceo_auth_2_client

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
