import jinja2
from collections.abc import Generator, Iterable
from contextvars import ContextVar
from datetime import datetime
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, LENGTH_METERS as LENGTH_METERS, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.typing import TemplateVarsType as TemplateVarsType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import convert as convert
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.thread import ThreadWithException as ThreadWithException
from jinja2.sandbox import ImmutableSandboxedEnvironment
from typing import Any, Optional

_LOGGER: Any
_SENTINEL: Any
DATE_STR_FORMAT: str
_RENDER_INFO: str
_ENVIRONMENT: str
_ENVIRONMENT_LIMITED: str
_ENVIRONMENT_STRICT: str
_RE_JINJA_DELIMITERS: Any
_IS_NUMERIC: Any
_RESERVED_NAMES: Any
_GROUP_DOMAIN_PREFIX: str
_COLLECTABLE_STATE_ATTRIBUTES: Any
ALL_STATES_RATE_LIMIT: Any
DOMAIN_STATES_RATE_LIMIT: Any
template_cv: ContextVar[Union[str, None]]

def attach(hass: HomeAssistant, obj: Any) -> None: ...
def render_complex(value: Any, variables: TemplateVarsType=..., limited: bool=...) -> Any: ...
def is_complex(value: Any) -> bool: ...
def is_template_string(maybe_template: str) -> bool: ...

class ResultWrapper:
    render_result: Union[str, None]

def gen_result_wrapper(kls: Any): ...

class TupleWrapper(tuple, ResultWrapper):
    def __new__(cls: Any, value: tuple, *, render_result: Union[str, None]=...) -> TupleWrapper: ...
    render_result: Any = ...
    def __init__(self, value: tuple, *, render_result: Union[str, None]=...) -> None: ...
    def __str__(self) -> str: ...

RESULT_WRAPPERS: dict[type, type]

def _true(arg: str) -> bool: ...
def _false(arg: str) -> bool: ...

class RenderInfo:
    template: Any = ...
    filter_lifecycle: Any = ...
    filter: Any = ...
    _result: Any = ...
    is_static: bool = ...
    exception: Any = ...
    all_states: bool = ...
    all_states_lifecycle: bool = ...
    domains: Any = ...
    domains_lifecycle: Any = ...
    entities: Any = ...
    rate_limit: Any = ...
    has_time: bool = ...
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
    __slots__: Any = ...
    template: Any = ...
    _compiled_code: Any = ...
    _compiled: Any = ...
    hass: Any = ...
    is_static: Any = ...
    _exc_info: Any = ...
    _limited: Any = ...
    _strict: Any = ...
    def __init__(self, template: Any, hass: Optional[Any] = ...) -> None: ...
    @property
    def _env(self) -> TemplateEnvironment: ...
    def ensure_valid(self) -> None: ...
    def render(self, variables: TemplateVarsType=..., parse_result: bool=..., limited: bool=..., **kwargs: Any) -> Any: ...
    def async_render(self, variables: TemplateVarsType=..., parse_result: bool=..., limited: bool=..., strict: bool=..., **kwargs: Any) -> Any: ...
    def _parse_result(self, render_result: str) -> Any: ...
    async def async_render_will_timeout(self, timeout: float, variables: TemplateVarsType=..., strict: bool=..., **kwargs: Any) -> bool: ...
    def async_render_to_info(self, variables: TemplateVarsType=..., strict: bool=..., **kwargs: Any) -> RenderInfo: ...
    def render_with_possible_json_value(self, value: Any, error_value: Any = ...): ...
    def async_render_with_possible_json_value(self, value: Any, error_value: Any = ..., variables: Optional[Any] = ...): ...
    def _ensure_compiled(self, limited: bool=..., strict: bool=...) -> jinja2.Template: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

class AllStates:
    _hass: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, name: Any): ...
    __getitem__: Any = ...
    def _collect_all(self) -> None: ...
    def _collect_all_lifecycle(self) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __call__(self, entity_id: Any): ...
    def __repr__(self) -> str: ...

class DomainStates:
    _hass: Any = ...
    _domain: Any = ...
    def __init__(self, hass: HomeAssistant, domain: str) -> None: ...
    def __getattr__(self, name: Any): ...
    __getitem__: Any = ...
    def _collect_domain(self) -> None: ...
    def _collect_domain_lifecycle(self) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

