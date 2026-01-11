from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impersonation_o_auth_2_flow import ImpersonationOAuth2Flow
    from ..models.pkceo_auth_2_client import PKCEOAuth2Client
    from ..models.template_o_auth_2_flow import TemplateOAuth2Flow


T = TypeVar("T", bound="PKCEOAuth2TokenIssuer")


@_attrs_define
class PKCEOAuth2TokenIssuer:
    """
    Attributes:
        oauth2_flow (Union['ImpersonationOAuth2Flow', 'TemplateOAuth2Flow']):
        oauth2_client (PKCEOAuth2Client):
        identity_provider (Union[Unset, str]):  Default: 'Google'.
        response_type (Union[Unset, str]):  Default: 'code'.
        scope (Union[Unset, str]):  Default: 'openid email profile'.
        type_ (Union[Literal['PKCE'], Unset]):  Default: 'PKCE'.
    """

    oauth2_flow: Union["ImpersonationOAuth2Flow", "TemplateOAuth2Flow"]
    oauth2_client: "PKCEOAuth2Client"
    identity_provider: Union[Unset, str] = "Google"
    response_type: Union[Unset, str] = "code"
    scope: Union[Unset, str] = "openid email profile"
    type_: Union[Literal["PKCE"], Unset] = "PKCE"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.impersonation_o_auth_2_flow import ImpersonationOAuth2Flow

        oauth2_flow: dict[str, Any]
        if isinstance(self.oauth2_flow, ImpersonationOAuth2Flow):
            oauth2_flow = self.oauth2_flow.to_dict()
        else:
            oauth2_flow = self.oauth2_flow.to_dict()

        oauth2_client = self.oauth2_client.to_dict()

        identity_provider = self.identity_provider

        response_type = self.response_type

        scope = self.scope

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oauth2_flow": oauth2_flow,
                "oauth2_client": oauth2_client,
            }
        )
        if identity_provider is not UNSET:
            field_dict["identity_provider"] = identity_provider
        if response_type is not UNSET:
            field_dict["response_type"] = response_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impersonation_o_auth_2_flow import ImpersonationOAuth2Flow
        from ..models.pkceo_auth_2_client import PKCEOAuth2Client
        from ..models.template_o_auth_2_flow import TemplateOAuth2Flow

        d = dict(src_dict)

        def _parse_oauth2_flow(data: object) -> Union["ImpersonationOAuth2Flow", "TemplateOAuth2Flow"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth2_flow_type_0 = ImpersonationOAuth2Flow.from_dict(data)

                return oauth2_flow_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            oauth2_flow_type_1 = TemplateOAuth2Flow.from_dict(data)

            return oauth2_flow_type_1

        oauth2_flow = _parse_oauth2_flow(d.pop("oauth2_flow"))

        oauth2_client = PKCEOAuth2Client.from_dict(d.pop("oauth2_client"))

        identity_provider = d.pop("identity_provider", UNSET)

        response_type = d.pop("response_type", UNSET)

        scope = d.pop("scope", UNSET)

        type_ = cast(Union[Literal["PKCE"], Unset], d.pop("type", UNSET))
        if type_ != "PKCE" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'PKCE', got '{type_}'")

        pkceo_auth_2_token_issuer = cls(
            oauth2_flow=oauth2_flow,
            oauth2_client=oauth2_client,
            identity_provider=identity_provider,
            response_type=response_type,
            scope=scope,
            type_=type_,
        )

        pkceo_auth_2_token_issuer.additional_properties = d
        return pkceo_auth_2_token_issuer

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
