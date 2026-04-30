from .const import CONF_AZIMUTH as CONF_AZIMUTH, CONF_DAMPING_EVENING as CONF_DAMPING_EVENING, CONF_DAMPING_MORNING as CONF_DAMPING_MORNING, CONF_DECLINATION as CONF_DECLINATION, CONF_INVERTER_SIZE as CONF_INVERTER_SIZE, CONF_MODULES_POWER as CONF_MODULES_POWER, DEFAULT_AZIMUTH as DEFAULT_AZIMUTH, DEFAULT_DAMPING as DEFAULT_DAMPING, DEFAULT_DECLINATION as DEFAULT_DECLINATION, DEFAULT_MODULES_POWER as DEFAULT_MODULES_POWER, DOMAIN as DOMAIN, MAX_PLANES as MAX_PLANES, SUBENTRY_TYPE_PLANE as SUBENTRY_TYPE_PLANE
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, OptionsFlow as OptionsFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from typing import Any

RE_API_KEY: Incomplete
PLANE_SCHEMA: Incomplete

class ForecastSolarFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> ForecastSolarOptionFlowHandler: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ForecastSolarOptionFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class PlaneSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
