from .const import CONF_BACKUP_PATH as CONF_BACKUP_PATH, CONF_BACKUP_SHARE as CONF_BACKUP_SHARE, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from homeassistant.components.backup import AgentBackup as AgentBackup, BackupAgent as BackupAgent, BackupAgentError as BackupAgentError
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import ChunkAsyncStreamIterator as ChunkAsyncStreamIterator
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.util.json import JsonObjectType as JsonObjectType, json_loads_object as json_loads_object
from synology_dsm.api.file_station import SynoFileStation as SynoFileStation
from typing import Any

LOGGER: Incomplete

async def async_get_backup_agents(hass: HomeAssistant) -> list[BackupAgent]: ...
@callback
def async_register_backup_agents_listener(hass: HomeAssistant, *, listener: Callable[[], None], **kwargs: Any) -> Callable[[], None]: ...

class SynologyDSMBackupAgent(BackupAgent):
    domain = DOMAIN
    name: Incomplete
    unique_id: Incomplete
    path: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, unique_id: str) -> None: ...
    @property
    def _file_station(self) -> SynoFileStation: ...
    async def async_download_backup(self, backup_id: str, **kwargs: Any) -> AsyncIterator[bytes]: ...
    async def async_upload_backup(self, *, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup, **kwargs: Any) -> None: ...
    async def async_delete_backup(self, backup_id: str, **kwargs: Any) -> None: ...
    async def async_list_backups(self, **kwargs: Any) -> list[AgentBackup]: ...
    async def _async_list_backups(self, **kwargs: Any) -> dict[str, AgentBackup]: ...
    async def async_get_backup(self, backup_id: str, **kwargs: Any) -> AgentBackup | None: ...
