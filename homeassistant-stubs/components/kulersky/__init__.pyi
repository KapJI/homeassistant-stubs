from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.bluetooth import async_ble_device_from_address as async_ble_device_from_address
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_INTEGRATION_DISCOVERY as SOURCE_INTEGRATION_DISCOVERY
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
