from .const import CONF_TRACKED_INTEGRATIONS as CONF_TRACKED_INTEGRATIONS, DOMAIN as DOMAIN
from .coordinator import HomeassistantAnalyticsDataUpdateCoordinator as HomeassistantAnalyticsDataUpdateCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

@dataclass(frozen=True)
class AnalyticsInsightsData:
    coordinator: HomeassistantAnalyticsDataUpdateCoordinator
    names: dict[str, str]
    def __init__(self, coordinator, names) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
