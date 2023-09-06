import jinja2
from . import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry
from .singleton import singleton as singleton
from .typing import TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Iterable, MutableMapping
from contextvars import ContextVar
from datetime import datetime, timedelta
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_PERSONS as ATTR_PERSONS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfLength as UnitOfLength
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_domain as valid_domain, valid_entity_id as valid_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import convert as convert
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from homeassistant.util.thread import ThreadWithException as ThreadWithException
from jinja2.sandbox import ImmutableSandboxedEnvironment
from types import CodeType
from typing import Any, Literal, NoReturn, TypeVar, overload

_LOGGER: Incomplete
_SENTINEL: Incomplete
DATE_STR_FORMAT: str
_ENVIRONMENT: str
_ENVIRONMENT_LIMITED: str
_ENVIRONMENT_STRICT: str
_HASS_LOADER: str
_RE_JINJA_DELIMITERS: Incomplete
_IS_NUMERIC: Incomplete
_RESERVED_NAMES: Incomplete
_GROUP_DOMAIN_PREFIX: str
_ZONE_DOMAIN_PREFIX: str
_COLLECTABLE_STATE_ATTRIBUTES: Incomplete
_T = TypeVar('_T')
_R = TypeVar('_R')
_P: Incomplete
ALL_STATES_RATE_LIMIT: Incomplete
DOMAIN_STATES_RATE_LIMIT: Incomplete
_render_info: ContextVar[RenderInfo | None]
template_cv: ContextVar[tuple[str, str] | None]
CACHED_TEMPLATE_STATES: int
EVAL_CACHE_SIZE: int
MAX_CUSTOM_TEMPLATE_SIZE: Incomplete
CACHED_TEMPLATE_LRU: MutableMapping[State, TemplateState]
CACHED_TEMPLATE_NO_COLLECT_LRU: MutableMapping[State, TemplateState]
ENTITY_COUNT_GROWTH_FACTOR: float
ORJSON_PASSTHROUGH_OPTIONS: Incomplete

def _template_state_no_collect(hass: HomeAssistant, state: State) -> TemplateState: ...
def _template_state(hass: HomeAssistant, state: State) -> TemplateState: ...
def async_setup(hass: HomeAssistant) -> bool: ...
def attach(hass: HomeAssistant, obj: Any) -> None: ...
def render_complex(value: Any, variables: TemplateVarsType = ..., limited: bool = ..., parse_result: bool = ...) -> Any: ...
def is_complex(value: Any) -> bool: ...
def is_template_string(maybe_template: str) -> bool: ...

class ResultWrapper:
    render_result: str | None

def gen_result_wrapper(kls: type[dict | list | set]) -> type: ...

class TupleWrapper(tuple, ResultWrapper):
    def __new__(cls, value: tuple, *, render_result: str | None = ...) -> TupleWrapper: ...
    render_result: Incomplete
    def __init__(self, value: tuple, *, render_result: str | None = ...) -> None: ...
    def __str__(self) -> str: ...

_types: tuple[type[dict | list | set], ...]
RESULT_WRAPPERS: dict[type, type]

def _true(arg: str) -> bool: ...
def _false(arg: str) -> bool: ...

_cached_literal_eval: Incomplete

class RenderInfo:
    __slots__: Incomplete
    template: Incomplete
    filter_lifecycle: Incomplete
    filter: Incomplete
    _result: Incomplete
    is_static: bool
    exception: Incomplete
    all_states: bool
    all_states_lifecycle: bool
    domains: Incomplete
    domains_lifecycle: Incomplete
    entities: Incomplete
    rate_limit: Incomplete
    has_time: bool
    def __init__(self, template: Template) -> None: ...
    def __repr__(self) -> str: ...
    def _filter_domains_and_entities(self, entity_id: str) -> bool: ...
    def _filter_entities(self, entity_id: str) -> bool: ...
    def _filter_lifecycle_domains(self, entity_id: str) -> bool: ...
    def result(self) -> str: ...
    def _freeze_static(self) -> None: ...
    def _freeze_sets(self) -> None: ...
    def _freeze(self) -> None: ...

