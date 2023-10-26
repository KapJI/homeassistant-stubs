from .const import CONF_KEEP_MAIN_LIGHT as CONF_KEEP_MAIN_LIGHT, DEFAULT_KEEP_MAIN_LIGHT as DEFAULT_KEEP_MAIN_LIGHT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import onboarding as onboarding, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any
from wled import Device as Device

class WLEDFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_host: str
    discovered_device: Device
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> WLEDOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _async_get_device(self, host: str) -> Device: ...

class WLEDOptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
