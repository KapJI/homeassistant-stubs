import asyncio
import datetime
import enum
import threading
import voluptuous as vol
from . import block_async_io as block_async_io, util as util
from .auth import AuthManager as AuthManager
from .components.http import ApiConfig as ApiConfig, HomeAssistantHTTP as HomeAssistantHTTP
from .config_entries import ConfigEntries as ConfigEntries
from .const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_SERVICE as ATTR_SERVICE, ATTR_SERVICE_DATA as ATTR_SERVICE_DATA, COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_CONTEXT as COMPRESSED_STATE_CONTEXT, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_STATE_REPORTED as EVENT_STATE_REPORTED, MATCH_ALL as MATCH_ALL, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, UnitOfLength as UnitOfLength, __version__ as __version__
from .exceptions import HomeAssistantError as HomeAssistantError, InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, MaxLengthExceeded as MaxLengthExceeded, ServiceNotFound as ServiceNotFound, Unauthorized as Unauthorized
from .helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from .helpers.entity import StateInfo as StateInfo
from .helpers.json import json_bytes as json_bytes, json_fragment as json_fragment
from .helpers.storage import Store as Store
from .util import location as location
from .util.async_ import cancelling as cancelling, create_eager_task as create_eager_task, run_callback_threadsafe as run_callback_threadsafe, shutdown_run_callback_threadsafe as shutdown_run_callback_threadsafe
from .util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from .util.json import JsonObjectType as JsonObjectType
from .util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from .util.timeout import TimeoutManager as TimeoutManager
from .util.ulid import ulid_at_time as ulid_at_time, ulid_now as ulid_now
from .util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM, UnitSystem as UnitSystem, _CONF_UNIT_SYSTEM_IMPERIAL as _CONF_UNIT_SYSTEM_IMPERIAL, _CONF_UNIT_SYSTEM_US_CUSTOMARY as _CONF_UNIT_SYSTEM_US_CUSTOMARY, get_unit_system as get_unit_system
from _typeshed import Incomplete
from collections import UserDict
from collections.abc import Callable, Collection, Coroutine, Iterable, KeysView, Mapping, ValuesView
from dataclasses import dataclass
from functools import cached_property as cached_property
from typing import Any, Generic, Literal, NotRequired, ParamSpec, Self, TypeVarTuple, TypedDict, overload
from typing_extensions import TypeVar

STOPPING_STAGE_SHUTDOWN_TIMEOUT: int
STOP_STAGE_SHUTDOWN_TIMEOUT: int
FINAL_WRITE_STAGE_SHUTDOWN_TIMEOUT: int
CLOSE_STAGE_SHUTDOWN_TIMEOUT: int
_T = TypeVar('_T')
_R = TypeVar('_R')
_R_co = TypeVar('_R_co', covariant=True)
_P = ParamSpec('_P')
_Ts = TypeVarTuple('_Ts')
_UNDEF: dict[Any, Any]
_CallableT = TypeVar('_CallableT', bound=Callable[..., Any])
_DataT = TypeVar('_DataT', bound=Mapping[str, Any], default=Mapping[str, Any])
CALLBACK_TYPE = Callable[[], None]
CORE_STORAGE_KEY: str
CORE_STORAGE_VERSION: int
CORE_STORAGE_MINOR_VERSION: int
DOMAIN: str
BLOCK_LOG_TIMEOUT: int
ServiceResponse: Incomplete
EntityServiceResponse = dict[str, ServiceResponse]

class ConfigSource(enum.StrEnum):
    DEFAULT: str
    DISCOVERED: str
    STORAGE: str
    YAML: str

_DEPRECATED_SOURCE_DISCOVERED: Incomplete
_DEPRECATED_SOURCE_STORAGE: Incomplete
_DEPRECATED_SOURCE_YAML: Incomplete
TIMEOUT_EVENT_START: int
MAX_EXPECTED_ENTITY_IDS: int
EVENTS_EXCLUDED_FROM_MATCH_ALL: Incomplete
_LOGGER: Incomplete

def split_entity_id(entity_id: str) -> tuple[str, str]: ...

_OBJECT_ID: str
_DOMAIN: Incomplete
VALID_DOMAIN: Incomplete
VALID_ENTITY_ID: Incomplete

