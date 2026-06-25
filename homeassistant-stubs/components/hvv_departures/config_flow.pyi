from .const import CONF_FILTER as CONF_FILTER, CONF_REAL_TIME as CONF_REAL_TIME, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from .hub import GTIHub as GTIHub, HVVConfigEntry as HVVConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_OFFSET as CONF_OFFSET, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, override

_LOGGER: Incomplete
SCHEMA_STEP_USER: Incomplete
SCHEMA_STEP_STATION: Incomplete
SCHEMA_STEP_OPTIONS: Incomplete

class HVVDeparturesConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    hub: GTIHub
    data: dict[str, Any]
    stations: dict[str, Any]
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_station(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_station_select(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: HVVConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlow):
    config_entry: HVVConfigEntry
    departure_filters: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
