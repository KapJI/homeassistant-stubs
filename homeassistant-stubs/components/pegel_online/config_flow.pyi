from .const import CONF_STATION as CONF_STATION, DEFAULT_RADIUS as DEFAULT_RADIUS, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_RADIUS as CONF_RADIUS, UnitOfLength as UnitOfLength
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import LocationSelector as LocationSelector, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _data: dict[str, Any]
    _stations: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_select_station(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _show_form_user(self, user_input: dict[str, Any] | None = None, errors: dict[str, Any] | None = None) -> ConfigFlowResult: ...
