from .const import CONF_USE_AUX1 as CONF_USE_AUX1, CONF_USE_AUX2 as CONF_USE_AUX2, CONF_USE_AUX3 as CONF_USE_AUX3, CONF_USE_AUX4 as CONF_USE_AUX4, CONF_USE_COVER_SENSOR as CONF_USE_COVER_SENSOR, CONF_USE_LIGHT as CONF_USE_LIGHT, CURRENT_VERSION as CURRENT_VERSION, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UNIT_ID as DEFAULT_UNIT_ID, DOMAIN as DOMAIN
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from typing import Any, override

async def _async_probe(user_input: dict[str, Any]) -> tuple[str | None, str | None]: ...

class NeoPoolConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = CURRENT_VERSION
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: NeoPoolConfigEntry) -> NeoPoolOptionsFlowHandler: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class NeoPoolOptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
