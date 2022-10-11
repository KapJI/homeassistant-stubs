from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, async_get as async_get

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...