import asyncio
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components.backup import BackupManager as BackupManager, BackupPlatformEvent as BackupPlatformEvent, ManagerStateEvent as ManagerStateEvent
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_BACKUP: HassKey[BackupData]
DATA_MANAGER: HassKey[BackupManager]

@dataclass(slots=True)
class BackupData:
    backup_event_subscriptions: list[Callable[[ManagerStateEvent], None]] = field(default_factory=list)
    backup_platform_event_subscriptions: list[Callable[[BackupPlatformEvent], None]] = field(default_factory=list)
    manager_ready: asyncio.Future[None] = field(default_factory=asyncio.Future)

@callback
def async_initialize_backup(hass: HomeAssistant) -> None: ...
async def async_get_manager(hass: HomeAssistant) -> BackupManager: ...
@callback
def async_subscribe_events(hass: HomeAssistant, on_event: Callable[[ManagerStateEvent], None]) -> Callable[[], None]: ...
@callback
def async_subscribe_platform_events(hass: HomeAssistant, on_event: Callable[[BackupPlatformEvent], None]) -> Callable[[], None]: ...
