from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SamsungExLinkConfigEntry as SamsungExLinkConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_MODEL as CONF_MODEL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from samsung_exlink import TVState as TVState

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SamsungExLinkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SamsungExLinkConfigEntry) -> bool: ...
