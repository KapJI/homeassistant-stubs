from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, DOMAIN as DOMAIN, SUBENTRY_TYPE_STATION as SUBENTRY_TYPE_STATION
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality as WAQIAirQuality, WAQIClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import LocationSelector as LocationSelector
from typing import Any

_LOGGER: Incomplete
CONF_MAP: str

async def get_by_station_number(client: WAQIClient, station_number: int) -> tuple[WAQIAirQuality | None, dict[str, str]]: ...

class WAQIConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class StationFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_map(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_station_number(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def _async_create_entry(self, measuring_station: WAQIAirQuality) -> SubentryFlowResult: ...
