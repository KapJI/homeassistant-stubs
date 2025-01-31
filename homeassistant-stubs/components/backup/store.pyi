from .config import StoredBackupConfig as StoredBackupConfig
from .const import DOMAIN as DOMAIN
from .manager import BackupManager as BackupManager, StoredKnownBackup as StoredKnownBackup
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any, TypedDict

STORE_DELAY_SAVE: int
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int

class StoredBackupData(TypedDict):
    backups: list[StoredKnownBackup]
    config: StoredBackupConfig

class _BackupStore(Store[StoredBackupData]):
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

class BackupStore:
    _hass: Incomplete
    _manager: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant, manager: BackupManager) -> None: ...
    async def load(self) -> StoredBackupData | None: ...
    @callback
    def save(self) -> None: ...
    @callback
    def _data_to_save(self) -> StoredBackupData: ...
