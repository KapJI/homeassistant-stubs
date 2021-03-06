import asyncio
import datetime
import enum
import voluptuous as vol
from collections.abc import Awaitable, Coroutine, Iterable, Mapping
from homeassistant import block_async_io as block_async_io, loader as loader, util as util
from homeassistant.auth import AuthManager as AuthManager
from homeassistant.components.http import HomeAssistantHTTP as HomeAssistantHTTP
from homeassistant.config_entries import ConfigEntries as ConfigEntries
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_NOW as ATTR_NOW, ATTR_SECONDS as ATTR_SECONDS, ATTR_SERVICE as ATTR_SERVICE, ATTR_SERVICE_DATA as ATTR_SERVICE_DATA, CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_TIMER_OUT_OF_SYNC as EVENT_TIMER_OUT_OF_SYNC, EVENT_TIME_CHANGED as EVENT_TIME_CHANGED, LENGTH_METERS as LENGTH_METERS, MATCH_ALL as MATCH_ALL, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, __version__ as __version__
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, InvalidEntityFormatError as InvalidEntityFormatError, InvalidStateError as InvalidStateError, MaxLengthExceeded as MaxLengthExceeded, ServiceNotFound as ServiceNotFound, Unauthorized as Unauthorized
from homeassistant.util import location as location
from homeassistant.util.async_ import fire_coroutine_threadsafe as fire_coroutine_threadsafe, run_callback_threadsafe as run_callback_threadsafe, shutdown_run_callback_threadsafe as shutdown_run_callback_threadsafe
from homeassistant.util.timeout import TimeoutManager as TimeoutManager
from homeassistant.util.unit_system import IMPERIAL_SYSTEM as IMPERIAL_SYSTEM, METRIC_SYSTEM as METRIC_SYSTEM, UnitSystem as UnitSystem
from typing import Any, Callable, TypeVar

STAGE_1_SHUTDOWN_TIMEOUT: int
STAGE_2_SHUTDOWN_TIMEOUT: int
STAGE_3_SHUTDOWN_TIMEOUT: int
T = TypeVar('T')
_UNDEF: dict
CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable)
CALLBACK_TYPE = Callable[[], None]
CORE_STORAGE_KEY: str
CORE_STORAGE_VERSION: int
DOMAIN: str
BLOCK_LOG_TIMEOUT: int
SERVICE_CALL_LIMIT: int
SOURCE_DISCOVERED: str
SOURCE_STORAGE: str
SOURCE_YAML: str
TIMEOUT_EVENT_START: int
_LOGGER: Any

def split_entity_id(entity_id: str) -> list[str]: ...

VALID_ENTITY_ID: Any

def valid_entity_id(entity_id: str) -> bool: ...
def valid_state(state: str) -> bool: ...
def callback(func: CALLABLE_T) -> CALLABLE_T: ...
def is_callback(func: Callable[..., Any]) -> bool: ...

class HassJobType(enum.Enum):
    Coroutinefunction: int
    Callback: int
    Executor: int

class HassJob:
    __slots__: Any
    target: Any
    job_type: Any
    def __init__(self, target: Callable) -> None: ...
    def __repr__(self) -> str: ...

def _get_callable_job_type(target: Callable) -> HassJobType: ...

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
    loop: Any
    _pending_tasks: Any
    _track_task: bool
    bus: Any
    services: Any
    states: Any
    config: Any
    components: Any
    helpers: Any
    data: Any
    state: Any
    exit_code: int
    _stopped: Any
    timeout: Any
    def __init__(self) -> None: ...
    @property
    def is_running(self) -> bool: ...
    @property
    def is_stopping(self) -> bool: ...
    def start(self) -> int: ...
    async def async_run(self, *, attach_signals: bool = ...) -> int: ...
    async def async_start(self) -> None: ...
    def add_job(self, target: Callable[..., Any], *args: Any) -> None: ...
    def async_add_job(self, target: Callable[..., Any], *args: Any) -> Union[asyncio.Future, None]: ...
    def async_add_hass_job(self, hassjob: HassJob, *args: Any) -> Union[asyncio.Future, None]: ...
    def create_task(self, target: Awaitable) -> None: ...
    def async_create_task(self, target: Awaitable) -> asyncio.Task: ...
    def async_add_executor_job(self, target: Callable[..., T], *args: Any) -> Awaitable[T]: ...
    def async_track_tasks(self) -> None: ...
    def async_stop_track_tasks(self) -> None: ...
    def async_run_hass_job(self, hassjob: HassJob, *args: Any) -> Union[asyncio.Future, None]: ...
    def async_run_job(self, target: Callable[..., Union[None, Awaitable]], *args: Any) -> Union[asyncio.Future, None]: ...
    def block_till_done(self) -> None: ...
    async def async_block_till_done(self) -> None: ...
    async def _await_and_log_pending(self, pending: Iterable[Awaitable[Any]]) -> None: ...
    def stop(self) -> None: ...
    async def async_stop(self, exit_code: int = ..., *, force: bool = ...) -> None: ...

