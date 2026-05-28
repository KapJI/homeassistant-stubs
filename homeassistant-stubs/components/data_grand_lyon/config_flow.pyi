from .const import CONF_LINE as CONF_LINE, CONF_STATION_ID as CONF_STATION_ID, CONF_STOP_ID as CONF_STOP_ID, DOMAIN as DOMAIN, SUBENTRY_TYPE_STOP as SUBENTRY_TYPE_STOP, SUBENTRY_TYPE_VELOV_STATION as SUBENTRY_TYPE_VELOV_STATION
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_RECONFIGURE_SCHEMA: Incomplete
STEP_STOP_DATA_SCHEMA: Incomplete
STEP_VELOV_STATION_DATA_SCHEMA: Incomplete

class DataGrandLyonConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _test_connection(self, user_input: dict[str, Any]) -> str | None: ...

class StopSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...

class VelovStationSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
