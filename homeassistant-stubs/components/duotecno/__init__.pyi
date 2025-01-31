from duotecno.controller import PyDuotecno
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type DuotecnoConfigEntry = ConfigEntry[PyDuotecno]

async def async_setup_entry(hass: HomeAssistant, entry: DuotecnoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DuotecnoConfigEntry) -> bool: ...
