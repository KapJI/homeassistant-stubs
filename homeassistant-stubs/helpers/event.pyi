from collections.abc import Awaitable, Iterable
from datetime import datetime, timedelta
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NOW as ATTR_NOW, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_TIME_CHANGED as EVENT_TIME_CHANGED, MATCH_ALL as MATCH_ALL, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity_registry import EVENT_ENTITY_REGISTRY_UPDATED as EVENT_ENTITY_REGISTRY_UPDATED
from homeassistant.helpers.ratelimit import KeyedRateLimit as KeyedRateLimit
from homeassistant.helpers.sun import get_astral_event_next as get_astral_event_next
from homeassistant.helpers.template import RenderInfo as RenderInfo, Template as Template, result_as_boolean as result_as_boolean
from homeassistant.helpers.typing import TemplateVarsType as TemplateVarsType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import dt as dt_util
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any, Callable, List

TRACK_STATE_CHANGE_CALLBACKS: str
TRACK_STATE_CHANGE_LISTENER: str
TRACK_STATE_ADDED_DOMAIN_CALLBACKS: str
TRACK_STATE_ADDED_DOMAIN_LISTENER: str
TRACK_STATE_REMOVED_DOMAIN_CALLBACKS: str
TRACK_STATE_REMOVED_DOMAIN_LISTENER: str
TRACK_ENTITY_REGISTRY_UPDATED_CALLBACKS: str
TRACK_ENTITY_REGISTRY_UPDATED_LISTENER: str
_ALL_LISTENER: str
_DOMAINS_LISTENER: str
_ENTITIES_LISTENER: str
_LOGGER: Any

class TrackStates:
    all_states: bool
    entities: set[str]
    domains: set[str]

class TrackTemplate:
    template: Template
    variables: TemplateVarsType
    rate_limit: Union[timedelta, None]

class TrackTemplateResult:
    template: Template
    last_result: Any
    result: Any

def threaded_listener_factory(async_factory: Callable[..., Any]) -> Callable[..., CALLBACK_TYPE]: ...
def async_track_state_change(hass: HomeAssistant, entity_ids: Union[str, Iterable[str]], action: Callable[[str, State, State], Union[Awaitable[None], None]], from_state: Union[None, str, Iterable[str]] = ..., to_state: Union[None, str, Iterable[str]] = ...) -> CALLBACK_TYPE: ...

track_state_change: Any

def async_track_state_change_event(hass: HomeAssistant, entity_ids: Union[str, Iterable[str]], action: Callable[[Event], Any]) -> Callable[[], None]: ...
def _remove_empty_listener() -> None: ...
def _async_remove_indexed_listeners(hass: HomeAssistant, data_key: str, listener_key: str, storage_keys: Iterable[str], job: HassJob) -> None: ...
def async_track_entity_registry_updated_event(hass: HomeAssistant, entity_ids: Union[str, Iterable[str]], action: Callable[[Event], Any]) -> Callable[[], None]: ...
def _async_dispatch_domain_event(hass: HomeAssistant, event: Event, callbacks: dict[str, list[HassJob]]) -> None: ...
def async_track_state_added_domain(hass: HomeAssistant, domains: Union[str, Iterable[str]], action: Callable[[Event], Any]) -> Callable[[], None]: ...
def async_track_state_removed_domain(hass: HomeAssistant, domains: Union[str, Iterable[str]], action: Callable[[Event], Any]) -> Callable[[], None]: ...
def _async_string_to_lower_list(instr: Union[str, Iterable[str]]) -> list[str]: ...

class _TrackStateChangeFiltered:
    hass: Any
    _action: Any
    _listeners: Any
    _last_track_states: Any
    def __init__(self, hass: HomeAssistant, track_states: TrackStates, action: Callable[[Event], Any]) -> None: ...
    def async_setup(self) -> None: ...
    @property
    def listeners(self) -> dict: ...
    def async_update_listeners(self, new_track_states: TrackStates) -> None: ...
    def async_remove(self) -> None: ...
    def _cancel_listener(self, listener_name: str) -> None: ...
    def _setup_entities_listener(self, domains: set[str], entities: set[str]) -> None: ...
    def _setup_domains_listener(self, domains: set[str]) -> None: ...
    def _setup_all_listener(self) -> None: ...

def async_track_state_change_filtered(hass: HomeAssistant, track_states: TrackStates, action: Callable[[Event], Any]) -> _TrackStateChangeFiltered: ...
def async_track_template(hass: HomeAssistant, template: Template, action: Callable[[str, Union[State, None], Union[State, None]], Union[Awaitable[None], None]], variables: Union[TemplateVarsType, None] = ...) -> Callable[[], None]: ...

track_template: Any

