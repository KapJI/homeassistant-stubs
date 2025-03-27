from . import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, GoogleDriveConfigEntry as GoogleDriveConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, BackupNotFound as BackupNotFound
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import ChunkAsyncStreamIterator as ChunkAsyncStreamIterator
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete

async def async_get_backup_agents(hass: HomeAssistant, **kwargs: Any) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...

class GoogleDriveBackupAgent(BackupAgent):
    domain = DOMAIN
    name: Incomplete
    unique_id: Incomplete
    _client: Incomplete
    def __init__(self, config_entry: GoogleDriveConfigEntry) -> None: ...
    async def async_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup, **kwargs: Any) -> None: ...
    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]: ...
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup: ...
    async def async_download_backup(self, backup_id: str, **kwargs: Any) -> AsyncIterator[bytes]: ...
    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None: ...
