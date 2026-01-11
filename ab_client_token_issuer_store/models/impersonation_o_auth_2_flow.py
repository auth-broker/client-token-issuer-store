from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playwright_cdp_browserless_impersonator import PlaywrightCDPBrowserlessImpersonator
    from ..models.playwright_cdp_impersonator import PlaywrightCDPImpersonator
    from ..models.playwright_impersonator import PlaywrightImpersonator
    from ..models.template_impersonator import TemplateImpersonator


T = TypeVar("T", bound="ImpersonationOAuth2Flow")


@_attrs_define
class ImpersonationOAuth2Flow:
    """Automate browser login to capture auth code via OIDC with PKCE.

    Attributes:
        idp_prefix (str):
        impersonator (Union['PlaywrightCDPBrowserlessImpersonator', 'PlaywrightCDPImpersonator',
            'PlaywrightImpersonator', 'TemplateImpersonator']):
        timeout (Union[None, Unset, int]):
        type_ (Union[Literal['IMPERSONATION'], Unset]):  Default: 'IMPERSONATION'.
    """

    idp_prefix: str
    impersonator: Union[
        "PlaywrightCDPBrowserlessImpersonator",
        "PlaywrightCDPImpersonator",
        "PlaywrightImpersonator",
        "TemplateImpersonator",
    ]
    timeout: Union[None, Unset, int] = UNSET
    type_: Union[Literal["IMPERSONATION"], Unset] = "IMPERSONATION"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.playwright_cdp_browserless_impersonator import PlaywrightCDPBrowserlessImpersonator
        from ..models.playwright_cdp_impersonator import PlaywrightCDPImpersonator
        from ..models.playwright_impersonator import PlaywrightImpersonator

        idp_prefix = self.idp_prefix

        impersonator: dict[str, Any]
        if isinstance(self.impersonator, PlaywrightImpersonator):
            impersonator = self.impersonator.to_dict()
        elif isinstance(self.impersonator, PlaywrightCDPImpersonator):
            impersonator = self.impersonator.to_dict()
        elif isinstance(self.impersonator, PlaywrightCDPBrowserlessImpersonator):
            impersonator = self.impersonator.to_dict()
        else:
            impersonator = self.impersonator.to_dict()

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
                "impersonator": impersonator,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playwright_cdp_browserless_impersonator import PlaywrightCDPBrowserlessImpersonator
        from ..models.playwright_cdp_impersonator import PlaywrightCDPImpersonator
        from ..models.playwright_impersonator import PlaywrightImpersonator
        from ..models.template_impersonator import TemplateImpersonator

        d = dict(src_dict)
        idp_prefix = d.pop("idp_prefix")

        def _parse_impersonator(
            data: object,
        ) -> Union[
            "PlaywrightCDPBrowserlessImpersonator",
            "PlaywrightCDPImpersonator",
            "PlaywrightImpersonator",
            "TemplateImpersonator",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impersonator_type_0 = PlaywrightImpersonator.from_dict(data)

                return impersonator_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impersonator_type_1 = PlaywrightCDPImpersonator.from_dict(data)

                return impersonator_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impersonator_type_2 = PlaywrightCDPBrowserlessImpersonator.from_dict(data)

                return impersonator_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            impersonator_type_3 = TemplateImpersonator.from_dict(data)

            return impersonator_type_3

        impersonator = _parse_impersonator(d.pop("impersonator"))

        def _parse_timeout(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        type_ = cast(Union[Literal["IMPERSONATION"], Unset], d.pop("type", UNSET))
        if type_ != "IMPERSONATION" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'IMPERSONATION', got '{type_}'")

        impersonation_o_auth_2_flow = cls(
            idp_prefix=idp_prefix,
            impersonator=impersonator,
            timeout=timeout,
            type_=type_,
        )

        impersonation_o_auth_2_flow.additional_properties = d
        return impersonation_o_auth_2_flow

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