class TemplateState(State):
    __slots__: Any = ...
    _hass: Any = ...
    _state: Any = ...
    _collect: Any = ...
    def __init__(self, hass: HomeAssistant, state: State, collect: bool=...) -> None: ...
    def _collect_state(self) -> None: ...
    def __getitem__(self, item: Any): ...
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
    def __repr__(self) -> str: ...

def _collect_state(hass: HomeAssistant, entity_id: str) -> None: ...
def _state_generator(hass: HomeAssistant, domain: Union[str, None]) -> Generator: ...
def _get_state_if_valid(hass: HomeAssistant, entity_id: str) -> Union[TemplateState, None]: ...
def _get_state(hass: HomeAssistant, entity_id: str) -> Union[TemplateState, None]: ...
def _get_template_state_from_state(hass: HomeAssistant, entity_id: str, state: Union[State, None]) -> Union[TemplateState, None]: ...
def _resolve_state(hass: HomeAssistant, entity_id_or_state: Any) -> Union[State, TemplateState, None]: ...
def result_as_boolean(template_result: Union[str, None]) -> bool: ...
def expand(hass: HomeAssistant, *args: Any) -> Iterable[State]: ...
def device_entities(hass: HomeAssistant, device_id: str) -> Iterable[str]: ...
def closest(hass: Any, *args: Any): ...
def closest_filter(hass: Any, *args: Any): ...
def distance(hass: Any, *args: Any): ...
def is_state(hass: HomeAssistant, entity_id: str, state: State) -> bool: ...
def is_state_attr(hass: HomeAssistant, entity_id: str, name: str, value: Any) -> bool: ...
def state_attr(hass: HomeAssistant, entity_id: str, name: str) -> Any: ...
def now(hass: HomeAssistant) -> datetime: ...
def utcnow(hass: HomeAssistant) -> datetime: ...
def forgiving_round(value: Any, precision: int = ..., method: str = ...): ...
def multiply(value: Any, amount: Any): ...
def logarithm(value: Any, base: Any = ...): ...
def sine(value: Any): ...
def cosine(value: Any): ...
def tangent(value: Any): ...
def arc_sine(value: Any): ...
def arc_cosine(value: Any): ...
def arc_tangent(value: Any): ...
def arc_tangent2(*args: Any): ...
def square_root(value: Any): ...
def timestamp_custom(value: Any, date_format: Any = ..., local: bool = ...): ...
def timestamp_local(value: Any): ...
def timestamp_utc(value: Any): ...
def forgiving_as_timestamp(value: Any): ...
def strptime(string: Any, fmt: Any): ...
def fail_when_undefined(value: Any): ...
def forgiving_float(value: Any): ...
def regex_match(value: Any, find: str = ..., ignorecase: bool = ...): ...
def regex_replace(value: str = ..., find: str = ..., replace: str = ..., ignorecase: bool = ...): ...
def regex_search(value: Any, find: str = ..., ignorecase: bool = ...): ...
def regex_findall_index(value: Any, find: str = ..., index: int = ..., ignorecase: bool = ...): ...
def bitwise_and(first_value: Any, second_value: Any): ...
def bitwise_or(first_value: Any, second_value: Any): ...
def base64_encode(value: Any): ...
def base64_decode(value: Any): ...
def ordinal(value: Any): ...
def from_json(value: Any): ...
def to_json(value: Any): ...
def random_every_time(context: Any, values: Any): ...
def relative_time(value: Any): ...
def urlencode(value: Any): ...
def _render_with_context(template_str: str, template: jinja2.Template, **kwargs: Any) -> str: ...

class LoggingUndefined(jinja2.Undefined):
    def _log_message(self) -> None: ...
    def _fail_with_undefined_error(self, *args: Any, **kwargs: Any): ...
    def __str__(self): ...
    def __iter__(self) -> Any: ...
    def __bool__(self): ...

class TemplateEnvironment(ImmutableSandboxedEnvironment):
    hass: Any = ...
    template_cache: Any = ...
    def __init__(self, hass: Any, limited: bool = ..., strict: bool = ...): ...
    def is_safe_callable(self, obj: Any): ...
    def is_safe_attribute(self, obj: Any, attr: Any, value: Any): ...
    def compile(self, source: Any, name: Optional[Any] = ..., filename: Optional[Any] = ..., raw: bool = ..., defer_init: bool = ...): ...

_NO_HASS_ENV: Any
