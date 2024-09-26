from .const import DOMAIN as DOMAIN
from .media_player import setup_services as setup_services
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from pyblu import Player, SyncStatus as SyncStatus

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

@dataclass
class BluesoundRuntimeData:
    player: Player
    sync_status: SyncStatus
    def __init__(self, player, sync_status) -> None: ...
BluesoundConfigEntry = ConfigEntry[BluesoundRuntimeData]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: BluesoundConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
