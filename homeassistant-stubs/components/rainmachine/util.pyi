from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Iterable
from datetime import timedelta
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SIGNAL_REBOOT_COMPLETED: str
SIGNAL_REBOOT_REQUESTED: str

class RunStates(StrEnum):
    NOT_RUNNING: str
    QUEUED: str
    RUNNING: str

RUN_STATE_MAP: Incomplete

class EntityDomainReplacementStrategy:
    old_domain: str
    old_unique_id: str
    replacement_entity_id: str
    breaks_in_ha_version: str
    remove_old_entity: bool
    def __init__(self, old_domain, old_unique_id, replacement_entity_id, breaks_in_ha_version, remove_old_entity) -> None: ...

def async_finish_entity_domain_replacements(hass: HomeAssistant, entry: ConfigEntry, entity_replacement_strategies: Iterable[EntityDomainReplacementStrategy]) -> None: ...
def key_exists(data: dict[str, Any], search_key: str) -> bool: ...

class RainMachineDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    config_entry: ConfigEntry
    _rebooting: bool
    _signal_handler_unsubs: Incomplete
    signal_reboot_completed: Incomplete
    signal_reboot_requested: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, name: str, api_category: str, update_interval: timedelta, update_method: Callable[..., Awaitable]) -> None: ...
    last_update_success: bool
    async def async_initialize(self) -> None: ...
