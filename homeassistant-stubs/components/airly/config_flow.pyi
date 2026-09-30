from .const import CONF_USE_NEAREST as CONF_USE_NEAREST, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, override

DESCRIPTION_PLACEHOLDERS: Incomplete
_LOGGER: Incomplete

class AirlyFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_check_location(self, api_key: str, latitude: float, longitude: float, use_nearest: bool = False) -> tuple[bool, dict[str, str]]: ...