class Template:
    __slots__: Incomplete
    template: Incomplete
    _compiled_code: Incomplete
    _compiled: Incomplete
    hass: Incomplete
    is_static: Incomplete
    _exc_info: Incomplete
    _limited: Incomplete
    _strict: Incomplete
    _hash_cache: Incomplete
    _renders: int
    def __init__(self, template: str, hass: HomeAssistant | None = ...) -> None: ...
    @property
    def _env(self) -> TemplateEnvironment: ...
    def ensure_valid(self) -> None: ...
    def render(self, variables: TemplateVarsType = ..., parse_result: bool = ..., limited: bool = ..., **kwargs: Any) -> Any: ...
    def async_render(self, variables: TemplateVarsType = ..., parse_result: bool = ..., limited: bool = ..., strict: bool = ..., **kwargs: Any) -> Any: ...
    def _parse_result(self, render_result: str) -> Any: ...
    async def async_render_will_timeout(self, timeout: float, variables: TemplateVarsType = ..., strict: bool = ..., **kwargs: Any) -> bool: ...
    def async_render_to_info(self, variables: TemplateVarsType = ..., strict: bool = ..., **kwargs: Any) -> RenderInfo: ...
    def render_with_possible_json_value(self, value, error_value=...): ...
    def async_render_with_possible_json_value(self, value: Any, error_value: Any = ..., variables: dict[str, Any] | None = ...) -> Any: ...
    def _ensure_compiled(self, limited: bool = ..., strict: bool = ...) -> jinja2.Template: ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

def _domain_states(hass: HomeAssistant, name: str) -> DomainStates: ...
def _readonly(*args: Any, **kwargs: Any) -> Any: ...

class AllStates:
    __setitem__ = _readonly
    __delitem__ = _readonly
    __slots__: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, name): ...
    __getitem__ = __getattr__
    def _collect_all(self) -> None: ...
    def _collect_all_lifecycle(self) -> None: ...
    def __iter__(self) -> Generator[TemplateState, None, None]: ...
    def __len__(self) -> int: ...
    def __call__(self, entity_id: str, rounded: bool | object = ..., with_unit: bool = ...) -> str: ...
    def __repr__(self) -> str: ...

class DomainStates:
    __slots__: Incomplete
    __setitem__ = _readonly
    __delitem__ = _readonly
    _hass: Incomplete
    _domain: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str) -> None: ...
    def __getattr__(self, name: str) -> TemplateState | None: ...
    __getitem__ = __getattr__
    def _collect_domain(self) -> None: ...
    def _collect_domain_lifecycle(self) -> None: ...
    def __iter__(self) -> Generator[TemplateState, None, None]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

