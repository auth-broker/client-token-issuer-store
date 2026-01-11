from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.o_auth_2_token_issuer import OAuth2TokenIssuer
    from ..models.pkceo_auth_2_token_issuer import PKCEOAuth2TokenIssuer
    from ..models.template_token_issuer import TemplateTokenIssuer


T = TypeVar("T", bound="CreateTokenIssuerRequest")


@_attrs_define
class CreateTokenIssuerRequest:
    """
    Attributes:
        created_by (UUID):
        name (str):
        token_issuer (Union['OAuth2TokenIssuer', 'PKCEOAuth2TokenIssuer', 'TemplateTokenIssuer']):
    """

    created_by: UUID
    name: str
    token_issuer: Union["OAuth2TokenIssuer", "PKCEOAuth2TokenIssuer", "TemplateTokenIssuer"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.o_auth_2_token_issuer import OAuth2TokenIssuer
        from ..models.pkceo_auth_2_token_issuer import PKCEOAuth2TokenIssuer

        created_by = str(self.created_by)

        name = self.name

        token_issuer: dict[str, Any]
        if isinstance(self.token_issuer, PKCEOAuth2TokenIssuer):
            token_issuer = self.token_issuer.to_dict()
        elif isinstance(self.token_issuer, OAuth2TokenIssuer):
            token_issuer = self.token_issuer.to_dict()
        else:
            token_issuer = self.token_issuer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "name": name,
                "token_issuer": token_issuer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_token_issuer import OAuth2TokenIssuer
        from ..models.pkceo_auth_2_token_issuer import PKCEOAuth2TokenIssuer
        from ..models.template_token_issuer import TemplateTokenIssuer

        d = dict(src_dict)
        created_by = UUID(d.pop("created_by"))

        name = d.pop("name")

        def _parse_token_issuer(
            data: object,
        ) -> Union["OAuth2TokenIssuer", "PKCEOAuth2TokenIssuer", "TemplateTokenIssuer"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                token_issuer_type_0 = PKCEOAuth2TokenIssuer.from_dict(data)

                return token_issuer_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                token_issuer_type_1 = OAuth2TokenIssuer.from_dict(data)

                return token_issuer_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            token_issuer_type_2 = TemplateTokenIssuer.from_dict(data)

            return token_issuer_type_2

        token_issuer = _parse_token_issuer(d.pop("token_issuer"))

        create_token_issuer_request = cls(
            created_by=created_by,
            name=name,
            token_issuer=token_issuer,
        )

        create_token_issuer_request.additional_properties = d
        return create_token_issuer_request

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
