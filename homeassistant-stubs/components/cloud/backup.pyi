from .client import CloudClient as CloudClient
from .const import DATA_CLOUD as DATA_CLOUD, DOMAIN as DOMAIN, EVENT_CLOUD_EVENT as EVENT_CLOUD_EVENT
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import ChunkAsyncStreamIterator as ChunkAsyncStreamIterator
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from typing import Any

_LOGGER: Incomplete
_STORAGE_BACKUP: str
_RETRY_LIMIT: int
_RETRY_SECONDS_MIN: int
_RETRY_SECONDS_MAX: int

async def _b64md5(stream: AsyncIterator[bytes]) -> str: ...
async def async_get_backup_agents(hass: HomeAssistant, **kwargs: Any) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...

class CloudBackupAgent(BackupAgent):
    domain = DOMAIN
    name = DOMAIN
    unique_id = DOMAIN
    _cloud: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant, cloud: Cloud[CloudClient]) -> None: ...
    @callback
    def _get_backup_filename(self) -> str: ...
    async def async_download_backup(self, backup_id: str, **kwargs: Any) -> AsyncIterator[bytes]: ...
    async def _async_do_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], filename: str, base64md5hash: str, metadata: dict[str, Any], size: int) -> None: ...
    async def async_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup, **kwargs: Any) -> None: ...
    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None: ...
    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]: ...
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup | None: ...
