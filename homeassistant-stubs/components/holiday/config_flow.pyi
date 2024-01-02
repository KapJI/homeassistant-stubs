from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.selector import CountrySelector as CountrySelector, CountrySelectorConfig as CountrySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

SUPPORTED_COUNTRIES: Incomplete

class HolidayConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_province(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
