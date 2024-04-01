from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class TVWeatherConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: ConfigEntry | None
    async def validate_input(self, sensor_api: str, station: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
