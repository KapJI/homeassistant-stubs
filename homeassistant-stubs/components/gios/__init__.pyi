from .const import API_TIMEOUT as API_TIMEOUT, CONF_STATION_ID as CONF_STATION_ID, DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import async_get_registry as async_get_registry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class GiosDataUpdateCoordinator(DataUpdateCoordinator):
    gios: Any
    def __init__(self, hass: HomeAssistant, session: ClientSession, station_id: int) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
