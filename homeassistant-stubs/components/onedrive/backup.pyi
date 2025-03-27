from .const import CONF_DELETE_PERMANENTLY as CONF_DELETE_PERMANENTLY, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, BackupNotFound as BackupNotFound, suggested_filename as suggested_filename
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, Concatenate

_LOGGER: Incomplete
UPLOAD_CHUNK_SIZE: Incomplete
TIMEOUT: Incomplete
METADATA_VERSION: int
CACHE_TTL: int

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...
def handle_backup_errors[_R, **P](func: Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]: ...

@dataclass(kw_only=True)
class OneDriveBackup:
    backup: AgentBackup
    backup_file_id: str
    metadata_file_id: str

class OneDriveBackupAgent(BackupAgent):
    domain = DOMAIN
    _hass: Incomplete
    _entry: Incomplete
    _client: Incomplete
    _token_function: Incomplete
    _folder_id: Incomplete
    name: Incomplete
    unique_id: Incomplete
    _backup_cache: dict[str, OneDriveBackup]
    _cache_expiration: Incomplete
    def __init__(self, hass: HomeAssistant, entry: OneDriveConfigEntry) -> None: ...
    @handle_backup_errors
    async def async_download_backup(self, backup_id: str, **kwargs: Any) -> AsyncIterator[bytes]: ...
    @handle_backup_errors
    async def async_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup, **kwargs: Any) -> None: ...
    @handle_backup_errors
    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None: ...
    @handle_backup_errors
    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]: ...
    @handle_backup_errors
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup: ...
    async def _list_cached_backups(self) -> dict[str, OneDriveBackup]: ...
