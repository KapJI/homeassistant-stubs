from . import OneDriveConfigEntry as OneDriveConfigEntry
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, suggested_filename as suggested_filename
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from onedrive_personal_sdk.models.items import File as File, Folder as Folder
from typing import Any, Concatenate

_LOGGER: Incomplete
UPLOAD_CHUNK_SIZE: Incomplete
TIMEOUT: Incomplete

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...
def handle_backup_errors[_R, **P](func: Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]: ...

class OneDriveBackupAgent(BackupAgent):
    domain = DOMAIN
    _hass: Incomplete
    _entry: Incomplete
    _client: Incomplete
    _token_provider: Incomplete
    _folder_id: Incomplete
    name: Incomplete
    unique_id: Incomplete
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
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup | None: ...
    def _backup_from_description(self, description: str) -> AgentBackup: ...
    async def _find_item_by_backup_id(self, backup_id: str) -> File | Folder | None: ...
