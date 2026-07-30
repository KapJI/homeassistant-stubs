import asyncio
from .const import DOMAIN as DOMAIN, SIGNAL_NEW_POOL as SIGNAL_NEW_POOL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from _typeshed import Incomplete
from aioaquarite import AquariteAuth, AquariteClient, ResilientUserPoolsSubscription as ResilientUserPoolsSubscription
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

_LOGGER: Incomplete
PLATFORMS: list[Platform]

@dataclass
class VistapoolData:
    auth: AquariteAuth
    api: AquariteClient
    coordinators: dict[str, VistapoolDataUpdateCoordinator] = field(default_factory=dict)
    sync_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
type VistapoolConfigEntry = ConfigEntry[VistapoolData]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VistapoolConfigEntry) -> bool: ...
@callback
def _async_remove_stale_devices(hass: HomeAssistant, entry: VistapoolConfigEntry, valid_pool_ids: set[str]) -> None: ...
async def _async_initial_refresh(coordinator: VistapoolDataUpdateCoordinator, *, first: bool) -> None: ...
async def _async_add_coordinator(hass: HomeAssistant, entry: VistapoolConfigEntry, pool_id: str, pool_name: str, *, first: bool) -> VistapoolDataUpdateCoordinator: ...
async def _async_reconcile_pools(hass: HomeAssistant, entry: VistapoolConfigEntry, pool_ids: list[str]) -> None: ...
