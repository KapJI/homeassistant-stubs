from .const import CALC_METHODS as CALC_METHODS, CONF_CALC_METHOD as CONF_CALC_METHOD, CONF_LAT_ADJ_METHOD as CONF_LAT_ADJ_METHOD, CONF_MIDNIGHT_MODE as CONF_MIDNIGHT_MODE, CONF_SCHOOL as CONF_SCHOOL, DEFAULT_CALC_METHOD as DEFAULT_CALC_METHOD, DEFAULT_LAT_ADJ_METHOD as DEFAULT_LAT_ADJ_METHOD, DEFAULT_MIDNIGHT_MODE as DEFAULT_MIDNIGHT_MODE, DEFAULT_SCHOOL as DEFAULT_SCHOOL, DOMAIN as DOMAIN, LAT_ADJ_METHODS as LAT_ADJ_METHODS, MIDNIGHT_MODES as MIDNIGHT_MODES, NAME as NAME, SCHOOLS as SCHOOLS
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

class IslamicPrayerFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> IslamicPrayerOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class IslamicPrayerOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
