from .const import DOMAIN as DOMAIN
from homeassistant.components import onboarding as onboarding, zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from technove import Station as TechnoVEStation
from typing import Any

class TechnoVEConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_host: str
    discovered_station: TechnoVEStation
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def _async_get_station(self, host: str) -> TechnoVEStation: ...
