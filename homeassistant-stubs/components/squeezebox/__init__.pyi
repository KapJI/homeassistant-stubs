from .const import CONF_HTTPS as CONF_HTTPS, DISCOVERY_TASK as DISCOVERY_TASK, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SERVER_MODEL as SERVER_MODEL, STATUS_API_TIMEOUT as STATUS_API_TIMEOUT, STATUS_QUERY_LIBRARYNAME as STATUS_QUERY_LIBRARYNAME, STATUS_QUERY_MAC as STATUS_QUERY_MAC, STATUS_QUERY_UUID as STATUS_QUERY_UUID, STATUS_QUERY_VERSION as STATUS_QUERY_VERSION
from .coordinator import LMSStatusDataUpdateCoordinator as LMSStatusDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceEntryType as DeviceEntryType, format_mac as format_mac
from pysqueezebox import Server

_LOGGER: Incomplete
PLATFORMS: Incomplete

@dataclass
class SqueezeboxData:
    coordinator: LMSStatusDataUpdateCoordinator
    server: Server
    def __init__(self, coordinator, server) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry) -> bool: ...
