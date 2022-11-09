import jinja2
import re
from . import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry
from .json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from .typing import TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Iterable
from contextvars import ContextVar
from datetime import datetime, timedelta
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_PERSONS as ATTR_PERSONS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, LENGTH_METERS as LENGTH_METERS, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import convert as convert
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from homeassistant.util.thread import ThreadWithException as ThreadWithException
from jinja2.sandbox import ImmutableSandboxedEnvironment
from typing import Any, NoReturn, TypeVar, overload

_LOGGER: Incomplete
_SENTINEL: Incomplete
DATE_STR_FORMAT: str
_RENDER_INFO: str
_ENVIRONMENT: str
_ENVIRONMENT_LIMITED: str
_ENVIRONMENT_STRICT: str
_RE_JINJA_DELIMITERS: Incomplete
_IS_NUMERIC: Incomplete
_RESERVED_NAMES: Incomplete
_GROUP_DOMAIN_PREFIX: str
_ZONE_DOMAIN_PREFIX: str
_COLLECTABLE_STATE_ATTRIBUTES: Incomplete
_T = TypeVar('_T')
ALL_STATES_RATE_LIMIT: Incomplete
DOMAIN_STATES_RATE_LIMIT: Incomplete
template_cv: ContextVar[Union[tuple[str, str], None]]
CACHED_TEMPLATE_STATES: int
EVAL_CACHE_SIZE: int

def attach(hass: HomeAssistant, obj: Any) -> None: ...
def render_complex(value: Any, variables: TemplateVarsType = ..., limited: bool = ..., parse_result: bool = ...) -> Any: ...
def is_complex(value: Any) -> bool: ...
def is_template_string(maybe_template: str) -> bool: ...

class ResultWrapper:
    render_result: Union[str, None]

def gen_result_wrapper(kls): ...

class TupleWrapper(tuple, ResultWrapper):
    def __new__(cls, value: tuple, *, render_result: Union[str, None] = ...) -> TupleWrapper: ...
    render_result: Incomplete
    def __init__(self, value: tuple, *, render_result: Union[str, None] = ...) -> None: ...
    def __str__(self) -> str: ...

RESULT_WRAPPERS: dict[type, type]

def _true(arg: str) -> bool: ...
def _false(arg: str) -> bool: ...

_cached_literal_eval: Incomplete

class RenderInfo:
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
    def __init__(self, template, hass: Incomplete | None = ...) -> None: ...
    @property
    def _env(self) -> TemplateEnvironment: ...
    def ensure_valid(self) -> None: ...
    def render(self, variables: TemplateVarsType = ..., parse_result: bool = ..., limited: bool = ..., **kwargs: Any) -> Any: ...
    def async_render(self, variables: TemplateVarsType = ..., parse_result: bool = ..., limited: bool = ..., strict: bool = ..., **kwargs: Any) -> Any: ...
    def _parse_result(self, render_result: str) -> Any: ...
    async def async_render_will_timeout(self, timeout: float, variables: TemplateVarsType = ..., strict: bool = ..., **kwargs: Any) -> bool: ...
    def async_render_to_info(self, variables: TemplateVarsType = ..., strict: bool = ..., **kwargs: Any) -> RenderInfo: ...
    def render_with_possible_json_value(self, value, error_value=...): ...
    def async_render_with_possible_json_value(self, value, error_value=..., variables: Incomplete | None = ...): ...
    def _ensure_compiled(self, limited: bool = ..., strict: bool = ...) -> jinja2.Template: ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

def _domain_states(hass: HomeAssistant, name: str) -> DomainStates: ...
def _readonly(*args: Any, **kwargs: Any) -> Any: ...

class AllStates:
    __setitem__: Incomplete
    __delitem__: Incomplete
    __slots__: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, name): ...
    __getitem__: Incomplete
    def _collect_all(self) -> None: ...
    def _collect_all_lifecycle(self) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __call__(self, entity_id): ...
    def __repr__(self) -> str: ...

class DomainStates:
    __slots__: Incomplete
    __setitem__: Incomplete
    __delitem__: Incomplete
    _hass: Incomplete
    _domain: Incomplete
    def __init__(self, hass: HomeAssistant, domain: str) -> None: ...
    def __getattr__(self, name): ...
    __getitem__: Incomplete
    def _collect_domain(self) -> None: ...
    def _collect_domain_lifecycle(self) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

class TemplateStateBase(State):
    __slots__: Incomplete
    _state: State
    __setitem__: Incomplete
    __delitem__: Incomplete
    _hass: Incomplete
    _collect: Incomplete
    _entity_id: Incomplete
    _as_dict: Incomplete
    def __init__(self, hass: HomeAssistant, collect: bool, entity_id: str) -> None: ...
    def _collect_state(self) -> None: ...
    def __getitem__(self, item): ...
    @property
    def entity_id(self): ...
    @property
    def state(self): ...
    @property
    def attributes(self): ...
    @property
    def last_changed(self): ...
    @property
    def last_updated(self): ...
    @property
    def context(self): ...
    @property
    def domain(self): ...
    @property
    def object_id(self): ...
    @property
    def name(self): ...
    @property
    def state_with_unit(self) -> str: ...
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

