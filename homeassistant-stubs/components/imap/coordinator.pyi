from .const import CONF_CHARSET as CONF_CHARSET, CONF_CUSTOM_EVENT_DATA_TEMPLATE as CONF_CUSTOM_EVENT_DATA_TEMPLATE, CONF_FOLDER as CONF_FOLDER, CONF_MAX_MESSAGE_SIZE as CONF_MAX_MESSAGE_SIZE, CONF_SEARCH as CONF_SEARCH, CONF_SERVER as CONF_SERVER, CONF_SSL_CIPHER_LIST as CONF_SSL_CIPHER_LIST, DEFAULT_MAX_MESSAGE_SIZE as DEFAULT_MAX_MESSAGE_SIZE, DOMAIN as DOMAIN
from .errors import InvalidAuth as InvalidAuth, InvalidFolder as InvalidFolder
from _typeshed import Incomplete
from aioimaplib import IMAP4_SSL
from collections.abc import Mapping
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, CONTENT_TYPE_TEXT_PLAIN as CONTENT_TYPE_TEXT_PLAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, TemplateError as TemplateError
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.ssl import SSLCipherList as SSLCipherList, client_context as client_context, create_no_verify_ssl_context as create_no_verify_ssl_context
from typing import Any

_LOGGER: Incomplete
BACKOFF_TIME: int
EVENT_IMAP: str
MAX_ERRORS: int
MAX_EVENT_DATA_BYTES: int

async def connect_to_server(data: Mapping[str, Any]) -> IMAP4_SSL: ...

class ImapMessage:
    _charset: Incomplete
    email_message: Incomplete
    def __init__(self, raw_message: bytes, charset: str = 'utf-8') -> None: ...
    @property
    def headers(self) -> dict[str, tuple[str]]: ...
    @property
    def message_id(self) -> str | None: ...
    @property
    def date(self) -> datetime | None: ...
    @property
    def sender(self) -> str: ...
    @property
    def subject(self) -> str: ...
    @property
    def text(self) -> str: ...

class ImapDataUpdateCoordinator(DataUpdateCoordinator[int | None]):
    config_entry: ConfigEntry
    custom_event_template: Template | None
    imap_client: Incomplete
    auth_errors: int
    _last_message_uid: Incomplete
    _last_message_id: Incomplete
    def __init__(self, hass: HomeAssistant, imap_client: IMAP4_SSL, entry: ConfigEntry, update_interval: timedelta | None) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_reconnect_if_needed(self) -> None: ...
    async def _async_process_event(self, last_message_uid: str) -> None: ...
    async def _async_fetch_number_of_messages(self) -> int | None: ...
    async def _cleanup(self, log_error: bool = False) -> None: ...
    async def shutdown(self, *_: Any) -> None: ...

class ImapPollingDataUpdateCoordinator(ImapDataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, imap_client: IMAP4_SSL, entry: ConfigEntry) -> None: ...
    auth_errors: int
    async def _async_update_data(self) -> int | None: ...

class ImapPushDataUpdateCoordinator(ImapDataUpdateCoordinator):
    _push_wait_task: Incomplete
    def __init__(self, hass: HomeAssistant, imap_client: IMAP4_SSL, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> int | None: ...
    async def async_start(self) -> None: ...
    auth_errors: int
    async def _async_wait_push_loop(self) -> None: ...
    async def shutdown(self, *_: Any) -> None: ...
