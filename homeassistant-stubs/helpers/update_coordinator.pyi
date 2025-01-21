import abc
import asyncio
import logging
from . import entity as entity, event as event
from .debounce import Debouncer as Debouncer
from .frame import report_usage as report_usage
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Awaitable, Callable as Callable, Coroutine, Generator
from datetime import datetime, timedelta
from homeassistant import config_entries as config_entries
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.util.dt import utcnow as utcnow
from propcache import cached_property
from typing import Any, Generic, Protocol
from typing_extensions import TypeVar

REQUEST_REFRESH_DEFAULT_COOLDOWN: int
REQUEST_REFRESH_DEFAULT_IMMEDIATE: bool
_DataT = TypeVar('_DataT', default=dict[str, Any])
_DataUpdateCoordinatorT = TypeVar('_DataUpdateCoordinatorT', bound='DataUpdateCoordinator[Any]', default='DataUpdateCoordinator[dict[str, Any]]')

class UpdateFailed(HomeAssistantError): ...

class BaseDataUpdateCoordinatorProtocol(Protocol):
    @callback
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = None) -> Callable[[], None]: ...

class DataUpdateCoordinator(BaseDataUpdateCoordinatorProtocol, Generic[_DataT]):
    hass: Incomplete
    logger: Incomplete
    name: Incomplete
    update_method: Incomplete
    setup_method: Incomplete
    _update_interval_seconds: float | None
    _shutdown_requested: bool
    config_entry: Incomplete
    always_update: Incomplete
    data: _DataT
    _microsecond: Incomplete
    _listeners: dict[CALLBACK_TYPE, tuple[CALLBACK_TYPE, object | None]]
    _unsub_refresh: CALLBACK_TYPE | None
    _unsub_shutdown: CALLBACK_TYPE | None
    _request_refresh_task: asyncio.TimerHandle | None
    last_update_success: bool
    last_exception: Exception | None
    _debounced_refresh: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, config_entry: config_entries.ConfigEntry | None | UndefinedType = ..., name: str, update_interval: timedelta | None = None, update_method: Callable[[], Awaitable[_DataT]] | None = None, setup_method: Callable[[], Awaitable[None]] | None = None, request_refresh_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = None, always_update: bool = True) -> None: ...
    async def async_register_shutdown(self) -> None: ...
    @callback
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = None) -> Callable[[], None]: ...
    @callback
    def async_update_listeners(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    @callback
    def _unschedule_refresh(self) -> None: ...
    def async_contexts(self) -> Generator[Any]: ...
    def _async_unsub_refresh(self) -> None: ...
    def _async_unsub_shutdown(self) -> None: ...
    @property
    def update_interval(self) -> timedelta | None: ...
    _update_interval: Incomplete
    @update_interval.setter
    def update_interval(self, value: timedelta | None) -> None: ...
    @callback
    def _schedule_refresh(self) -> None: ...
    @callback
    def __wrap_handle_refresh_interval(self) -> None: ...
    async def _handle_refresh_interval(self, _now: datetime | None = None) -> None: ...
    async def async_request_refresh(self) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    async def async_config_entry_first_refresh(self) -> None: ...
    async def __wrap_async_setup(self) -> bool: ...
    async def _async_setup(self) -> None: ...
    async def async_refresh(self) -> None: ...
    async def _async_refresh(self, log_failures: bool = True, raise_on_auth_failed: bool = False, scheduled: bool = False, raise_on_entry_error: bool = False) -> None: ...
    @callback
    def _async_refresh_finished(self) -> None: ...
    @callback
    def async_set_update_error(self, err: Exception) -> None: ...
    @callback
    def async_set_updated_data(self, data: _DataT) -> None: ...

class TimestampDataUpdateCoordinator(DataUpdateCoordinator[_DataT]):
    last_update_success_time: datetime | None
    @callback
    def _async_refresh_finished(self) -> None: ...

class BaseCoordinatorEntity[_BaseDataUpdateCoordinatorT: BaseDataUpdateCoordinatorProtocol](entity.Entity, metaclass=abc.ABCMeta):
    coordinator: Incomplete
    coordinator_context: Incomplete
    def __init__(self, coordinator: _BaseDataUpdateCoordinatorT, context: Any = None) -> None: ...
    @cached_property
    def should_poll(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    async def async_update(self) -> None: ...

class CoordinatorEntity(BaseCoordinatorEntity[_DataUpdateCoordinatorT]):
    def __init__(self, coordinator: _DataUpdateCoordinatorT, context: Any = None) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
