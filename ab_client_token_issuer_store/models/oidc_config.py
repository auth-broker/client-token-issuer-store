from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OIDCConfig")


@_attrs_define
class OIDCConfig:
    """
    Attributes:
        client_id (str):
        redirect_uri (str):
        authorize_url (str):
        token_url (str):
        client_secret (Union[None, Unset, str]):
    """

    client_id: str
    redirect_uri: str
    authorize_url: str
    token_url: str
    client_secret: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        redirect_uri = self.redirect_uri

        authorize_url = self.authorize_url

        token_url = self.token_url

        client_secret: Union[None, Unset, str]
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "authorize_url": authorize_url,
                "token_url": token_url,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        redirect_uri = d.pop("redirect_uri")

        authorize_url = d.pop("authorize_url")

        token_url = d.pop("token_url")

        def _parse_client_secret(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        oidc_config = cls(
            client_id=client_id,
            redirect_uri=redirect_uri,
            authorize_url=authorize_url,
            token_url=token_url,
            client_secret=client_secret,
        )

        oidc_config.additional_properties = d
        return oidc_config

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
