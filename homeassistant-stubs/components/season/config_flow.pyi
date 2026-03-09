from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, TYPE_ASTRONOMICAL as TYPE_ASTRONOMICAL, TYPE_METEOROLOGICAL as TYPE_METEOROLOGICAL
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

class SeasonConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
