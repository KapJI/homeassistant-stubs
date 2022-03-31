from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class KaleidescapeDeviceInfo:
    host: str
    serial: str
    name: str
    model: str
    server_only: bool
    def __init__(self, host, serial, name, model, server_only) -> None: ...

class UnsupportedError(HomeAssistantError): ...

async def validate_host(host: str) -> KaleidescapeDeviceInfo: ...
