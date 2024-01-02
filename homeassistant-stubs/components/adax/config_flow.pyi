from .const import ACCOUNT_ID as ACCOUNT_ID, CLOUD as CLOUD, CONNECTION_TYPE as CONNECTION_TYPE, DOMAIN as DOMAIN, LOCAL as LOCAL, WIFI_PSWD as WIFI_PSWD, WIFI_SSID as WIFI_SSID
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_local(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_cloud(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
