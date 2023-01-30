import asyncio
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Awaitable, Callable as Callable, Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_UPDATE_INTERVAL: Incomplete
SIGNAL_REBOOT_REQUESTED: str

class EntityDomainReplacementStrategy:
    old_domain: str
    old_unique_id: str
    replacement_entity_id: str
    breaks_in_ha_version: str
    remove_old_entity: bool
    def __init__(self, old_domain, old_unique_id, replacement_entity_id, breaks_in_ha_version, remove_old_entity) -> None: ...

def async_finish_entity_domain_replacements(hass: HomeAssistant, entry: ConfigEntry, entity_replacement_strategies: Iterable[EntityDomainReplacementStrategy]) -> None: ...

class GuardianDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    config_entry: ConfigEntry
    _api_coro: Incomplete
    _api_lock: Incomplete
    _client: Incomplete
    signal_reboot_requested: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, client: Client, api_name: str, api_coro: Callable[..., Awaitable], api_lock: asyncio.Lock, valve_controller_uid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    last_update_success: bool
    async def async_initialize(self) -> None: ...