class _TrackTemplateResultInfo:
    hass: Any
    _job: Any
    _track_templates: Any
    _last_result: Any
    _rate_limit: Any
    _info: Any
    _track_state_changes: Any
    _time_listeners: Any
    def __init__(self, hass: HomeAssistant, track_templates: Iterable[TrackTemplate], action: Callable) -> None: ...
    def async_setup(self, raise_on_template_error: bool, strict: bool = ...) -> None: ...
    @property
    def listeners(self) -> dict: ...
    def _setup_time_listener(self, template: Template, has_time: bool) -> None: ...
    def _update_time_listeners(self) -> None: ...
    def async_remove(self) -> None: ...
    def async_refresh(self) -> None: ...
    def _render_template_if_ready(self, track_template_: TrackTemplate, now: datetime, event: Union[Event, None]) -> Union[bool, TrackTemplateResult]: ...
    def _refresh(self, event: Union[Event, None], track_templates: Union[Iterable[TrackTemplate], None] = ..., replayed: Union[bool, None] = ...) -> None: ...
TrackTemplateResultListener = Callable[[Event, List[TrackTemplateResult]], None]

def async_track_template_result(hass: HomeAssistant, track_templates: Iterable[TrackTemplate], action: TrackTemplateResultListener, raise_on_template_error: bool = ..., strict: bool = ...) -> _TrackTemplateResultInfo: ...
def async_track_same_state(hass: HomeAssistant, period: timedelta, action: Callable[..., Union[Awaitable[None], None]], async_check_same_func: Callable[[str, Union[State, None], Union[State, None]], bool], entity_ids: Union[str, Iterable[str]] = ...) -> CALLBACK_TYPE: ...

track_same_state: Any

def async_track_point_in_time(hass: HomeAssistant, action: Union[HassJob, Callable[..., Union[Awaitable[None], None]]], point_in_time: datetime) -> CALLBACK_TYPE: ...

track_point_in_time: Any

def async_track_point_in_utc_time(hass: HomeAssistant, action: Union[HassJob, Callable[..., Union[Awaitable[None], None]]], point_in_time: datetime) -> CALLBACK_TYPE: ...

track_point_in_utc_time: Any

def async_call_later(hass: HomeAssistant, delay: Union[float, timedelta], action: Union[HassJob, Callable[..., Union[Awaitable[None], None]]]) -> CALLBACK_TYPE: ...

call_later: Any

def async_track_time_interval(hass: HomeAssistant, action: Callable[..., Union[Awaitable[None], None]], interval: timedelta) -> CALLBACK_TYPE: ...

track_time_interval: Any

class SunListener:
    hass: HomeAssistant
    job: HassJob
    event: str
    offset: Union[timedelta, None]
    _unsub_sun: Union[CALLBACK_TYPE, None]
    _unsub_config: Union[CALLBACK_TYPE, None]
    def async_attach(self) -> None: ...
    def async_detach(self) -> None: ...
    def _listen_next_sun_event(self) -> None: ...
    def _handle_sun_event(self, _now: Any) -> None: ...
    def _handle_config_event(self, _event: Any) -> None: ...
    def __init__(self, hass, job, event, offset, unsub_sun, unsub_config) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def async_track_sunrise(hass: HomeAssistant, action: Callable[..., None], offset: Union[timedelta, None] = ...) -> CALLBACK_TYPE: ...

track_sunrise: Any

def async_track_sunset(hass: HomeAssistant, action: Callable[..., None], offset: Union[timedelta, None] = ...) -> CALLBACK_TYPE: ...

track_sunset: Any
time_tracker_utcnow = dt_util.utcnow

def async_track_utc_time_change(hass: HomeAssistant, action: Callable[..., Union[Awaitable[None], None]], hour: Union[Any, None] = ..., minute: Union[Any, None] = ..., second: Union[Any, None] = ..., local: bool = ...) -> CALLBACK_TYPE: ...

track_utc_time_change: Any

def async_track_time_change(hass: HomeAssistant, action: Callable[..., None], hour: Union[Any, None] = ..., minute: Union[Any, None] = ..., second: Union[Any, None] = ...) -> CALLBACK_TYPE: ...

track_time_change: Any

def process_state_match(parameter: Union[None, str, Iterable[str]]) -> Callable[[Union[str, None]], bool]: ...
def _entities_domains_from_render_infos(render_infos: Iterable[RenderInfo]) -> tuple[set[str], set[str]]: ...
def _render_infos_needs_all_listener(render_infos: Iterable[RenderInfo]) -> bool: ...
def _render_infos_to_track_states(render_infos: Iterable[RenderInfo]) -> TrackStates: ...
def _event_triggers_rerender(event: Event, info: RenderInfo) -> bool: ...
def _rate_limit_for_event(event: Event, info: RenderInfo, track_template_: TrackTemplate) -> Union[timedelta, None]: ...
def _suppress_domain_all_in_render_info(render_info: RenderInfo) -> RenderInfo: ...
