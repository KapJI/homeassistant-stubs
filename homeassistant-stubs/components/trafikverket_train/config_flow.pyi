from .const import CONF_FILTER_PRODUCT as CONF_FILTER_PRODUCT, CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import create_unique_id as create_unique_id, next_departuredate as next_departuredate
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector, TimeSelector as TimeSelector
from typing import Any

_LOGGER: Incomplete
OPTION_SCHEMA: Incomplete
DATA_SCHEMA: Incomplete
DATA_SCHEMA_REAUTH: Incomplete

async def validate_input(hass: HomeAssistant, api_key: str, train_from: str, train_to: str, train_time: str | None, weekdays: list[str], product_filter: str | None) -> dict[str, str]: ...

class TVTrainConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: config_entries.ConfigEntry | None
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> TVTrainOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class TVTrainOptionsFlowHandler(config_entries.OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
