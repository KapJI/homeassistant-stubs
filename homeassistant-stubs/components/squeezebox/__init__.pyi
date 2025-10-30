import asyncio
from .const import CONF_HTTPS as CONF_HTTPS, DISCOVERY_INTERVAL as DISCOVERY_INTERVAL, DOMAIN as DOMAIN, SERVER_MANUFACTURER as SERVER_MANUFACTURER, SERVER_MODEL as SERVER_MODEL, SERVER_MODEL_ID as SERVER_MODEL_ID, SIGNAL_PLAYER_DISCOVERED as SIGNAL_PLAYER_DISCOVERED, SIGNAL_PLAYER_REDISCOVERED as SIGNAL_PLAYER_REDISCOVERED, STATUS_API_TIMEOUT as STATUS_API_TIMEOUT, STATUS_QUERY_LIBRARYNAME as STATUS_QUERY_LIBRARYNAME, STATUS_QUERY_MAC as STATUS_QUERY_MAC, STATUS_QUERY_UUID as STATUS_QUERY_UUID, STATUS_QUERY_VERSION as STATUS_QUERY_VERSION
from .coordinator import LMSStatusDataUpdateCoordinator as LMSStatusDataUpdateCoordinator, SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceEntryType as DeviceEntryType, format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util.hass_dict import HassKey as HassKey
from pysqueezebox import Player as Player, Server

_LOGGER: Incomplete
PLATFORMS: Incomplete
SQUEEZEBOX_HASS_DATA: HassKey[asyncio.Task]

@dataclass
class SqueezeboxData:
    coordinator: LMSStatusDataUpdateCoordinator
    server: Server
    known_player_ids: set[str] = field(default_factory=set)
type SqueezeboxConfigEntry = ConfigEntry[SqueezeboxData]

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry) -> bool: ...
