from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .manager import BackupManager as BackupManager, BackupManagerState as BackupManagerState, BackupPlatformEvent as BackupPlatformEvent, ManagerStateEvent as ManagerStateEvent
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.backup import async_subscribe_events as async_subscribe_events, async_subscribe_platform_events as async_subscribe_platform_events
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

type BackupConfigEntry = ConfigEntry[BackupDataUpdateCoordinator]
@dataclass
class BackupCoordinatorData:
    backup_manager_state: BackupManagerState
    last_successful_automatic_backup: datetime | None
    next_scheduled_automatic_backup: datetime | None

class BackupDataUpdateCoordinator(DataUpdateCoordinator[BackupCoordinatorData]):
    config_entry: ConfigEntry
    unsubscribe: list[Callable[[], None]]
    backup_manager: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, backup_manager: BackupManager) -> None: ...
    @callback
    def _on_event(self, event: ManagerStateEvent | BackupPlatformEvent) -> None: ...
    async def _async_update_data(self) -> BackupCoordinatorData: ...
    @callback
    def async_unsubscribe(self) -> None: ...