def _collect_state(hass: HomeAssistant, entity_id: str) -> None: ...
def _template_state_no_collect(hass: HomeAssistant, state: State) -> TemplateState: ...
def _state_generator(hass: HomeAssistant, domain: Union[str, None]) -> Generator: ...
def _get_state_if_valid(hass: HomeAssistant, entity_id: str) -> Union[TemplateState, None]: ...
def _get_state(hass: HomeAssistant, entity_id: str) -> Union[TemplateState, None]: ...
def _template_state(hass: HomeAssistant, state: State) -> TemplateState: ...
def _get_template_state_from_state(hass: HomeAssistant, entity_id: str, state: Union[State, None]) -> Union[TemplateState, None]: ...
def _resolve_state(hass: HomeAssistant, entity_id_or_state: Any) -> Union[State, TemplateState, None]: ...
@overload
def forgiving_boolean(value: Any) -> Union[bool, object]: ...
@overload
def forgiving_boolean(value: Any, default: _T) -> Union[bool, _T]: ...
def result_as_boolean(template_result: Union[Any, None]) -> bool: ...
def expand(hass: HomeAssistant, *args: Any) -> Iterable[State]: ...
def device_entities(hass: HomeAssistant, _device_id: str) -> Iterable[str]: ...
def integration_entities(hass: HomeAssistant, entry_name: str) -> Iterable[str]: ...
def config_entry_id(hass: HomeAssistant, entity_id: str) -> Union[str, None]: ...
def device_id(hass: HomeAssistant, entity_id_or_device_name: str) -> Union[str, None]: ...
def device_attr(hass: HomeAssistant, device_or_entity_id: str, attr_name: str) -> Any: ...
def is_device_attr(hass: HomeAssistant, device_or_entity_id: str, attr_name: str, attr_value: Any) -> bool: ...
def area_id(hass: HomeAssistant, lookup_value: str) -> Union[str, None]: ...
def _get_area_name(area_reg: area_registry.AreaRegistry, valid_area_id: str) -> str: ...
def area_name(hass: HomeAssistant, lookup_value: str) -> Union[str, None]: ...
def area_entities(hass: HomeAssistant, area_id_or_name: str) -> Iterable[str]: ...
def area_devices(hass: HomeAssistant, area_id_or_name: str) -> Iterable[str]: ...
def closest(hass, *args): ...
def closest_filter(hass, *args): ...
def distance(hass, *args): ...
def is_state(hass: HomeAssistant, entity_id: str, state: State) -> bool: ...
def is_state_attr(hass: HomeAssistant, entity_id: str, name: str, value: Any) -> bool: ...
def state_attr(hass: HomeAssistant, entity_id: str, name: str) -> Any: ...
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
def as_timedelta(value: str) -> Union[timedelta, None]: ...
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
def _regex_cache(find: str, flags: int) -> re.Pattern: ...
def regex_replace(value: str = ..., find: str = ..., replace: str = ..., ignorecase: bool = ...): ...
def regex_search(value, find: str = ..., ignorecase: bool = ...): ...
def regex_findall_index(value, find: str = ..., index: int = ..., ignorecase: bool = ...): ...
def regex_findall(value, find: str = ..., ignorecase: bool = ...): ...
def bitwise_and(first_value, second_value): ...
def bitwise_or(first_value, second_value): ...
def struct_pack(value: Union[Any, None], format_string: str) -> Union[bytes, None]: ...
def struct_unpack(value: bytes, format_string: str, offset: int = ...) -> Union[Any, None]: ...
def base64_encode(value): ...
def base64_decode(value): ...
def ordinal(value): ...
def from_json(value): ...
def to_json(value, ensure_ascii: bool = ...): ...
def random_every_time(context, values): ...
def today_at(time_str: str = ...) -> datetime: ...
def relative_time(value): ...
def urlencode(value): ...
def slugify(value, separator: str = ...): ...
def iif(value: Any, if_true: Any = ..., if_false: Any = ..., if_none: Any = ...) -> Any: ...
def set_template(template_str: str, action: str) -> Generator: ...
def _render_with_context(template_str: str, template: jinja2.Template, **kwargs: Any) -> str: ...

class LoggingUndefined(jinja2.Undefined):
    def _log_message(self) -> None: ...
    def _fail_with_undefined_error(self, *args, **kwargs): ...
    def __str__(self): ...
    def __iter__(self): ...
    def __bool__(self) -> bool: ...

class TemplateEnvironment(ImmutableSandboxedEnvironment):
    hass: Incomplete
    template_cache: Incomplete
    def __init__(self, hass, limited: bool = ..., strict: bool = ...) -> None: ...
    def is_safe_callable(self, obj): ...
    def is_safe_attribute(self, obj, attr, value): ...
    def compile(self, source, name: Incomplete | None = ..., filename: Incomplete | None = ..., raw: bool = ..., defer_init: bool = ...): ...

_NO_HASS_ENV: Incomplete
