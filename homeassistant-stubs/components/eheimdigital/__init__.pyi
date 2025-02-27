from .const import DOMAIN as DOMAIN
from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: EheimDigitalConfigEntry, device_entry: DeviceEntry) -> bool: ...
