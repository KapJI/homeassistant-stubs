import voluptuous as vol
from .const import CONF_BROWSE_LIMIT as CONF_BROWSE_LIMIT, CONF_HTTPS as CONF_HTTPS, CONF_VOLUME_STEP as CONF_VOLUME_STEP, DEFAULT_BROWSE_LIMIT as DEFAULT_BROWSE_LIMIT, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_VOLUME_STEP as DEFAULT_VOLUME_STEP, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any

_LOGGER: Incomplete
TIMEOUT: int

def _base_schema(discovery_info: dict[str, Any] | None = None) -> vol.Schema: ...

class SqueezeboxConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    discovery_info: dict[str, Any] | None
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...
    async def _discover(self, uuid: str | None = None) -> None: ...
    async def _validate_input(self, data: dict[str, Any]) -> str | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_edit(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...

OPTIONS_SCHEMA: Incomplete

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
