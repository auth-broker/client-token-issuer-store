from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaywrightImpersonator")


@_attrs_define
class PlaywrightImpersonator:
    """Automate browser login to capture auth code via OIDC with PKCE. Good For CLIs, but

    Attributes:
        tool (Union[Literal['PLAYWRIGHT'], Unset]):  Default: 'PLAYWRIGHT'.
        browser_channel (Union[Unset, str]):  Default: 'chrome'.
    """

    tool: Union[Literal["PLAYWRIGHT"], Unset] = "PLAYWRIGHT"
    browser_channel: Union[Unset, str] = "chrome"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool = self.tool

        browser_channel = self.browser_channel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tool is not UNSET:
            field_dict["tool"] = tool
        if browser_channel is not UNSET:
            field_dict["browser_channel"] = browser_channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool = cast(Union[Literal["PLAYWRIGHT"], Unset], d.pop("tool", UNSET))
        if tool != "PLAYWRIGHT" and not isinstance(tool, Unset):
            raise ValueError(f"tool must match const 'PLAYWRIGHT', got '{tool}'")

        browser_channel = d.pop("browser_channel", UNSET)

        playwright_impersonator = cls(
            tool=tool,
            browser_channel=browser_channel,
        )

        playwright_impersonator.additional_properties = d
        return playwright_impersonator

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
