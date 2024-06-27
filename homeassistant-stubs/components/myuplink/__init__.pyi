from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN, OAUTH2_SCOPES as OAUTH2_SCOPES
from .coordinator import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

PLATFORMS: list[Platform]
MyUplinkConfigEntry = ConfigEntry[MyUplinkDataCoordinator]

async def async_setup_entry(hass: HomeAssistant, config_entry: MyUplinkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def create_devices(hass: HomeAssistant, config_entry: ConfigEntry, coordinator: MyUplinkDataCoordinator) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: MyUplinkConfigEntry, device_entry: DeviceEntry) -> bool: ...
