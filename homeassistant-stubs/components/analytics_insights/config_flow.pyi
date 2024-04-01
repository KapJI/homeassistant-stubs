from .const import CONF_TRACKED_CUSTOM_INTEGRATIONS as CONF_TRACKED_CUSTOM_INTEGRATIONS, CONF_TRACKED_INTEGRATIONS as CONF_TRACKED_INTEGRATIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

INTEGRATION_TYPES_WITHOUT_ANALYTICS: Incomplete

class HomeassistantAnalyticsConfigFlow(ConfigFlow, domain=DOMAIN):
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class HomeassistantAnalyticsOptionsFlowHandler(OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
