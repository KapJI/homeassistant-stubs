from .const import DOMAIN as DOMAIN, LinkPlaySharedData as LinkPlaySharedData, PLATFORMS as PLATFORMS, SHARED_DATA as SHARED_DATA
from .utils import async_get_client_session as async_get_client_session
from aiohttp import ClientSession as ClientSession
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge

@dataclass
class LinkPlayData:
    bridge: LinkPlayBridge
type LinkPlayConfigEntry = ConfigEntry[LinkPlayData]

async def async_setup_entry(hass: HomeAssistant, entry: LinkPlayConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LinkPlayConfigEntry) -> bool: ...