class TemplateStateBase(State):
    __slots__: Incomplete
    _state: State
    __setitem__ = _readonly
    __delitem__ = _readonly
    _hass: Incomplete
    _collect: Incomplete
    _entity_id: Incomplete
    _as_dict: Incomplete
    def __init__(self, hass: HomeAssistant, collect: bool, entity_id: str) -> None: ...
    def _collect_state(self) -> None: ...
    def __getitem__(self, item: str) -> Any: ...
    @property
    def entity_id(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def attributes(self) -> ReadOnlyDict[str, Any]: ...
    @property
    def last_changed(self) -> datetime: ...
    @property
    def last_updated(self) -> datetime: ...
    @property
    def context(self) -> Context: ...
    @property
    def domain(self) -> str: ...
    @property
    def object_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def state_with_unit(self) -> str: ...
    def format_state(self, rounded: bool, with_unit: bool) -> str: ...
    def __eq__(self, other: Any) -> bool: ...

class TemplateState(TemplateStateBase):
    __slots__: Incomplete
    _state: Incomplete
    def __init__(self, hass: HomeAssistant, state: State, collect: bool = ...) -> None: ...
    def __repr__(self) -> str: ...

class TemplateStateFromEntityId(TemplateStateBase):
    def __init__(self, hass: HomeAssistant, entity_id: str, collect: bool = ...) -> None: ...
    @property
    def _state(self) -> State: ...
    def __repr__(self) -> str: ...

_create_template_state_no_collect: Incomplete

def _collect_state(hass: HomeAssistant, entity_id: str) -> None: ...
def _state_generator(hass: HomeAssistant, domain: str | None) -> Generator[TemplateState, None, None]: ...
def _get_state_if_valid(hass: HomeAssistant, entity_id: str) -> TemplateState | None: ...
def _get_state(hass: HomeAssistant, entity_id: str) -> TemplateState | None: ...
def _get_template_state_from_state(hass: HomeAssistant, entity_id: str, state: State | None) -> TemplateState | None: ...
def _resolve_state(hass: HomeAssistant, entity_id_or_state: Any) -> State | TemplateState | None: ...
@overload
def forgiving_boolean(value: Any) -> bool | object: ...
@overload
def forgiving_boolean(value: Any, default: _T) -> bool | _T: ...
def result_as_boolean(template_result: Any | None) -> bool: ...
def expand(hass: HomeAssistant, *args: Any) -> Iterable[State]: ...
def device_entities(hass: HomeAssistant, _device_id: str) -> Iterable[str]: ...
def integration_entities(hass: HomeAssistant, entry_name: str) -> Iterable[str]: ...
def config_entry_id(hass: HomeAssistant, entity_id: str) -> str | None: ...
def device_id(hass: HomeAssistant, entity_id_or_device_name: str) -> str | None: ...
def device_attr(hass: HomeAssistant, device_or_entity_id: str, attr_name: str) -> Any: ...
def is_device_attr(hass: HomeAssistant, device_or_entity_id: str, attr_name: str, attr_value: Any) -> bool: ...
def areas(hass: HomeAssistant) -> Iterable[str | None]: ...
def area_id(hass: HomeAssistant, lookup_value: str) -> str | None: ...
def _get_area_name(area_reg: area_registry.AreaRegistry, valid_area_id: str) -> str: ...
def area_name(hass: HomeAssistant, lookup_value: str) -> str | None: ...
def area_entities(hass: HomeAssistant, area_id_or_name: str) -> Iterable[str]: ...
def area_devices(hass: HomeAssistant, area_id_or_name: str) -> Iterable[str]: ...
def closest(hass, *args): ...
def closest_filter(hass, *args): ...
def distance(hass, *args): ...
def is_hidden_entity(hass: HomeAssistant, entity_id: str) -> bool: ...
def is_state(hass: HomeAssistant, entity_id: str, state: str | list[str]) -> bool: ...
def is_state_attr(hass: HomeAssistant, entity_id: str, name: str, value: Any) -> bool: ...
def state_attr(hass: HomeAssistant, entity_id: str, name: str) -> Any: ...
def has_value(hass: HomeAssistant, entity_id: str) -> bool: ...
def now(hass: HomeAssistant) -> datetime: ...
def utcnow(hass: HomeAssistant) -> datetime: ...
def raise_no_default(function: str, value: Any) -> NoReturn: ...
def forgiving_round(value, precision: int = ..., method: str = ..., default=...): ...
def multiply(value, amount, default=...): ...
def logarithm(value, base=..., default=...): ...
def sine(value, default=...): ...
def cosine(value, default=...): ...
def tangent(value, default=...): ...
def arc_sine(value, default=...): ...
def arc_cosine(value, default=...): ...
def arc_tangent(value, default=...): ...
def arc_tangent2(*args, default=...): ...
def version(value): ...
def square_root(value, default=...): ...
def timestamp_custom(value, date_format=..., local: bool = ..., default=...): ...
def timestamp_local(value, default=...): ...
def timestamp_utc(value, default=...): ...
def forgiving_as_timestamp(value, default=...): ...
def as_datetime(value): ...
def as_timedelta(value: str) -> timedelta | None: ...
def strptime(string, fmt, default=...): ...
def fail_when_undefined(value): ...
def min_max_from_filter(builtin_filter: Any, name: str) -> Any: ...
def average(*args: Any, default: Any = ...) -> Any: ...
def forgiving_float(value, default=...): ...
def forgiving_float_filter(value, default=...): ...
def forgiving_int(value, default=..., base: int = ...): ...
def forgiving_int_filter(value, default=..., base: int = ...): ...
def is_number(value): ...
def regex_match(value, find: str = ..., ignorecase: bool = ...): ...

_regex_cache: Incomplete

def regex_replace(value: str = ..., find: str = ..., replace: str = ..., ignorecase: bool = ...): ...
def regex_search(value, find: str = ..., ignorecase: bool = ...): ...
def regex_findall_index(value, find: str = ..., index: int = ..., ignorecase: bool = ...): ...
def regex_findall(value, find: str = ..., ignorecase: bool = ...): ...
def bitwise_and(first_value, second_value): ...
def bitwise_or(first_value, second_value): ...
def struct_pack(value: Any | None, format_string: str) -> bytes | None: ...
def struct_unpack(value: bytes, format_string: str, offset: int = ...) -> Any | None: ...
def base64_encode(value): ...
def base64_decode(value): ...
def ordinal(value): ...
def from_json(value): ...
def _to_json_default(obj: Any) -> None: ...
def to_json(value: Any, ensure_ascii: bool = ..., pretty_print: bool = ..., sort_keys: bool = ...) -> str: ...
def random_every_time(context, values): ...
def today_at(hass: HomeAssistant, time_str: str = ...) -> datetime: ...
def relative_time(hass: HomeAssistant, value: Any) -> Any: ...
def urlencode(value): ...
def slugify(value, separator: str = ...): ...
def iif(value: Any, if_true: Any = ..., if_false: Any = ..., if_none: Any = ...) -> Any: ...
def set_template(template_str: str, action: str) -> Generator: ...
def _render_with_context(template_str: str, template: jinja2.Template, **kwargs: Any) -> str: ...

class LoggingUndefined(jinja2.Undefined):
    def _log_message(self) -> None: ...
    def _fail_with_undefined_error(self, *args, **kwargs): ...
    def __str__(self) -> str: ...
    def __iter__(self): ...
    def __bool__(self) -> bool: ...

async def async_load_custom_templates(hass: HomeAssistant) -> None: ...
def _load_custom_templates(hass: HomeAssistant) -> dict[str, str]: ...
def _get_hass_loader(hass: HomeAssistant) -> HassLoader: ...

class HassLoader(jinja2.BaseLoader):
    _sources: Incomplete
    _reload: int
    def __init__(self, sources: dict[str, str]) -> None: ...
    @property
    def sources(self) -> dict[str, str]: ...
    def get_source(self, environment: jinja2.Environment, template: str) -> tuple[str, str | None, Callable[[], bool] | None]: ...

class TemplateEnvironment(ImmutableSandboxedEnvironment):
    hass: Incomplete
    template_cache: Incomplete
    loader: Incomplete
    def __init__(self, hass: HomeAssistant | None, limited: bool | None = ..., strict: bool | None = ...) -> None: ...
    def is_safe_callable(self, obj): ...
    def is_safe_attribute(self, obj, attr, value): ...
    @overload
    def compile(self, source: str | jinja2.nodes.Template, name: str | None = ..., filename: str | None = ..., raw: Literal[False] = ..., defer_init: bool = ...) -> CodeType: ...
    @overload
    def compile(self, source: str | jinja2.nodes.Template, name: str | None = ..., filename: str | None = ..., raw: Literal[True] = ..., defer_init: bool = ...) -> str: ...

_NO_HASS_ENV: Incomplete