class Context:
    user_id: str
    parent_id: Union[str, None]
    id: str
    def as_dict(self) -> dict[str, Union[str, None]]: ...
    def __init__(self, user_id, parent_id, id) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class EventOrigin(enum.Enum):
    local: str
    remote: str
    def __str__(self) -> str: ...

class Event:
    __slots__: Any
    event_type: Any
    data: Any
    origin: Any
    time_fired: Any
    context: Any
    def __init__(self, event_type: str, data: Union[dict[str, Any], None] = ..., origin: EventOrigin = ..., time_fired: Union[datetime.datetime, None] = ..., context: Union[Context, None] = ...) -> None: ...
    def __hash__(self) -> int: ...
    def as_dict(self) -> dict[str, Any]: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...

class EventBus:
    _listeners: Any
    _hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_listeners(self) -> dict[str, int]: ...
    @property
    def listeners(self) -> dict[str, int]: ...
    def fire(self, event_type: str, event_data: Union[dict, None] = ..., origin: EventOrigin = ..., context: Union[Context, None] = ...) -> None: ...
    def async_fire(self, event_type: str, event_data: Union[dict[str, Any], None] = ..., origin: EventOrigin = ..., context: Union[Context, None] = ..., time_fired: Union[datetime.datetime, None] = ...) -> None: ...
    def listen(self, event_type: str, listener: Callable) -> CALLBACK_TYPE: ...
    def async_listen(self, event_type: str, listener: Callable, event_filter: Union[Callable, None] = ...) -> CALLBACK_TYPE: ...
    def _async_listen_filterable_job(self, event_type: str, filterable_job: tuple[HassJob, Union[Callable, None]]) -> CALLBACK_TYPE: ...
    def listen_once(self, event_type: str, listener: Callable[[Event], None]) -> CALLBACK_TYPE: ...
    def async_listen_once(self, event_type: str, listener: Callable) -> CALLBACK_TYPE: ...
    def _async_remove_listener(self, event_type: str, filterable_job: tuple[HassJob, Union[Callable, None]]) -> None: ...

class State:
    __slots__: Any
    entity_id: Any
    state: Any
    attributes: Any
    last_updated: Any
    last_changed: Any
    context: Any
    _as_dict: Any
    def __init__(self, entity_id: str, state: str, attributes: Union[Mapping[str, Any], None] = ..., last_changed: Union[datetime.datetime, None] = ..., last_updated: Union[datetime.datetime, None] = ..., context: Union[Context, None] = ..., validate_entity_id: Union[bool, None] = ...) -> None: ...
    @property
    def name(self) -> str: ...
    def as_dict(self) -> dict: ...
    @classmethod
    def from_dict(cls, json_dict: dict) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...

