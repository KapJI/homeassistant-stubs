import abc
import asyncio
import voluptuous as vol
from . import selector as selector
from .automation import get_absolute_description_key as get_absolute_description_key, get_relative_description_key as get_relative_description_key, move_options_fields_to_top_level as move_options_fields_to_top_level
from .integration_platform import async_process_integration_platforms as async_process_integration_platforms
from .selector import TargetSelector as TargetSelector
from .target import TargetStateChangedData as TargetStateChangedData, async_track_target_selector_state_change_event as async_track_target_selector_state_change_event
from .template import Template as Template
from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Coroutine, Iterable
from dataclasses import dataclass, field
from enum import StrEnum
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ABOVE as CONF_ABOVE, CONF_ALIAS as CONF_ALIAS, CONF_BELOW as CONF_BELOW, CONF_ENABLED as CONF_ENABLED, CONF_ID as CONF_ID, CONF_OPTIONS as CONF_OPTIONS, CONF_PLATFORM as CONF_PLATFORM, CONF_SELECTOR as CONF_SELECTOR, CONF_TARGET as CONF_TARGET, CONF_VARIABLES as CONF_VARIABLES, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HassJob as HassJob, HassJobType as HassJobType, HomeAssistant as HomeAssistant, State as State, callback as callback, get_hassjob_callable_job_type as get_hassjob_callable_job_type, is_callback as is_callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, async_get_integrations as async_get_integrations
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from typing import Any, Final, Protocol, TypedDict, override

_LOGGER: Incomplete
_PLATFORM_ALIASES: Incomplete
DATA_PLUGGABLE_ACTIONS: HassKey[defaultdict[tuple, PluggableActionsEntry]]
TRIGGER_DESCRIPTION_CACHE: HassKey[dict[str, dict[str, Any] | None]]
TRIGGER_DISABLED_TRIGGERS: HassKey[set[str]]
TRIGGER_PLATFORM_SUBSCRIPTIONS: HassKey[list[Callable[[set[str]], Coroutine[Any, Any, None]]]]
TRIGGERS: HassKey[dict[str, str]]
_FIELD_DESCRIPTION_SCHEMA: Incomplete
_TRIGGER_DESCRIPTION_SCHEMA: Incomplete

def starts_with_dot(key: str) -> str: ...

_TRIGGERS_DESCRIPTION_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant) -> None: ...
@callback
def async_subscribe_platform_events(hass: HomeAssistant, on_event: Callable[[set[str]], Coroutine[Any, Any, None]]) -> Callable[[], None]: ...
async def _register_trigger_platform(hass: HomeAssistant, integration_domain: str, platform: TriggerProtocol) -> None: ...

_TRIGGER_SCHEMA: Incomplete

class Trigger(abc.ABC, metaclass=abc.ABCMeta):
    _hass: HomeAssistant
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    @abc.abstractmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_action(self, action: TriggerAction, action_payload_builder: TriggerActionPayloadBuilder) -> CALLBACK_TYPE: ...
    @abc.abstractmethod
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...

ATTR_BEHAVIOR: Final[str]
BEHAVIOR_FIRST: Final[str]
BEHAVIOR_LAST: Final[str]
BEHAVIOR_ANY: Final[str]
ENTITY_STATE_TRIGGER_SCHEMA: Incomplete
ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST: Incomplete

class EntityTriggerBase(Trigger, metaclass=abc.ABCMeta):
    _domain: str
    _schema: vol.Schema
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _options: Incomplete
    _target: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    @abc.abstractmethod
    def is_valid_state(self, state: State) -> bool: ...
    def check_all_match(self, entity_ids: set[str]) -> bool: ...
    def check_one_match(self, entity_ids: set[str]) -> bool: ...
    def entity_filter(self, entities: set[str]) -> set[str]: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...

class EntityTargetStateTriggerBase(EntityTriggerBase):
    _to_states: set[str]
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

class EntityTransitionTriggerBase(EntityTriggerBase):
    _from_states: set[str]
    _to_states: set[str]
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

class EntityOriginStateTriggerBase(EntityTriggerBase):
    _from_state: str
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

class EntityTargetStateAttributeTriggerBase(EntityTriggerBase):
    _attribute: str
    _attribute_to_state: str
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

def _validate_range[_T: dict[str, Any]](lower_limit: str, upper_limit: str) -> Callable[[_T], _T]: ...

_NUMBER_OR_ENTITY_CHOOSE_SCHEMA: Incomplete

def _validate_number_or_entity(value: dict | float | str) -> float | str: ...

_number_or_entity: Incomplete
NUMERICAL_ATTRIBUTE_CHANGED_TRIGGER_SCHEMA: Incomplete

def _get_numerical_value(hass: HomeAssistant, entity_or_float: float | str) -> float | None: ...

class EntityNumericalStateAttributeChangedTriggerBase(EntityTriggerBase):
    _attribute: str
    _schema = NUMERICAL_ATTRIBUTE_CHANGED_TRIGGER_SCHEMA
    _above: None | float | str
    _below: None | float | str
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

