from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping, Sequence
from functools import cached_property as cached_property
from homeassistant.const import EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import MAX_LOAD_CONCURRENTLY as MAX_LOAD_CONCURRENTLY, bind_hass as bind_hass
from homeassistant.util.file import WriteError as WriteError
from json import JSONEncoder
from typing import Any, Generic, TypeVar

STORAGE_DIR: str
_LOGGER: Incomplete
STORAGE_SEMAPHORE: str
_T = TypeVar('_T', bound=Mapping[str, Any] | Sequence[Any])

async def async_migrator(hass: HomeAssistant, old_path: str, store: Store[_T], *, old_conf_load_func: Callable | None = None, old_conf_migrate_func: Callable | None = None) -> _T | None: ...

class Store(Generic[_T]):
    version: Incomplete
    minor_version: Incomplete
    key: Incomplete
    hass: Incomplete
    _private: Incomplete
    _data: Incomplete
    _delay_handle: Incomplete
    _unsub_final_write_listener: Incomplete
    _write_lock: Incomplete
    _load_task: Incomplete
    _encoder: Incomplete
    _atomic_writes: Incomplete
    _read_only: Incomplete
    _next_write_time: float
    def __init__(self, hass: HomeAssistant, version: int, key: str, private: bool = False, *, atomic_writes: bool = False, encoder: type[JSONEncoder] | None = None, minor_version: int = 1, read_only: bool = False) -> None: ...
    @cached_property
    def path(self): ...
    async def async_load(self) -> _T | None: ...
    async def _async_load(self) -> _T | None: ...
    async def _async_load_data(self): ...
    async def async_save(self, data: _T) -> None: ...
    def async_delay_save(self, data_func: Callable[[], _T], delay: float = 0) -> None: ...
    def _async_reschedule_delayed_write(self, when: float) -> None: ...
    def _async_schedule_callback_delayed_write(self) -> None: ...
    def _async_ensure_final_write_listener(self) -> None: ...
    def _async_cleanup_final_write_listener(self) -> None: ...
    def _async_cleanup_delay_listener(self) -> None: ...
    async def _async_callback_delayed_write(self) -> None: ...
    async def _async_callback_final_write(self, _event: Event) -> None: ...
    async def _async_handle_write_data(self, *_args) -> None: ...
    async def _async_write_data(self, path: str, data: dict) -> None: ...
    def _write_data(self, path: str, data: dict) -> None: ...
    async def _async_migrate_func(self, old_major_version, old_minor_version, old_data) -> None: ...
    async def async_remove(self) -> None: ...
