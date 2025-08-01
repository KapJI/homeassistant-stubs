import asyncio
from .actions import get_music_assistant_client as get_music_assistant_client, register_actions as register_actions
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_URL as CONF_URL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from music_assistant_client import MusicAssistantClient
from music_assistant_models.event import MassEvent as MassEvent

PLATFORMS: Incomplete
CONNECT_TIMEOUT: int
LISTEN_READY_TIMEOUT: int
CONFIG_SCHEMA: Incomplete
type MusicAssistantConfigEntry = ConfigEntry[MusicAssistantEntryData]
type PlayerAddCallback = Callable[[str], None]

@dataclass
class MusicAssistantEntryData:
    mass: MusicAssistantClient
    listen_task: asyncio.Task
    discovered_players: set[str] = field(default_factory=set)
    platform_handlers: dict[Platform, PlayerAddCallback] = field(default_factory=dict)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry) -> bool: ...
async def _client_listen(hass: HomeAssistant, entry: ConfigEntry, mass: MusicAssistantClient, init_ready: asyncio.Event) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
