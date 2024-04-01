from .const import CONF_PROFILE_ID as CONF_PROFILE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PROFILE_NAME as CONF_PROFILE_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class NextDnsFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    nextdns: Incomplete
    api_key: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_profiles(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
