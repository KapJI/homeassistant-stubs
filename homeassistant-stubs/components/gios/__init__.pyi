from .const import API_TIMEOUT as API_TIMEOUT, CONF_STATION_ID as CONF_STATION_ID, DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class GiosDataUpdateCoordinator(DataUpdateCoordinator):
    gios: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, station_id: int) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