class StateMachine:
    _states: Any
    _reservations: Any
    _bus: Any
    _loop: Any
    def __init__(self, bus: EventBus, loop: asyncio.events.AbstractEventLoop) -> None: ...
    def entity_ids(self, domain_filter: Union[str, None] = ...) -> list[str]: ...
    def async_entity_ids(self, domain_filter: Union[str, Iterable, None] = ...) -> list[str]: ...
    def async_entity_ids_count(self, domain_filter: Union[str, Iterable, None] = ...) -> int: ...
    def all(self, domain_filter: Union[str, Iterable, None] = ...) -> list[State]: ...
    def async_all(self, domain_filter: Union[str, Iterable, None] = ...) -> list[State]: ...
    def get(self, entity_id: str) -> Union[State, None]: ...
    def is_state(self, entity_id: str, state: str) -> bool: ...
    def remove(self, entity_id: str) -> bool: ...
    def async_remove(self, entity_id: str, context: Union[Context, None] = ...) -> bool: ...
    def set(self, entity_id: str, new_state: str, attributes: Union[Mapping[str, Any], None] = ..., force_update: bool = ..., context: Union[Context, None] = ...) -> None: ...
    def async_reserve(self, entity_id: str) -> None: ...
    def async_available(self, entity_id: str) -> bool: ...
    def async_set(self, entity_id: str, new_state: str, attributes: Union[Mapping[str, Any], None] = ..., force_update: bool = ..., context: Union[Context, None] = ...) -> None: ...

class Service:
    __slots__: Any
    job: Any
    schema: Any
    def __init__(self, func: Callable, schema: Union[vol.Schema, None], context: Union[Context, None] = ...) -> None: ...

class ServiceCall:
    __slots__: Any
    domain: Any
    service: Any
    data: Any
    context: Any
    def __init__(self, domain: str, service: str, data: Union[dict, None] = ..., context: Union[Context, None] = ...) -> None: ...
    def __repr__(self) -> str: ...

class ServiceRegistry:
    _services: Any
    _hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def services(self) -> dict[str, dict[str, Service]]: ...
    def async_services(self) -> dict[str, dict[str, Service]]: ...
    def has_service(self, domain: str, service: str) -> bool: ...
    def register(self, domain: str, service: str, service_func: Callable, schema: Union[vol.Schema, None] = ...) -> None: ...
    def async_register(self, domain: str, service: str, service_func: Callable, schema: Union[vol.Schema, None] = ...) -> None: ...
    def remove(self, domain: str, service: str) -> None: ...
    def async_remove(self, domain: str, service: str) -> None: ...
    def call(self, domain: str, service: str, service_data: Union[dict, None] = ..., blocking: bool = ..., context: Union[Context, None] = ..., limit: Union[float, None] = ..., target: Union[dict, None] = ...) -> Union[bool, None]: ...
    async def async_call(self, domain: str, service: str, service_data: Union[dict, None] = ..., blocking: bool = ..., context: Union[Context, None] = ..., limit: Union[float, None] = ..., target: Union[dict, None] = ...) -> Union[bool, None]: ...
    def _run_service_in_background(self, coro_or_task: Union[Coroutine, asyncio.Task], service_call: ServiceCall) -> None: ...
    async def _execute_service(self, handler: Service, service_call: ServiceCall) -> None: ...

class Config:
    hass: Any
    latitude: int
    longitude: int
    elevation: int
    location_name: str
    time_zone: str
    units: Any
    internal_url: Any
    external_url: Any
    currency: str
    config_source: str
    skip_pip: bool
    components: Any
    api: Any
    config_dir: Any
    allowlist_external_dirs: Any
    allowlist_external_urls: Any
    media_dirs: Any
    safe_mode: bool
    legacy_templates: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    def distance(self, lat: float, lon: float) -> Union[float, None]: ...
    def path(self, *path: str) -> str: ...
    def is_allowed_external_url(self, url: str) -> bool: ...
    def is_allowed_path(self, path: str) -> bool: ...
    def as_dict(self) -> dict: ...
    def set_time_zone(self, time_zone_str: str) -> None: ...
    def _update(self, source: str, *, latitude: Union[float, None] = ..., longitude: Union[float, None] = ..., elevation: Union[int, None] = ..., unit_system: Union[str, None] = ..., location_name: Union[str, None] = ..., time_zone: Union[str, None] = ..., external_url: Union[str, dict, None] = ..., internal_url: Union[str, dict, None] = ..., currency: Union[str, None] = ...) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
    async def async_load(self) -> None: ...
    async def async_store(self) -> None: ...

def _async_create_timer(hass: HomeAssistant) -> None: ...
