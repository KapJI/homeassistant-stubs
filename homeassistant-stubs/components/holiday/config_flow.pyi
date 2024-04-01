from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.helpers.selector import CountrySelector as CountrySelector, CountrySelectorConfig as CountrySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

SUPPORTED_COUNTRIES: Incomplete

class HolidayConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    config_entry: ConfigEntry | None
    data: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_province(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
