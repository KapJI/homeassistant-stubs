import abc
import aiohttp
from .const import DOMAIN as DOMAIN, EXCLUDE_FROM_BACKUP as EXCLUDE_FROM_BACKUP, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.backup_restore import RESTORE_BACKUP_FILE as RESTORE_BACKUP_FILE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import integration_platform as integration_platform
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.util.json import json_loads_object as json_loads_object
from pathlib import Path
from typing import Any, Protocol

BUF_SIZE: Incomplete

@dataclass(slots=True)
class Backup:
    slug: str
    name: str
    date: str
    path: Path
    size: float
    def as_dict(self) -> dict: ...
    def __init__(self, slug, name, date, path, size) -> None: ...

class BackupPlatformProtocol(Protocol):
    async def async_pre_backup(self, hass: HomeAssistant) -> None: ...
    async def async_post_backup(self, hass: HomeAssistant) -> None: ...

class BaseBackupManager(abc.ABC, metaclass=abc.ABCMeta):
    hass: Incomplete
    backing_up: bool
    backups: Incomplete
    loaded_platforms: bool
    platforms: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def _add_platform(self, hass: HomeAssistant, integration_domain: str, platform: BackupPlatformProtocol) -> None: ...
    async def async_pre_backup_actions(self, **kwargs: Any) -> None: ...
    async def async_post_backup_actions(self, **kwargs: Any) -> None: ...
    async def load_platforms(self) -> None: ...
    @abc.abstractmethod
    async def async_restore_backup(self, slug: str, **kwargs: Any) -> None: ...
    @abc.abstractmethod
    async def async_create_backup(self, **kwargs: Any) -> Backup: ...
    @abc.abstractmethod
    async def async_get_backups(self, **kwargs: Any) -> dict[str, Backup]: ...
    @abc.abstractmethod
    async def async_get_backup(self, *, slug: str, **kwargs: Any) -> Backup | None: ...
    @abc.abstractmethod
    async def async_remove_backup(self, *, slug: str, **kwargs: Any) -> None: ...
    @abc.abstractmethod
    async def async_receive_backup(self, *, contents: aiohttp.BodyPartReader, **kwargs: Any) -> None: ...

class BackupManager(BaseBackupManager):
    backup_dir: Incomplete
    loaded_backups: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    backups: Incomplete
    async def load_backups(self) -> None: ...
    def _read_backups(self) -> dict[str, Backup]: ...
    async def async_get_backups(self, **kwargs: Any) -> dict[str, Backup]: ...
    async def async_get_backup(self, *, slug: str, **kwargs: Any) -> Backup | None: ...
    async def async_remove_backup(self, *, slug: str, **kwargs: Any) -> None: ...
    async def async_receive_backup(self, *, contents: aiohttp.BodyPartReader, **kwargs: Any) -> None: ...
    backing_up: bool
    async def async_create_backup(self, **kwargs: Any) -> Backup: ...
    def _mkdir_and_generate_backup_contents(self, tar_file_path: Path, backup_data: dict[str, Any]) -> int: ...
    async def async_restore_backup(self, slug: str, **kwargs: Any) -> None: ...

def _generate_slug(date: str, name: str) -> str: ...
