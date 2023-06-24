from .const import CONF_PROFILE_ID as CONF_PROFILE_ID, CONF_PROFILE_NAME as CONF_PROFILE_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class NextDnsFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    nextdns: Incomplete
    api_key: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_profiles(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
