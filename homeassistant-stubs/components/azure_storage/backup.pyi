from . import AzureStorageConfigEntry as AzureStorageConfigEntry
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from azure.storage.blob import BlobProperties as BlobProperties
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, BackupNotFound as BackupNotFound, suggested_filename as suggested_filename
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Concatenate

_LOGGER: Incomplete
METADATA_VERSION: str

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...
def handle_backup_errors[_R, **P](func: Callable[Concatenate[AzureStorageBackupAgent, P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[AzureStorageBackupAgent, P], Coroutine[Any, Any, _R]]: ...

class AzureStorageBackupAgent(BackupAgent):
    domain = DOMAIN
    _client: Incomplete
    name: Incomplete
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AzureStorageConfigEntry) -> None: ...
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
    async def _find_blob_by_backup_id(self, backup_id: str) -> BlobProperties | None: ...
