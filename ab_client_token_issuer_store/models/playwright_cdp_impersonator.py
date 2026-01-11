from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdpgui_service import CDPGUIService
    from ..models.playwright_cdp_impersonator_cdp_headers_type_0 import PlaywrightCDPImpersonatorCdpHeadersType0


T = TypeVar("T", bound="PlaywrightCDPImpersonator")


@_attrs_define
class PlaywrightCDPImpersonator:
    """Automate browser login to capture auth code via OIDC with PKCE. Good For CLIs, but

    Attributes:
        cdp_endpoint (str): CDP endpoint URL, e.g. "wss://your-browserless/chromium?token=..."
        tool (Union[Literal['PLAYWRIGHT_CDP'], Unset]):  Default: 'PLAYWRIGHT_CDP'.
        cdp_headers (Union['PlaywrightCDPImpersonatorCdpHeadersType0', None, Unset]):
        cdp_timeout (Union[None, Unset, float]):
        cdp_gui_service (Union['CDPGUIService', None, Unset]):
    """

    cdp_endpoint: str
    tool: Union[Literal["PLAYWRIGHT_CDP"], Unset] = "PLAYWRIGHT_CDP"
    cdp_headers: Union["PlaywrightCDPImpersonatorCdpHeadersType0", None, Unset] = UNSET
    cdp_timeout: Union[None, Unset, float] = UNSET
    cdp_gui_service: Union["CDPGUIService", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cdpgui_service import CDPGUIService
        from ..models.playwright_cdp_impersonator_cdp_headers_type_0 import PlaywrightCDPImpersonatorCdpHeadersType0

        cdp_endpoint = self.cdp_endpoint

        tool = self.tool

        cdp_headers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cdp_headers, Unset):
            cdp_headers = UNSET
        elif isinstance(self.cdp_headers, PlaywrightCDPImpersonatorCdpHeadersType0):
            cdp_headers = self.cdp_headers.to_dict()
        else:
            cdp_headers = self.cdp_headers

        cdp_timeout: Union[None, Unset, float]
        if isinstance(self.cdp_timeout, Unset):
            cdp_timeout = UNSET
        else:
            cdp_timeout = self.cdp_timeout

        cdp_gui_service: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cdp_gui_service, Unset):
            cdp_gui_service = UNSET
        elif isinstance(self.cdp_gui_service, CDPGUIService):
            cdp_gui_service = self.cdp_gui_service.to_dict()
        else:
            cdp_gui_service = self.cdp_gui_service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cdp_endpoint": cdp_endpoint,
            }
        )
        if tool is not UNSET:
            field_dict["tool"] = tool
        if cdp_headers is not UNSET:
            field_dict["cdp_headers"] = cdp_headers
        if cdp_timeout is not UNSET:
            field_dict["cdp_timeout"] = cdp_timeout
        if cdp_gui_service is not UNSET:
            field_dict["cdp_gui_service"] = cdp_gui_service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdpgui_service import CDPGUIService
        from ..models.playwright_cdp_impersonator_cdp_headers_type_0 import PlaywrightCDPImpersonatorCdpHeadersType0

        d = dict(src_dict)
        cdp_endpoint = d.pop("cdp_endpoint")

        tool = cast(Union[Literal["PLAYWRIGHT_CDP"], Unset], d.pop("tool", UNSET))
        if tool != "PLAYWRIGHT_CDP" and not isinstance(tool, Unset):
            raise ValueError(f"tool must match const 'PLAYWRIGHT_CDP', got '{tool}'")

        def _parse_cdp_headers(data: object) -> Union["PlaywrightCDPImpersonatorCdpHeadersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cdp_headers_type_0 = PlaywrightCDPImpersonatorCdpHeadersType0.from_dict(data)

                return cdp_headers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PlaywrightCDPImpersonatorCdpHeadersType0", None, Unset], data)

        cdp_headers = _parse_cdp_headers(d.pop("cdp_headers", UNSET))

        def _parse_cdp_timeout(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cdp_timeout = _parse_cdp_timeout(d.pop("cdp_timeout", UNSET))

        def _parse_cdp_gui_service(data: object) -> Union["CDPGUIService", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cdp_gui_service_type_0 = CDPGUIService.from_dict(data)

                return cdp_gui_service_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CDPGUIService", None, Unset], data)

        cdp_gui_service = _parse_cdp_gui_service(d.pop("cdp_gui_service", UNSET))

        playwright_cdp_impersonator = cls(
            cdp_endpoint=cdp_endpoint,
            tool=tool,
            cdp_headers=cdp_headers,
            cdp_timeout=cdp_timeout,
            cdp_gui_service=cdp_gui_service,
        )

        playwright_cdp_impersonator.additional_properties = d
        return playwright_cdp_impersonator

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