def valid_domain(domain: str) -> bool: ...
def valid_entity_id(entity_id: str) -> bool: ...
def validate_state(state: str) -> str: ...
def callback(func: _CallableT) -> _CallableT: ...
def is_callback(func: Callable[..., Any]) -> bool: ...
def is_callback_check_partial(target: Callable[..., Any]) -> bool: ...

class _Hass(threading.local):
    hass: HomeAssistant | None

_hass: Incomplete

def async_get_hass() -> HomeAssistant: ...
def get_release_channel() -> Literal['beta', 'dev', 'nightly', 'stable']: ...

class HassJobType(enum.Enum):
    Coroutinefunction: int
    Callback: int
    Executor: int

class HassJob(Generic[_P, _R_co]):
    target: Incomplete
    name: Incomplete
    _cancel_on_shutdown: Incomplete
    _job_type: Incomplete
    def __init__(self, target: Callable[_P, _R_co], name: str | None = None, *, cancel_on_shutdown: bool | None = None, job_type: HassJobType | None = None) -> None: ...
    @cached_property
    def job_type(self) -> HassJobType: ...
    @property
    def cancel_on_shutdown(self) -> bool | None: ...
    def __repr__(self) -> str: ...

@dataclass(frozen=True)
class HassJobWithArgs:
    job: HassJob[..., Coroutine[Any, Any, Any] | Any]
    args: Iterable[Any]
    def __init__(self, job, args) -> None: ...

def get_hassjob_callable_job_type(target: Callable[..., Any]) -> HassJobType: ...

class CoreState(enum.Enum):
    not_running: str
    starting: str
    running: str
    stopping: str
    final_write: str
    stopped: str
    def __str__(self) -> str: ...

class HomeAssistant:
    auth: AuthManager
    http: HomeAssistantHTTP
    config_entries: ConfigEntries
    def __new__(cls, config_dir: str) -> HomeAssistant: ...
    def __repr__(self) -> str: ...
    data: Incomplete
    loop: Incomplete
    _tasks: Incomplete
    _background_tasks: Incomplete
    bus: Incomplete
    services: Incomplete
    states: Incomplete
    config: Incomplete
    components: Incomplete
    helpers: Incomplete
    state: Incomplete
    exit_code: int
    _stopped: Incomplete
    timeout: Incomplete
    _stop_future: Incomplete
    _shutdown_jobs: Incomplete
    import_executor: Incomplete
    def __init__(self, config_dir: str) -> None: ...
    @property
    def _active_tasks(self) -> set[asyncio.Future[Any]]: ...
    @cached_property
    def is_running(self) -> bool: ...
    @cached_property
    def is_stopping(self) -> bool: ...
    def set_state(self, state: CoreState) -> None: ...
    def start(self) -> int: ...
    async def async_run(self, *, attach_signals: bool = True) -> int: ...
    async def async_start(self) -> None: ...
    def add_job(self, target: Callable[[Unpack[_Ts]], Any] | Coroutine[Any, Any, Any], *args: Unpack[_Ts]) -> None: ...
    @overload
    def async_add_job(self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R]], *args: Unpack[_Ts], eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job(self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R] | _R], *args: Unpack[_Ts], eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job(self, target: Coroutine[Any, Any, _R], *args: Any, eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any, eager_start: bool = False, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any, eager_start: bool = False, background: bool = False) -> asyncio.Future[_R] | None: ...
    def create_task(self, target: Coroutine[Any, Any, Any], name: str | None = None) -> None: ...
    def async_create_task(self, target: Coroutine[Any, Any, _R], name: str | None = None, eager_start: bool = False) -> asyncio.Task[_R]: ...
    def async_create_background_task(self, target: Coroutine[Any, Any, _R], name: str, eager_start: bool = False) -> asyncio.Task[_R]: ...
    def async_add_executor_job(self, target: Callable[[Unpack[_Ts]], _T], *args: Unpack[_Ts]) -> asyncio.Future[_T]: ...
    def async_add_import_executor_job(self, target: Callable[[Unpack[_Ts]], _T], *args: Unpack[_Ts]) -> asyncio.Future[_T]: ...
    @overload
    def async_run_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_hass_job(self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R]], *args: Unpack[_Ts]) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R] | _R], *args: Unpack[_Ts]) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job(self, target: Coroutine[Any, Any, _R], *args: Any) -> asyncio.Future[_R] | None: ...
    def block_till_done(self) -> None: ...
    async def async_block_till_done(self, wait_background_tasks: bool = False) -> None: ...
    async def _await_and_log_pending(self, pending: Collection[asyncio.Future[Any]]) -> None: ...
    @overload
    def async_add_shutdown_job(self, hassjob: HassJob[..., Coroutine[Any, Any, Any]], *args: Any) -> CALLBACK_TYPE: ...
    @overload
    def async_add_shutdown_job(self, hassjob: HassJob[..., Coroutine[Any, Any, Any] | Any], *args: Any) -> CALLBACK_TYPE: ...
    def stop(self) -> None: ...
    async def async_stop(self, exit_code: int = 0, *, force: bool = False) -> None: ...
    def _cancel_cancellable_timers(self) -> None: ...
    def _async_log_running_tasks(self, stage: str) -> None: ...

