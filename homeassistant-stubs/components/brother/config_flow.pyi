from .const import DOMAIN as DOMAIN, PRINTER_TYPES as PRINTER_TYPES
from .utils import get_snmp_engine as get_snmp_engine
from _typeshed import Incomplete
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

DATA_SCHEMA: Incomplete

class BrotherConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    brother: Incomplete
    host: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidHost(HomeAssistantError): ...
