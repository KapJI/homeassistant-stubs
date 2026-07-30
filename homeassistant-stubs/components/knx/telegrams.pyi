import asyncio
from .const import CONF_KNX_TELEGRAM_DB_BACKEND as CONF_KNX_TELEGRAM_DB_BACKEND, CONF_KNX_TELEGRAM_DB_POSTGRES_DSN as CONF_KNX_TELEGRAM_DB_POSTGRES_DSN, CONF_KNX_TELEGRAM_DB_RETENTION_DAYS as CONF_KNX_TELEGRAM_DB_RETENTION_DAYS, KNXConfigEntryOptions as KNXConfigEntryOptions, KNX_TELEGRAM_BACKEND_POSTGRES as KNX_TELEGRAM_BACKEND_POSTGRES, KNX_TELEGRAM_DB_PATH_SQLITE as KNX_TELEGRAM_DB_PATH_SQLITE, SIGNAL_KNX_DATA_SECURE_ISSUE_TELEGRAM as SIGNAL_KNX_DATA_SECURE_ISSUE_TELEGRAM, SIGNAL_KNX_TELEGRAM as SIGNAL_KNX_TELEGRAM
from .project import KNXProject as KNXProject
from .repairs import async_create_telegram_storage_issue as async_create_telegram_storage_issue, async_delete_telegram_storage_issue as async_delete_telegram_storage_issue
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_change as async_track_time_change
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR, Store as Store
from knx_telegram_store import BufferedPostgresStore, BufferedSqliteStore, StoredTelegram
from typing import TypedDict
from xknx import XKNX as XKNX
from xknx.dpt import DPTArray as DPTArray, DPTBase, DPTBinary as DPTBinary
from xknx.dpt.dpt import DPTComplexData, DPTEnumData
from xknx.telegram import Telegram as Telegram

_LOGGER: Incomplete
EVICT_EXPIRED_HOUR: int
FLUSH_INTERVAL_SECONDS: int
MAX_BUFFER_TELEGRAMS: Incomplete
STORE_INIT_TIMEOUT: int
STORE_INIT_RETRY_BACKOFF: Incomplete
STORE_INIT_MAX_RETRIES: Incomplete

class DecodedTelegramPayload(TypedDict):
    dpt_main: int | None
    dpt_sub: int | None
    dpt_name: str | None
    unit: str | None
    value: bool | str | int | float | dict[str, str | int | float | bool] | None

class TelegramDict(DecodedTelegramPayload):
    data_secure: bool | None
    destination: str
    destination_name: str
    direction: str
    payload: int | tuple[int, ...] | None
    source: str
    source_name: str
    telegramtype: str
    timestamp: str

class Telegrams:
    hass: Incomplete
    project: Incomplete
    config: Incomplete
    backend: str
    dsn: str
    retention_days: int
    store: BufferedSqliteStore | BufferedPostgresStore | None
    _uninitialized_store: BufferedSqliteStore | BufferedPostgresStore | None
    _evict_expired_unsub: CALLBACK_TYPE | None
    _store_init_retry_unsub: CALLBACK_TYPE | None
    _store_init_retry_task: asyncio.Task[None] | None
    _store_init_attempts: int
    _xknx_telegram_cb_handle: Incomplete
    _xknx_data_secure_group_key_issue_cb_handle: Incomplete
    last_ga_telegrams: dict[str, TelegramDict]
    def __init__(self, hass: HomeAssistant, xknx: XKNX, project: KNXProject, config: KNXConfigEntryOptions) -> None: ...
    async def load_history(self) -> None: ...
    async def _async_retry_load_history(self, now: datetime) -> None: ...
    async def _abort_store_init(self) -> None: ...
    async def _async_evict_expired(self, now: datetime) -> None: ...
    async def stop(self) -> None: ...
    def _xknx_telegram_cb(self, telegram: Telegram) -> None: ...
    def _xknx_data_secure_group_key_issue_cb(self, telegram: Telegram) -> None: ...
    def telegram_to_dict(self, telegram: Telegram) -> TelegramDict: ...
    def dict_to_model(self, t: TelegramDict) -> StoredTelegram: ...
    async def migrate_telegrams(self) -> None: ...
    def model_to_dict(self, m: StoredTelegram) -> TelegramDict: ...
    def _resolve_dpt(self, main: int | None, sub: int | None) -> tuple[str | None, str | None]: ...

def _serializable_decoded_data(value: bool | float | str | DPTComplexData | DPTEnumData) -> bool | str | int | float | dict[str, str | int | float | bool]: ...
def decode_telegram_payload(payload: DPTArray | DPTBinary, transcoder: type[DPTBase]) -> DecodedTelegramPayload: ...
