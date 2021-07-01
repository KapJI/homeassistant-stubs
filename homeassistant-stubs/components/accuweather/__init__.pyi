from .const import ATTR_FORECAST as ATTR_FORECAST, CONF_FORECAST as CONF_FORECAST, DOMAIN as DOMAIN
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Dict

_LOGGER: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class AccuWeatherDataUpdateCoordinator(DataUpdateCoordinator[Dict[str, Any]]):
    location_key: Any
    forecast: Any
    is_metric: Any
    accuweather: Any
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, location_key: str, forecast: bool) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
