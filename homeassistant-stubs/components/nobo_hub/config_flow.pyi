from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import CONF_OVERRIDE_TYPE as CONF_OVERRIDE_TYPE, CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN, OVERRIDE_TYPE_CONSTANT as OVERRIDE_TYPE_CONSTANT, OVERRIDE_TYPE_NOW as OVERRIDE_TYPE_NOW, SERIAL_LENGTH as SERIAL_LENGTH, SERIAL_PREFIX_LENGTH as SERIAL_PREFIX_LENGTH
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_MAC as CONF_MAC
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any, override

DATA_NOBO_HUB_IMPL: str
DEVICE_INPUT: str

class NoboHubConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _discovered_hubs: dict[str, Any] | None
    _hub: str | None
    _mac: str | None
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_selected(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_manual(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _create_configuration(self, serial: str, ip_address: str) -> ConfigFlowResult: ...
    async def _test_connection(self, serial: str, ip_address: str) -> str: ...
    @staticmethod
    def _format_hub(ip: str, serial_prefix: str) -> str: ...
    def _hubs(self) -> dict[str, str]: ...
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: NoboHubConfigEntry) -> OptionsFlowHandler: ...

class NoboHubConnectError(HomeAssistantError):
    msg: Incomplete
    def __init__(self, msg: str) -> None: ...

class OptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
