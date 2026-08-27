from .const import DOMAIN as DOMAIN
from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import async_device_info as async_device_info
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import AnyDeviceEntry as AnyDeviceEntry

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: EheimDigitalConfigEntry, device_entry: AnyDeviceEntry) -> bool: ...
