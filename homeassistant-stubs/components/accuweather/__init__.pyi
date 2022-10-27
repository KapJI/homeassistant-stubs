from .const import ATTR_FORECAST as ATTR_FORECAST, CONF_FORECAST as CONF_FORECAST, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class AccuWeatherDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    location_key: Incomplete
    forecast: Incomplete
    accuweather: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, location_key: str, forecast: bool, name: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
