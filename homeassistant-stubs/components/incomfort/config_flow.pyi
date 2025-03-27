from .const import CONF_LEGACY_SETPOINT_STATUS as CONF_LEGACY_SETPOINT_STATUS, DOMAIN as DOMAIN
from .coordinator import InComfortConfigEntry as InComfortConfigEntry, async_connect_gateway as async_connect_gateway
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, BooleanSelectorConfig as BooleanSelectorConfig, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any

_LOGGER: Incomplete
TITLE: str
CONFIG_SCHEMA: Incomplete
DHCP_CONFIG_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete

async def async_try_connect_gateway(hass: HomeAssistant, config: dict[str, Any]) -> dict[str, str] | None: ...

class InComfortConfigFlow(ConfigFlow, domain=DOMAIN):
    _discovered_host: str
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: InComfortConfigEntry) -> InComfortOptionsFlowHandler: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_dhcp_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InComfortOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