class Context:
    id: Incomplete
    user_id: Incomplete
    parent_id: Incomplete
    origin_event: Incomplete
    def __init__(self, user_id: str | None = None, parent_id: str | None = None, id: str | None = None) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @cached_property
    def _as_dict(self) -> dict[str, str | None]: ...
    def as_dict(self) -> ReadOnlyDict[str, str | None]: ...
    @cached_property
    def _as_read_only_dict(self) -> ReadOnlyDict[str, str | None]: ...
    @cached_property
    def json_fragment(self) -> json_fragment: ...

class EventOrigin(enum.Enum):
    local: str
    remote: str
    def __str__(self) -> str: ...

class Event(Generic[_DataT]):
    event_type: Incomplete
    data: Incomplete
    origin: Incomplete
    time_fired_timestamp: Incomplete
    context: Incomplete
    def __init__(self, event_type: str, data: _DataT | None = None, origin: EventOrigin = ..., time_fired_timestamp: float | None = None, context: Context | None = None) -> None: ...
    @cached_property
    def time_fired(self) -> datetime.datetime: ...
    @cached_property
    def _as_dict(self) -> dict[str, Any]: ...
    def as_dict(self) -> ReadOnlyDict[str, Any]: ...
    @cached_property
    def _as_read_only_dict(self) -> ReadOnlyDict[str, Any]: ...
    @cached_property
    def json_fragment(self) -> json_fragment: ...
    def __repr__(self) -> str: ...

def _event_repr(event_type: str, origin: EventOrigin, data: Mapping[str, Any] | None) -> str: ...

_FilterableJobType: Incomplete

@dataclass(slots=True)
class _OneTimeListener:
    hass: HomeAssistant
    listener_job: HassJob[[Event], Coroutine[Any, Any, None] | None]
    remove: CALLBACK_TYPE | None = ...
    def __call__(self, event: Event) -> None: ...
    def __repr__(self) -> str: ...
    def __init__(self, hass, listener_job, remove) -> None: ...

EMPTY_LIST: list[Any]

