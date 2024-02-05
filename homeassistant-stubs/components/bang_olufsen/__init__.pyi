from .const import DOMAIN as DOMAIN
from .websocket import BangOlufsenWebsocket as BangOlufsenWebsocket
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from mozart_api.mozart_client import MozartClient

@dataclass
class BangOlufsenData:
    websocket: BangOlufsenWebsocket
    client: MozartClient
    def __init__(self, websocket, client) -> None: ...

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
