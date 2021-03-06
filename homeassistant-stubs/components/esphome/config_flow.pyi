from . import DOMAIN as DOMAIN, DomainData as DomainData
from aioesphomeapi import DeviceInfo as DeviceInfo
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

class EsphomeFlowHandler(ConfigFlow):
    VERSION: int
    _host: Any
    _port: Any
    _password: Any
    def __init__(self) -> None: ...
    async def _async_step_user_base(self, user_input: Union[dict[str, Any], None] = ..., error: Union[str, None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @property
    def _name(self) -> Union[str, None]: ...
    @_name.setter
    def _name(self, value: str) -> None: ...
    def _set_user_input(self, user_input: Union[dict[str, Any], None]) -> None: ...
    async def _async_authenticate_or_add(self, user_input: Union[dict[str, Any], None]) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    def _async_get_entry(self) -> FlowResult: ...
    async def async_step_authenticate(self, user_input: Union[dict[str, Any], None] = ..., error: Union[str, None] = ...) -> FlowResult: ...
    async def fetch_device_info(self) -> tuple[Union[str, None], Union[DeviceInfo, None]]: ...
    async def try_login(self) -> Union[str, None]: ...
