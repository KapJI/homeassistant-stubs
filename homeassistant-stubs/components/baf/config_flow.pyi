from .const import DOMAIN as DOMAIN, RUN_TIMEOUT as RUN_TIMEOUT
from .models import BAFDiscovery as BAFDiscovery
from _typeshed import Incomplete
from aiobafi6 import Device
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete

async def async_try_connect(ip_address: str) -> Device: ...

class BAFFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery: Incomplete
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class CannotConnect(Exception): ...