CONF_LOWER_LIMIT: str
CONF_UPPER_LIMIT: str
CONF_THRESHOLD_TYPE: str

class ThresholdType(StrEnum):
    ABOVE = 'above'
    BELOW = 'below'
    BETWEEN = 'between'
    OUTSIDE = 'outside'

def _validate_limits_for_threshold_type(value: dict[str, Any]) -> dict[str, Any]: ...

NUMERICAL_ATTRIBUTE_CROSSED_THRESHOLD_SCHEMA: Incomplete

class EntityNumericalStateAttributeCrossedThresholdTriggerBase(EntityTriggerBase):
    _attribute: str
    _schema = NUMERICAL_ATTRIBUTE_CROSSED_THRESHOLD_SCHEMA
    _lower_limit: float | str | None
    _upper_limit: float | str | None
    _threshold_type: ThresholdType
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...
    def is_valid_state(self, state: State) -> bool: ...

def make_entity_target_state_trigger(domain: str, to_states: str | set[str]) -> type[EntityTargetStateTriggerBase]: ...
def make_entity_transition_trigger(domain: str, *, from_states: set[str], to_states: set[str]) -> type[EntityTransitionTriggerBase]: ...
def make_entity_origin_state_trigger(domain: str, *, from_state: str) -> type[EntityOriginStateTriggerBase]: ...
def make_entity_numerical_state_attribute_changed_trigger(domain: str, attribute: str) -> type[EntityNumericalStateAttributeChangedTriggerBase]: ...
def make_entity_numerical_state_attribute_crossed_threshold_trigger(domain: str, attribute: str) -> type[EntityNumericalStateAttributeCrossedThresholdTriggerBase]: ...
def make_entity_target_state_attribute_trigger(domain: str, attribute: str, to_state: str) -> type[EntityTargetStateAttributeTriggerBase]: ...

class TriggerProtocol(Protocol):
    async def async_get_triggers(self, hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
    TRIGGER_SCHEMA: vol.Schema
    async def async_validate_trigger_config(self, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    async def async_attach_trigger(self, hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...

@dataclass(slots=True, frozen=True)
class TriggerConfig:
    key: str
    target: dict[str, Any] | None = ...
    options: dict[str, Any] | None = ...

class TriggerActionRunner(Protocol):
    @callback
    def __call__(self, extra_trigger_payload: dict[str, Any], description: str, context: Context | None = None) -> asyncio.Task[Any]: ...

class TriggerActionPayloadBuilder(Protocol):
    def __call__(self, extra_trigger_payload: dict[str, Any], description: str) -> dict[str, Any]: ...

class TriggerAction(Protocol):
    async def __call__(self, run_variables: dict[str, Any], context: Context | None = None) -> Any: ...

class TriggerActionType(Protocol):
    def __call__(self, run_variables: dict[str, Any], context: Context | None = None) -> Coroutine[Any, Any, Any] | Any: ...

class TriggerData(TypedDict):
    id: str
    idx: str
    alias: str | None

class TriggerInfo(TypedDict):
    domain: str
    name: str
    home_assistant_start: bool
    variables: TemplateVarsType
    trigger_data: TriggerData

@dataclass(slots=True)
class PluggableActionsEntry:
    plugs: set[PluggableAction] = field(default_factory=set)
    actions: dict[object, tuple[HassJob[[dict[str, Any], Context | None], Coroutine[Any, Any, None] | Any], dict[str, Any]]] = field(default_factory=dict)

class PluggableAction:
    _entry: PluggableActionsEntry | None
    _update: Incomplete
    def __init__(self, update: CALLBACK_TYPE | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    @callback
    def async_run_update(self) -> None: ...
    @staticmethod
    @callback
    def async_get_registry(hass: HomeAssistant) -> dict[tuple, PluggableActionsEntry]: ...
    @staticmethod
    @callback
    def async_attach_trigger(hass: HomeAssistant, trigger: dict[str, str], action: TriggerActionType, variables: dict[str, Any]) -> CALLBACK_TYPE: ...
    @callback
    def async_register(self, hass: HomeAssistant, trigger: dict[str, str]) -> CALLBACK_TYPE: ...
    async def async_run(self, hass: HomeAssistant, context: Context | None = None) -> None: ...

async def _async_get_trigger_platform(hass: HomeAssistant, trigger_key: str) -> tuple[str, TriggerProtocol]: ...
async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
def _trigger_action_wrapper(hass: HomeAssistant, action: Callable, conf: ConfigType) -> Callable: ...
async def _async_attach_trigger_cls(hass: HomeAssistant, trigger_cls: type[Trigger], trigger_key: str, conf: ConfigType, action: Callable, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool = False, variables: TemplateVarsType = None) -> CALLBACK_TYPE | None: ...
def _load_triggers_file(integration: Integration) -> dict[str, Any]: ...
def _load_triggers_files(integrations: Iterable[Integration]) -> dict[str, dict[str, Any]]: ...
async def async_get_all_descriptions(hass: HomeAssistant) -> dict[str, dict[str, Any] | None]: ...
