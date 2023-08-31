from .const import DOMAIN as DOMAIN
from .util import serialize_device_list as serialize_device_list
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_DEVICES as CONF_DEVICES, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

class AnovaConfligFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, str] | None = ...) -> FlowResult: ...
