from .const import DOMAIN as DOMAIN, PRINTER_TYPES as PRINTER_TYPES
from .utils import get_snmp_engine as get_snmp_engine
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DATA_SCHEMA: Any

def host_valid(host: str) -> bool: ...

class BrotherConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    brother: Any
    host: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class InvalidHost(exceptions.HomeAssistantError): ...
