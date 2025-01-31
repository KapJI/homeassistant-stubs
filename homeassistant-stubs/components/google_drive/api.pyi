from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession, StreamReader as StreamReader
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from google_drive_api.api import AbstractAuth
from homeassistant.components.backup import AgentBackup as AgentBackup
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_UPLOAD_AND_DOWNLOAD_TIMEOUT: Incomplete
_LOGGER: Incomplete

class AsyncConfigEntryAuth(AbstractAuth):
    _oauth_session: Incomplete
    def __init__(self, websession: ClientSession, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...

class AsyncConfigFlowAuth(AbstractAuth):
    _token: Incomplete
    def __init__(self, websession: ClientSession, token: str) -> None: ...
    async def async_get_access_token(self) -> str: ...

class DriveClient:
    _ha_instance_id: Incomplete
    _api: Incomplete
    def __init__(self, ha_instance_id: str, auth: AbstractAuth) -> None: ...
    async def async_get_email_address(self) -> str: ...
    async def async_create_ha_root_folder_if_not_exists(self) -> tuple[str, str]: ...
    async def async_upload_backup(self, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], backup: AgentBackup) -> None: ...
    async def async_list_backups(self) -> list[AgentBackup]: ...
    async def async_get_backup_file_id(self, backup_id: str) -> str | None: ...
    async def async_delete(self, file_id: str) -> None: ...
    async def async_download(self, file_id: str) -> StreamReader: ...
