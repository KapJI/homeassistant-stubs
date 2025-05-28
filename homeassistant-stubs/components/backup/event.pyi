from .coordinator import BackupConfigEntry as BackupConfigEntry, BackupDataUpdateCoordinator as BackupDataUpdateCoordinator
from .entity import BackupManagerBaseEntity as BackupManagerBaseEntity
from .manager import CreateBackupEvent as CreateBackupEvent, CreateBackupState as CreateBackupState
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

ATTR_BACKUP_STAGE: Final[str]
ATTR_FAILED_REASON: Final[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: BackupConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AutomaticBackupEvent(BackupManagerBaseEntity, EventEntity):
    _attr_event_types: Incomplete
    _unrecorded_attributes: Incomplete
    coordinator: BackupDataUpdateCoordinator
    _attr_unique_id: str
    _attr_translation_key: str
    def __init__(self, coordinator: BackupDataUpdateCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
