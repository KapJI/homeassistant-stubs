import voluptuous as vol
from .const import CONF_REFERRER as CONF_REFERRER, DOMAIN as DOMAIN, SECTION_API_KEY_OPTIONS as SECTION_API_KEY_OPTIONS
from _typeshed import Incomplete
from google_weather_api import GoogleWeatherApi
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import section as section
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import LocationSelector as LocationSelector, LocationSelectorConfig as LocationSelectorConfig
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _validate_input(user_input: dict[str, Any], api: GoogleWeatherApi, errors: dict[str, str], description_placeholders: dict[str, str]) -> bool: ...
def _get_location_schema(hass: HomeAssistant) -> vol.Schema: ...
def _is_location_already_configured(hass: HomeAssistant, new_data: dict[str, float], epsilon: float = 0.0001) -> bool: ...

class GoogleWeatherConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...

class LocationSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_location(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async_step_user = async_step_location
