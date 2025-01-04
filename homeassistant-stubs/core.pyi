import asyncio
import datetime
import enum
import threading
import voluptuous as vol
from . import util as util
from .auth import AuthManager as AuthManager
from .components.http import HomeAssistantHTTP as HomeAssistantHTTP
from .config_entries import ConfigEntries as ConfigEntries
from .const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_SERVICE as ATTR_SERVICE, ATTR_SERVICE_DATA as ATTR_SERVICE_DATA, COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_CONTEXT as COMPRESSED_STATE_CONTEXT, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_STATE_REPORTED as EVENT_STATE_REPORTED, MATCH_ALL as MATCH_ALL, MAX_EXPECTED_ENTITY_IDS as MAX_EXPECTED_ENTITY_IDS, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, __version__ as __version__
from .exceptions import HomeAssistantError as HomeAssistantError, InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, MaxLengthExceeded as MaxLengthExceeded, ServiceNotFound as ServiceNotFound, ServiceValidationError as ServiceValidationError, Unauthorized as Unauthorized
from .helpers.deprecation import DeferredDeprecatedAlias as DeferredDeprecatedAlias, EnumWithDeprecatedMembers as EnumWithDeprecatedMembers, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from .helpers.entity import StateInfo as StateInfo
from .helpers.json import json_bytes as json_bytes, json_fragment as json_fragment
from .helpers.typing import VolSchemaType as VolSchemaType
from .util.async_ import cancelling as cancelling, create_eager_task as create_eager_task, get_scheduled_timer_handles as get_scheduled_timer_handles, run_callback_threadsafe as run_callback_threadsafe, shutdown_run_callback_threadsafe as shutdown_run_callback_threadsafe
from .util.event_type import EventType as EventType
from .util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from .util.hass_dict import HassDict as HassDict
from .util.json import JsonObjectType as JsonObjectType
from .util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from .util.timeout import TimeoutManager as TimeoutManager
from .util.ulid import ulid_at_time as ulid_at_time, ulid_now as ulid_now
from _typeshed import Incomplete
from collections import UserDict
from collections.abc import Callable, Collection, Coroutine, Iterable, KeysView, Mapping, ValuesView
from dataclasses import dataclass
from typing import Any, Generic, NotRequired, Self, TypedDict, overload
from typing_extensions import TypeVar

STOPPING_STAGE_SHUTDOWN_TIMEOUT: int
STOP_STAGE_SHUTDOWN_TIMEOUT: int
FINAL_WRITE_STAGE_SHUTDOWN_TIMEOUT: int
CLOSE_STAGE_SHUTDOWN_TIMEOUT: int
_SENTINEL: Incomplete
_DataT = TypeVar('_DataT', bound=Mapping[str, Any], default=Mapping[str, Any])
type CALLBACK_TYPE = Callable[[], None]
DOMAIN: str
BLOCK_LOG_TIMEOUT: int
type ServiceResponse = JsonObjectType | None
type EntityServiceResponse = dict[str, ServiceResponse]

class ConfigSource(enum.StrEnum, deprecated={'DEFAULT': ('core_config.ConfigSource.DEFAULT', '2025.11.0'), 'DISCOVERED': ('core_config.ConfigSource.DISCOVERED', '2025.11.0'), 'STORAGE': ('core_config.ConfigSource.STORAGE', '2025.11.0'), 'YAML': ('core_config.ConfigSource.YAML', '2025.11.0')}, metaclass=EnumWithDeprecatedMembers):
    DEFAULT = 'default'
    DISCOVERED = 'discovered'
    STORAGE = 'storage'
    YAML = 'yaml'

class EventStateEventData(TypedDict):
    entity_id: str
    new_state: State | None

class EventStateChangedData(EventStateEventData):
    old_state: State | None

class EventStateReportedData(EventStateEventData):
    old_last_reported: datetime.datetime

def _deprecated_core_config() -> Any: ...

_DEPRECATED_Config: Incomplete
TIMEOUT_EVENT_START: int
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
def callback[_CallableT: Callable[..., Any]](func: _CallableT) -> _CallableT: ...
def is_callback(func: Callable[..., Any]) -> bool: ...
def is_callback_check_partial(target: Callable[..., Any]) -> bool: ...

class _Hass(threading.local):
    hass: HomeAssistant | None