class EventBus:
    __slots__: Incomplete
    _listeners: Incomplete
    _match_all_listeners: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    _debug: Incomplete
    def _async_logging_changed(self, event: Event | None = None) -> None: ...
    def async_listeners(self) -> dict[str, int]: ...
    @property
    def listeners(self) -> dict[str, int]: ...
    def fire(self, event_type: str, event_data: Mapping[str, Any] | None = None, origin: EventOrigin = ..., context: Context | None = None) -> None: ...
    def async_fire(self, event_type: str, event_data: Mapping[str, Any] | None = None, origin: EventOrigin = ..., context: Context | None = None, time_fired: float | None = None) -> None: ...
    def _async_fire(self, event_type: str, event_data: Mapping[str, Any] | None = None, origin: EventOrigin = ..., context: Context | None = None, time_fired: float | None = None) -> None: ...
    def listen(self, event_type: str, listener: Callable[[Event[Any]], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen(self, event_type: str, listener: Callable[[Event[_DataT]], Coroutine[Any, Any, None] | None], event_filter: Callable[[_DataT], bool] | None = None, run_immediately: bool = False) -> CALLBACK_TYPE: ...
    def _async_listen_filterable_job(self, event_type: str, filterable_job: _FilterableJobType[Any]) -> CALLBACK_TYPE: ...
    def listen_once(self, event_type: str, listener: Callable[[Event[Any]], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen_once(self, event_type: str, listener: Callable[[Event[Any]], Coroutine[Any, Any, None] | None], run_immediately: bool = False) -> CALLBACK_TYPE: ...
    def _async_remove_listener(self, event_type: str, filterable_job: _FilterableJobType) -> None: ...

class CompressedState(TypedDict):
    s: str
    a: ReadOnlyDict[str, Any]
    c: str | dict[str, Any]
    lc: float
    lu: NotRequired[float]

class State:
    entity_id: Incomplete
    state: Incomplete
    attributes: Incomplete
    last_reported: Incomplete
    last_updated: Incomplete
    last_changed: Incomplete
    context: Incomplete
    state_info: Incomplete
    def __init__(self, entity_id: str, state: str, attributes: Mapping[str, Any] | None = None, last_changed: datetime.datetime | None = None, last_reported: datetime.datetime | None = None, last_updated: datetime.datetime | None = None, context: Context | None = None, validate_entity_id: bool | None = True, state_info: StateInfo | None = None) -> None: ...
    @cached_property
    def name(self) -> str: ...
    @cached_property
    def last_changed_timestamp(self) -> float: ...
    @cached_property
    def last_reported_timestamp(self) -> float: ...
    @cached_property
    def last_updated_timestamp(self) -> float: ...
    @cached_property
    def _as_dict(self) -> dict[str, Any]: ...
    def as_dict(self) -> ReadOnlyDict[str, datetime.datetime | Collection[Any]]: ...
    @cached_property
    def _as_read_only_dict(self) -> ReadOnlyDict[str, datetime.datetime | Collection[Any]]: ...
    @cached_property
    def as_dict_json(self) -> bytes: ...
    @cached_property
    def json_fragment(self) -> json_fragment: ...
    @cached_property
    def as_compressed_state(self) -> CompressedState: ...
    @cached_property
    def as_compressed_state_json(self) -> bytes: ...
    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Self | None: ...
    def expire(self) -> None: ...
    def __repr__(self) -> str: ...

class States(UserDict[str, State]):
    _domain_index: Incomplete
    def __init__(self) -> None: ...
    def values(self) -> ValuesView[State]: ...
    def __setitem__(self, key: str, entry: State) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def domain_entity_ids(self, key: str) -> KeysView[str] | tuple: ...
    def domain_states(self, key: str) -> ValuesView[State] | tuple: ...

class StateMachine:
    __slots__: Incomplete
    _states: Incomplete
    _states_data: Incomplete
    _reservations: Incomplete
    _bus: Incomplete
    _loop: Incomplete
    def __init__(self, bus: EventBus, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def entity_ids(self, domain_filter: str | None = None) -> list[str]: ...
    def async_entity_ids(self, domain_filter: str | Iterable[str] | None = None) -> list[str]: ...
    def async_entity_ids_count(self, domain_filter: str | Iterable[str] | None = None) -> int: ...
    def all(self, domain_filter: str | Iterable[str] | None = None) -> list[State]: ...
    def async_all(self, domain_filter: str | Iterable[str] | None = None) -> list[State]: ...
    def get(self, entity_id: str) -> State | None: ...
    def is_state(self, entity_id: str, state: str) -> bool: ...
    def remove(self, entity_id: str) -> bool: ...
    def async_remove(self, entity_id: str, context: Context | None = None) -> bool: ...
    def set(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None = None, force_update: bool = False, context: Context | None = None) -> None: ...
    def async_reserve(self, entity_id: str) -> None: ...
    def async_available(self, entity_id: str) -> bool: ...
    def async_set(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None = None, force_update: bool = False, context: Context | None = None, state_info: StateInfo | None = None) -> None: ...

class SupportsResponse(enum.StrEnum):
    NONE: str
    OPTIONAL: str
    ONLY: str

class Service:
    __slots__: Incomplete
    job: Incomplete
    schema: Incomplete
    supports_response: Incomplete
    def __init__(self, func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse | EntityServiceResponse] | ServiceResponse | EntityServiceResponse | None], schema: vol.Schema | None, domain: str, service: str, context: Context | None = None, supports_response: SupportsResponse = ..., job_type: HassJobType | None = None) -> None: ...

class ServiceCall:
    __slots__: Incomplete
    domain: Incomplete
    service: Incomplete
    data: Incomplete
    context: Incomplete
    return_response: Incomplete
    def __init__(self, domain: str, service: str, data: dict[str, Any] | None = None, context: Context | None = None, return_response: bool = False) -> None: ...
    def __repr__(self) -> str: ...

class ServiceRegistry:
    __slots__: Incomplete
    _services: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def services(self) -> dict[str, dict[str, Service]]: ...
    def async_services(self) -> dict[str, dict[str, Service]]: ...
    def async_services_for_domain(self, domain: str) -> dict[str, Service]: ...
    def async_services_internal(self) -> dict[str, dict[str, Service]]: ...
    def has_service(self, domain: str, service: str) -> bool: ...
    def supports_response(self, domain: str, service: str) -> SupportsResponse: ...
    def register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse] | ServiceResponse | None], schema: vol.Schema | None = None, supports_response: SupportsResponse = ...) -> None: ...
    def async_register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse | EntityServiceResponse] | ServiceResponse | EntityServiceResponse | None], schema: vol.Schema | None = None, supports_response: SupportsResponse = ..., job_type: HassJobType | None = None) -> None: ...
    def remove(self, domain: str, service: str) -> None: ...
    def async_remove(self, domain: str, service: str) -> None: ...
    def call(self, domain: str, service: str, service_data: dict[str, Any] | None = None, blocking: bool = False, context: Context | None = None, target: dict[str, Any] | None = None, return_response: bool = False) -> ServiceResponse: ...
    async def async_call(self, domain: str, service: str, service_data: dict[str, Any] | None = None, blocking: bool = False, context: Context | None = None, target: dict[str, Any] | None = None, return_response: bool = False) -> ServiceResponse: ...
    async def _run_service_call_catch_exceptions(self, coro_or_task: Coroutine[Any, Any, Any] | asyncio.Task[Any], service_call: ServiceCall) -> None: ...
    async def _execute_service(self, handler: Service, service_call: ServiceCall) -> ServiceResponse: ...

