import voluptuous as vol
from .const import API as API, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FLOW_SMILE as FLOW_SMILE, FLOW_STRETCH as FLOW_STRETCH, PW_TYPE as PW_TYPE, SMILE as SMILE, STRETCH as STRETCH, STRETCH_USERNAME as STRETCH_USERNAME, ZEROCONF_MAP as ZEROCONF_MAP
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_BASE as CONF_BASE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from plugwise import Smile
from typing import Any

def _base_gw_schema(discovery_info: ZeroconfServiceInfo | None) -> vol.Schema: ...
async def validate_gw_input(hass: HomeAssistant, data: dict[str, Any]) -> Smile: ...

class PlugwiseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery_info: ZeroconfServiceInfo | None
    _username: str
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
