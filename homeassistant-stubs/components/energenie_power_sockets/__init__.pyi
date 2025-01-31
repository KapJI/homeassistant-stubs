from .const import CONF_DEVICE_API_ID as CONF_DEVICE_API_ID
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from pyegps import PowerStripUSB

PLATFORMS: Incomplete
type EnergenieConfigEntry = ConfigEntry[PowerStripUSB]

async def async_setup_entry(hass: HomeAssistant, entry: EnergenieConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EnergenieConfigEntry) -> bool: ...
