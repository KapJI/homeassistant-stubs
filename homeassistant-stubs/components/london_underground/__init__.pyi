from .coordinator import LondonTubeCoordinator as LondonTubeCoordinator, LondonUndergroundConfigEntry as LondonUndergroundConfigEntry, TubeData as TubeData
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LondonUndergroundConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LondonUndergroundConfigEntry) -> bool: ...
