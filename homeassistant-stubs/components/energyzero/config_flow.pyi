from .const import CONF_ELECTRICITY_PRICE_INTERVAL as CONF_ELECTRICITY_PRICE_INTERVAL, DEFAULT_ELECTRICITY_PRICE_INTERVAL as DEFAULT_ELECTRICITY_PRICE_INTERVAL, DOMAIN as DOMAIN, ELECTRICITY_INTERVALS as ELECTRICITY_INTERVALS
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any, override

class EnergyZeroFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: ConfigEntry) -> EnergyZeroOptionsFlow: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class EnergyZeroOptionsFlow(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
