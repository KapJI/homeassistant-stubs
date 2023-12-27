from .const import CONF_UID as CONF_UID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp, zeroconf as zeroconf
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DEFAULT_PORT: int
DATA_SCHEMA: Incomplete
UNIQUE_ID: str

def async_get_pin_from_discovery_hostname(hostname: str) -> str: ...
def async_get_pin_from_uid(uid: str) -> str: ...
async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery_info: Incomplete
    def __init__(self) -> None: ...
    async def _async_set_unique_id(self, pin: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def _async_handle_discovery(self) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
