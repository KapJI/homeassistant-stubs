from .const import DOMAIN as DOMAIN
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

class OTBRConfigFlow(ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