class Config:
    _store: Config._ConfigStore
    hass: Incomplete
    latitude: int
    longitude: int
    elevation: int
    location_name: str
    time_zone: str
    units: Incomplete
    internal_url: Incomplete
    external_url: Incomplete
    currency: str
    country: Incomplete
    language: str
    config_source: Incomplete
    skip_pip: bool
    skip_pip_packages: Incomplete
    components: Incomplete
    api: Incomplete
    config_dir: Incomplete
    allowlist_external_dirs: Incomplete
    allowlist_external_urls: Incomplete
    media_dirs: Incomplete
    recovery_mode: bool
    legacy_templates: bool
    safe_mode: bool
    def __init__(self, hass: HomeAssistant, config_dir: str) -> None: ...
    def async_initialize(self) -> None: ...
    def distance(self, lat: float, lon: float) -> float | None: ...
    def path(self, *path: str) -> str: ...
    def is_allowed_external_url(self, url: str) -> bool: ...
    def is_allowed_path(self, path: str) -> bool: ...
    def as_dict(self) -> dict[str, Any]: ...
    def set_time_zone(self, time_zone_str: str) -> None: ...
    def _update(self, *, source: ConfigSource, latitude: float | None = None, longitude: float | None = None, elevation: int | None = None, unit_system: str | None = None, location_name: str | None = None, time_zone: str | None = None, external_url: str | dict[Any, Any] | None = ..., internal_url: str | dict[Any, Any] | None = ..., currency: str | None = None, country: str | dict[Any, Any] | None = ..., language: str | None = None) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
    async def async_load(self) -> None: ...
    async def _async_store(self) -> None: ...
    class _ConfigStore(Store[dict[str, Any]]):
        _original_unit_system: Incomplete
        def __init__(self, hass: HomeAssistant) -> None: ...
        async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...
        async def async_save(self, data: dict[str, Any]) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
