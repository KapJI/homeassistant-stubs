from .const import CONF_TAILNET as CONF_TAILNET, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

async def validate_input(hass: HomeAssistant, *, tailnet: str, api_key: str) -> None: ...

class TailscaleFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    reauth_entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
