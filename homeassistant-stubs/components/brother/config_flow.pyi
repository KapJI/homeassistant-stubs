from .const import CONF_COMMUNITY as CONF_COMMUNITY, DEFAULT_COMMUNITY as DEFAULT_COMMUNITY, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, PRINTER_TYPES as PRINTER_TYPES, PRINTER_TYPE_LASER as PRINTER_TYPE_LASER, SECTION_ADVANCED_SETTINGS as SECTION_ADVANCED_SETTINGS
from _typeshed import Incomplete
from brother import Brother
from homeassistant.components.snmp import async_get_snmp_engine as async_get_snmp_engine
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import section as section
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

DATA_SCHEMA: Incomplete
ZEROCONF_SCHEMA: Incomplete
RECONFIGURE_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, user_input: dict[str, Any], expected_mac: str | None = None) -> tuple[str, str]: ...

class BrotherConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    brother: Brother
    host: str | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidHost(HomeAssistantError): ...
class AnotherDevice(HomeAssistantError): ...
