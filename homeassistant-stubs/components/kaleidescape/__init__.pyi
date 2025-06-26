from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from kaleidescape import Device as KaleidescapeDevice

PLATFORMS: Incomplete
type KaleidescapeConfigEntry = ConfigEntry[KaleidescapeDevice]

async def async_setup_entry(hass: HomeAssistant, entry: KaleidescapeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: KaleidescapeConfigEntry) -> bool: ...

@dataclass
class KaleidescapeDeviceInfo:
    host: str
    serial: str
    name: str
    model: str
    server_only: bool

class UnsupportedError(HomeAssistantError): ...

async def validate_host(host: str) -> KaleidescapeDeviceInfo: ...
