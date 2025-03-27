from .const import DESCRIPTION as DESCRIPTION, DEVICE as DEVICE, FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, PRODUCT as PRODUCT
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.util import guess_firmware_info as guess_firmware_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
