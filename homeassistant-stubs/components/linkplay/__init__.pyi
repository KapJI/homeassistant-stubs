from .const import PLATFORMS as PLATFORMS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge

class LinkPlayData:
    bridge: LinkPlayBridge
LinkPlayConfigEntry = ConfigEntry[LinkPlayData]

async def async_setup_entry(hass: HomeAssistant, entry: LinkPlayConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LinkPlayConfigEntry) -> bool: ...
