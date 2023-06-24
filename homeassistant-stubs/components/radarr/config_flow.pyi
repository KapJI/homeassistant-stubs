from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class RadarrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: Incomplete
    def __init__(self) -> None: ...
    async def async_step_reauth(self, _: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> tuple[str, str, str] | None: ...