_hass: Incomplete

def async_get_hass() -> HomeAssistant: ...
def async_get_hass_or_none() -> HomeAssistant | None: ...

class ReleaseChannel(enum.StrEnum):
    BETA = 'beta'
    DEV = 'dev'
    NIGHTLY = 'nightly'
    STABLE = 'stable'

def get_release_channel() -> ReleaseChannel: ...

class HassJobType(enum.Enum):
    Coroutinefunction = 1
    Callback = 2
    Executor = 3

class HassJob[**_P, _R_co]:
    __slots__: Incomplete
    target: Incomplete
    name: Incomplete
    _cancel_on_shutdown: Incomplete
    _cache: Incomplete
    def __init__(self, target: Callable[_P, _R_co], name: str | None = None, *, cancel_on_shutdown: bool | None = None, job_type: HassJobType | None = None) -> None: ...
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
    not_running = 'NOT_RUNNING'
    starting = 'STARTING'
    running = 'RUNNING'
    stopping = 'STOPPING'
    final_write = 'FINAL_WRITE'
    stopped = 'STOPPED'
    def __str__(self) -> str: ...

class HomeAssistant:
    auth: AuthManager
    http: HomeAssistantHTTP
    config_entries: ConfigEntries
    def __new__(cls, config_dir: str) -> Self: ...
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
    loop_thread_id: Incomplete
    def __init__(self, config_dir: str) -> None: ...
    def verify_event_loop_thread(self, what: str) -> None: ...
    @property
    def _active_tasks(self) -> set[asyncio.Future[Any]]: ...
    def is_running(self) -> bool: ...
    def is_stopping(self) -> bool: ...
    def set_state(self, state: CoreState) -> None: ...
    def start(self) -> int: ...
    async def async_run(self, *, attach_signals: bool = True) -> int: ...
    async def async_start(self) -> None: ...
    def add_job[*_Ts](self, target: Callable[[Unpack[_Ts]], Any] | Coroutine[Any, Any, Any], *args: Unpack[_Ts]) -> None: ...
    @overload
    def async_add_job[_R, *_Ts](self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R]], *args: Unpack[_Ts], eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job[_R, *_Ts](self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R] | _R], *args: Unpack[_Ts], eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_job[_R](self, target: Coroutine[Any, Any, _R], *args: Any, eager_start: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any, eager_start: bool = False, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_add_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any, eager_start: bool = False, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def _async_add_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def _async_add_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    def create_task(self, target: Coroutine[Any, Any, Any], name: str | None = None) -> None: ...
    def async_create_task[_R](self, target: Coroutine[Any, Any, _R], name: str | None = None, eager_start: bool = True) -> asyncio.Task[_R]: ...
    def async_create_task_internal[_R](self, target: Coroutine[Any, Any, _R], name: str | None = None, eager_start: bool = True) -> asyncio.Task[_R]: ...
    def async_create_background_task[_R](self, target: Coroutine[Any, Any, _R], name: str, eager_start: bool = True) -> asyncio.Task[_R]: ...
    def async_add_executor_job[*_Ts, _T](self, target: Callable[[Unpack[_Ts]], _T], *args: Unpack[_Ts]) -> asyncio.Future[_T]: ...
    def async_add_import_executor_job[*_Ts, _T](self, target: Callable[[Unpack[_Ts]], _T], *args: Unpack[_Ts]) -> asyncio.Future[_T]: ...
    @overload
    def async_run_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R]], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_hass_job[_R](self, hassjob: HassJob[..., Coroutine[Any, Any, _R] | _R], *args: Any, background: bool = False) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job[_R, *_Ts](self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R]], *args: Unpack[_Ts]) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job[_R, *_Ts](self, target: Callable[[Unpack[_Ts]], Coroutine[Any, Any, _R] | _R], *args: Unpack[_Ts]) -> asyncio.Future[_R] | None: ...
    @overload
    def async_run_job[_R](self, target: Coroutine[Any, Any, _R], *args: Any) -> asyncio.Future[_R] | None: ...
    def block_till_done(self, wait_background_tasks: bool = False) -> None: ...
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
    __slots__: Incomplete
    id: Incomplete
    user_id: Incomplete
    parent_id: Incomplete
    origin_event: Incomplete
    _cache: Incomplete
    def __init__(self, user_id: str | None = None, parent_id: str | None = None, id: str | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __copy__(self) -> Context: ...
    def __deepcopy__(self, memo: dict[int, Any]) -> Context: ...
    def _as_dict(self) -> dict[str, str | None]: ...
    def as_dict(self) -> ReadOnlyDict[str, str | None]: ...
    def _as_read_only_dict(self) -> ReadOnlyDict[str, str | None]: ...
    def json_fragment(self) -> json_fragment: ...

class EventOrigin(enum.Enum):
    local = 'LOCAL'
    remote = 'REMOTE'
    def __str__(self) -> str: ...
    def idx(self) -> int: ...

class Event(Generic[_DataT]):
    __slots__: Incomplete
    event_type: Incomplete
    data: Incomplete
    origin: Incomplete
    time_fired_timestamp: Incomplete
    context: Incomplete
    _cache: Incomplete
    def __init__(self, event_type: EventType[_DataT] | str, data: _DataT | None = None, origin: EventOrigin = ..., time_fired_timestamp: float | None = None, context: Context | None = None) -> None: ...
    def time_fired(self) -> datetime.datetime: ...
    def _as_dict(self) -> dict[str, Any]: ...
    def as_dict(self) -> ReadOnlyDict[str, Any]: ...
    def _as_read_only_dict(self) -> ReadOnlyDict[str, Any]: ...
    def json_fragment(self) -> json_fragment: ...
    def __repr__(self) -> str: ...

def _event_repr(event_type: EventType[_DataT] | str, origin: EventOrigin, data: _DataT | None) -> str: ...

_FilterableJobType: Incomplete

@dataclass(slots=True)
class _OneTimeListener(Generic[_DataT]):
    hass: HomeAssistant
    listener_job: HassJob[[Event[_DataT]], Coroutine[Any, Any, None] | None]
    remove: CALLBACK_TYPE | None = ...
    def __call__(self, event: Event[_DataT]) -> None: ...
    def __repr__(self) -> str: ...
    def __init__(self, hass, listener_job, remove=...) -> None: ...

EMPTY_LIST: list[Any]

def _verify_event_type_length_or_raise(event_type: EventType[_DataT] | str) -> None: ...

class EventBus:
    __slots__: Incomplete
    _listeners: Incomplete
    _match_all_listeners: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    _debug: Incomplete
    def _async_logging_changed(self, event: Event | None = None) -> None: ...
    def async_listeners(self) -> dict[EventType[Any] | str, int]: ...
    @property
    def listeners(self) -> dict[EventType[Any] | str, int]: ...
    def fire(self, event_type: EventType[_DataT] | str, event_data: _DataT | None = None, origin: EventOrigin = ..., context: Context | None = None) -> None: ...
    def async_fire(self, event_type: EventType[_DataT] | str, event_data: _DataT | None = None, origin: EventOrigin = ..., context: Context | None = None, time_fired: float | None = None) -> None: ...
    def async_fire_internal(self, event_type: EventType[_DataT] | str, event_data: _DataT | None = None, origin: EventOrigin = ..., context: Context | None = None, time_fired: float | None = None) -> None: ...
    def listen(self, event_type: EventType[_DataT] | str, listener: Callable[[Event[_DataT]], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen(self, event_type: EventType[_DataT] | str, listener: Callable[[Event[_DataT]], Coroutine[Any, Any, None] | None], event_filter: Callable[[_DataT], bool] | None = None, run_immediately: bool | object = ...) -> CALLBACK_TYPE: ...
    def _async_listen_filterable_job(self, event_type: EventType[_DataT] | str, filterable_job: _FilterableJobType[_DataT]) -> CALLBACK_TYPE: ...
    def listen_once(self, event_type: EventType[_DataT] | str, listener: Callable[[Event[_DataT]], Coroutine[Any, Any, None] | None]) -> CALLBACK_TYPE: ...
    def async_listen_once(self, event_type: EventType[_DataT] | str, listener: Callable[[Event[_DataT]], Coroutine[Any, Any, None] | None], run_immediately: bool | object = ...) -> CALLBACK_TYPE: ...
    def _async_remove_listener(self, event_type: EventType[_DataT] | str, filterable_job: _FilterableJobType[_DataT]) -> None: ...

class CompressedState(TypedDict):
    s: str
    a: ReadOnlyDict[str, Any]
    c: str | dict[str, Any]
    lc: float
    lu: NotRequired[float]

class State:
    __slots__: Incomplete
    _cache: Incomplete
    entity_id: Incomplete
    state: Incomplete
    attributes: Incomplete
    last_reported: Incomplete
    last_updated: Incomplete
    last_changed: Incomplete
    context: Incomplete
    state_info: Incomplete
    last_updated_timestamp: Incomplete
    def __init__(self, entity_id: str, state: str, attributes: Mapping[str, Any] | None = None, last_changed: datetime.datetime | None = None, last_reported: datetime.datetime | None = None, last_updated: datetime.datetime | None = None, context: Context | None = None, validate_entity_id: bool | None = True, state_info: StateInfo | None = None, last_updated_timestamp: float | None = None) -> None: ...
    def name(self) -> str: ...
    def last_changed_timestamp(self) -> float: ...
    def last_reported_timestamp(self) -> float: ...
    def _as_dict(self) -> dict[str, Any]: ...
    def as_dict(self) -> ReadOnlyDict[str, datetime.datetime | Collection[Any]]: ...
    def _as_read_only_dict(self) -> ReadOnlyDict[str, datetime.datetime | Collection[Any]]: ...
    def as_dict_json(self) -> bytes: ...
    def json_fragment(self) -> json_fragment: ...
    def as_compressed_state(self) -> CompressedState: ...
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
    def domain_entity_ids(self, key: str) -> KeysView[str] | tuple[()]: ...
    def domain_states(self, key: str) -> ValuesView[State] | tuple[()]: ...

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
    def async_set(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None = None, force_update: bool = False, context: Context | None = None, state_info: StateInfo | None = None, timestamp: float | None = None) -> None: ...
    def async_set_internal(self, entity_id: str, new_state: str, attributes: Mapping[str, Any] | None, force_update: bool, context: Context | None, state_info: StateInfo | None, timestamp: float) -> None: ...

class SupportsResponse(enum.StrEnum):
    NONE = 'none'
    OPTIONAL = 'optional'
    ONLY = 'only'

class Service:
    __slots__: Incomplete
    job: Incomplete
    schema: Incomplete
    supports_response: Incomplete
    def __init__(self, func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse | EntityServiceResponse] | ServiceResponse | EntityServiceResponse | None], schema: VolSchemaType | None, domain: str, service: str, context: Context | None = None, supports_response: SupportsResponse = ..., job_type: HassJobType | None = None) -> None: ...

class ServiceCall:
    __slots__: Incomplete
    hass: Incomplete
    domain: Incomplete
    service: Incomplete
    data: Incomplete
    context: Incomplete
    return_response: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str, service: str, data: dict[str, Any] | None = None, context: Context | None = None, return_response: bool = False) -> None: ...
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
    def async_register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse | EntityServiceResponse] | ServiceResponse | EntityServiceResponse | None], schema: VolSchemaType | None = None, supports_response: SupportsResponse = ..., job_type: HassJobType | None = None) -> None: ...
    def _async_register(self, domain: str, service: str, service_func: Callable[[ServiceCall], Coroutine[Any, Any, ServiceResponse | EntityServiceResponse] | ServiceResponse | EntityServiceResponse | None], schema: VolSchemaType | None = None, supports_response: SupportsResponse = ..., job_type: HassJobType | None = None) -> None: ...
    def remove(self, domain: str, service: str) -> None: ...
    def async_remove(self, domain: str, service: str) -> None: ...
    def _async_remove(self, domain: str, service: str) -> None: ...
    def call(self, domain: str, service: str, service_data: dict[str, Any] | None = None, blocking: bool = False, context: Context | None = None, target: dict[str, Any] | None = None, return_response: bool = False) -> ServiceResponse: ...
    async def async_call(self, domain: str, service: str, service_data: dict[str, Any] | None = None, blocking: bool = False, context: Context | None = None, target: dict[str, Any] | None = None, return_response: bool = False) -> ServiceResponse: ...
    async def _run_service_call_catch_exceptions(self, coro_or_task: Coroutine[Any, Any, Any] | asyncio.Task[Any], service_call: ServiceCall) -> None: ...
    async def _execute_service(self, handler: Service, service_call: ServiceCall) -> ServiceResponse: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
