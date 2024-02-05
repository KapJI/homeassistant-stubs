from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN
from .coordinator import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def create_devices(hass: HomeAssistant, config_entry: ConfigEntry, coordinator: MyUplinkDataCoordinator) -> None: ...
