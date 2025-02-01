from . import OneDriveConfigEntry as OneDriveConfigEntry
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, suggested_filename as suggested_filename
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from msgraph.generated.drives.item.items.item.drive_item_item_request_builder import DriveItemItemRequestBuilder as DriveItemItemRequestBuilder
from msgraph.generated.models.drive_item import DriveItem
from typing import Any, Concatenate

_LOGGER: Incomplete
UPLOAD_CHUNK_SIZE: Incomplete
MAX_RETRIES: int

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...
def handle_backup_errors[_R, **P](func: Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[OneDriveBackupAgent, P], Coroutine[Any, Any, _R]]: ...

class OneDriveBackupAgent(BackupAgent):
    domain = DOMAIN
    _hass: Incomplete
    _entry: Incomplete
    _items: Incomplete
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
    async def _find_item_by_backup_id(self, backup_id: str) -> DriveItem | None: ...
    def _get_backup_file_item(self, backup_id: str) -> DriveItemItemRequestBuilder: ...
    async def _upload_file(self, upload_url: str, stream: AsyncIterator[bytes], total_size: int) -> None: ...
