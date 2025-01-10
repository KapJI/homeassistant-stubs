import abc
import asyncio
import voluptuous as vol
from . import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry, floor_registry as floor_registry
from .typing import VolSchemaType as VolSchemaType
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable, Collection, Iterable
from dataclasses import dataclass, field
from enum import Enum, StrEnum
from homeassistant.components.homeassistant.exposed_entities import async_should_expose as async_should_expose
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any

_LOGGER: Incomplete
type _SlotsType = dict[str, Any]
type _IntentSlotsType = dict[str | tuple[str, str], VolSchemaType | Callable[[Any], Any]]
INTENT_TURN_OFF: str
INTENT_TURN_ON: str
INTENT_TOGGLE: str
INTENT_GET_STATE: str
INTENT_NEVERMIND: str
INTENT_SET_POSITION: str
INTENT_START_TIMER: str
INTENT_CANCEL_TIMER: str
INTENT_CANCEL_ALL_TIMERS: str
INTENT_INCREASE_TIMER: str
INTENT_DECREASE_TIMER: str
INTENT_PAUSE_TIMER: str
INTENT_UNPAUSE_TIMER: str
INTENT_TIMER_STATUS: str
INTENT_GET_CURRENT_DATE: str
INTENT_GET_CURRENT_TIME: str
INTENT_RESPOND: str
SLOT_SCHEMA: Incomplete
DATA_KEY: HassKey[dict[str, IntentHandler]]
SPEECH_TYPE_PLAIN: str
SPEECH_TYPE_SSML: str

def async_register(hass: HomeAssistant, handler: IntentHandler) -> None: ...
def async_remove(hass: HomeAssistant, intent_type: str) -> None: ...
def async_get(hass: HomeAssistant) -> Iterable[IntentHandler]: ...
async def async_handle(hass: HomeAssistant, platform: str, intent_type: str, slots: _SlotsType | None = None, text_input: str | None = None, context: Context | None = None, language: str | None = None, assistant: str | None = None, device_id: str | None = None, conversation_agent_id: str | None = None) -> IntentResponse: ...

class IntentError(HomeAssistantError): ...
class UnknownIntent(IntentError): ...
class InvalidSlotInfo(IntentError): ...

class IntentHandleError(IntentError):
    response_key: Incomplete
    def __init__(self, message: str = '', response_key: str | None = None) -> None: ...

class IntentUnexpectedError(IntentError): ...

class MatchFailedReason(Enum):
    NAME = ...
    AREA = ...
    FLOOR = ...
    DOMAIN = ...
    DEVICE_CLASS = ...
    FEATURE = ...
    STATE = ...
    ASSISTANT = ...
    INVALID_AREA = ...
    INVALID_FLOOR = ...
    DUPLICATE_NAME = ...
    def is_no_entities_reason(self) -> bool: ...

@dataclass
class MatchTargetsConstraints:
    name: str | None = ...
    area_name: str | None = ...
    floor_name: str | None = ...
    domains: Collection[str] | None = ...
    device_classes: Collection[str] | None = ...
    features: int | None = ...
    states: Collection[str] | None = ...
    assistant: str | None = ...
    allow_duplicate_names: bool = ...
    @property
    def has_constraints(self) -> bool: ...

@dataclass
class MatchTargetsPreferences:
    area_id: str | None = ...
    floor_id: str | None = ...

@dataclass
class MatchTargetsResult:
    is_match: bool
    no_match_reason: MatchFailedReason | None = ...
    states: list[State] = field(default_factory=list)
    no_match_name: str | None = ...
    areas: list[area_registry.AreaEntry] = field(default_factory=list)
    floors: list[floor_registry.FloorEntry] = field(default_factory=list)

class MatchFailedError(IntentError):
    result: Incomplete
    constraints: Incomplete
    preferences: Incomplete
    def __init__(self, result: MatchTargetsResult, constraints: MatchTargetsConstraints, preferences: MatchTargetsPreferences | None = None) -> None: ...
    def __str__(self) -> str: ...

class NoStatesMatchedError(MatchFailedError):
    def __init__(self, reason: MatchFailedReason, name: str | None = None, area: str | None = None, floor: str | None = None, domains: set[str] | None = None, device_classes: set[str] | None = None) -> None: ...

@dataclass
class MatchTargetsCandidate:
    state: State
    is_exposed: bool
    entity: entity_registry.RegistryEntry | None = ...
    area: area_registry.AreaEntry | None = ...
    floor: floor_registry.FloorEntry | None = ...
    device: device_registry.DeviceEntry | None = ...
    matched_name: str | None = ...

def find_areas(name: str, areas: area_registry.AreaRegistry) -> Iterable[area_registry.AreaEntry]: ...
def find_floors(name: str, floors: floor_registry.FloorRegistry) -> Iterable[floor_registry.FloorEntry]: ...
def _normalize_name(name: str) -> str: ...
def _filter_by_name(name: str, candidates: Iterable[MatchTargetsCandidate]) -> Iterable[MatchTargetsCandidate]: ...
def _filter_by_features(features: int, candidates: Iterable[MatchTargetsCandidate]) -> Iterable[MatchTargetsCandidate]: ...
def _filter_by_device_classes(device_classes: Iterable[str], candidates: Iterable[MatchTargetsCandidate]) -> Iterable[MatchTargetsCandidate]: ...
def _add_areas(areas: area_registry.AreaRegistry, devices: device_registry.DeviceRegistry, candidates: Iterable[MatchTargetsCandidate]) -> None: ...
def async_match_targets(hass: HomeAssistant, constraints: MatchTargetsConstraints, preferences: MatchTargetsPreferences | None = None, states: list[State] | None = None) -> MatchTargetsResult: ...
def async_match_states(hass: HomeAssistant, name: str | None = None, area_name: str | None = None, floor_name: str | None = None, domains: Collection[str] | None = None, device_classes: Collection[str] | None = None, states: list[State] | None = None, assistant: str | None = None) -> Iterable[State]: ...
def async_test_feature(state: State, feature: int, feature_name: str) -> None: ...

class IntentHandler:
    intent_type: str
    platforms: set[str] | None
    description: str | None
    @property
    def slot_schema(self) -> dict | None: ...
    def async_can_handle(self, intent_obj: Intent) -> bool: ...
    def async_validate_slots(self, slots: _SlotsType) -> _SlotsType: ...
    @cached_property
    def _slot_schema(self) -> vol.Schema: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...
    def __repr__(self) -> str: ...

def non_empty_string(value: Any) -> str: ...

class DynamicServiceIntentHandler(IntentHandler, metaclass=abc.ABCMeta):
    service_timeout: float
    intent_type: Incomplete
    speech: Incomplete
    required_domains: Incomplete
    required_features: Incomplete
    required_states: Incomplete
    description: Incomplete
    platforms: Incomplete
    device_classes: Incomplete
    required_slots: _IntentSlotsType
    optional_slots: _IntentSlotsType
    def __init__(self, intent_type: str, speech: str | None = None, required_slots: _IntentSlotsType | None = None, optional_slots: _IntentSlotsType | None = None, required_domains: set[str] | None = None, required_features: int | None = None, required_states: set[str] | None = None, description: str | None = None, platforms: set[str] | None = None, device_classes: set[type[StrEnum]] | None = None) -> None: ...
    @cached_property
    def slot_schema(self) -> dict: ...
    @abstractmethod
    def get_domain_and_service(self, intent_obj: Intent, state: State) -> tuple[str, str]: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...
    async def async_handle_states(self, intent_obj: Intent, match_result: MatchTargetsResult, match_constraints: MatchTargetsConstraints, match_preferences: MatchTargetsPreferences | None = None) -> IntentResponse: ...
    async def async_call_service(self, domain: str, service: str, intent_obj: Intent, state: State) -> None: ...
    async def _run_then_background(self, task: asyncio.Task[Any]) -> None: ...

class ServiceIntentHandler(DynamicServiceIntentHandler):
    domain: Incomplete
    service: Incomplete
    def __init__(self, intent_type: str, domain: str, service: str, speech: str | None = None, required_slots: _IntentSlotsType | None = None, optional_slots: _IntentSlotsType | None = None, required_domains: set[str] | None = None, required_features: int | None = None, required_states: set[str] | None = None, description: str | None = None, platforms: set[str] | None = None, device_classes: set[type[StrEnum]] | None = None) -> None: ...
    def get_domain_and_service(self, intent_obj: Intent, state: State) -> tuple[str, str]: ...

class IntentCategory(Enum):
    ACTION = 'action'
    QUERY = 'query'

class Intent:
    __slots__: Incomplete
    hass: Incomplete
    platform: Incomplete
    intent_type: Incomplete
    slots: Incomplete
    text_input: Incomplete
    context: Incomplete
    language: Incomplete
    category: Incomplete
    assistant: Incomplete
    device_id: Incomplete
    conversation_agent_id: Incomplete
    def __init__(self, hass: HomeAssistant, platform: str, intent_type: str, slots: _SlotsType, text_input: str | None, context: Context, language: str, category: IntentCategory | None = None, assistant: str | None = None, device_id: str | None = None, conversation_agent_id: str | None = None) -> None: ...
    def create_response(self) -> IntentResponse: ...

class IntentResponseType(Enum):
    ACTION_DONE = 'action_done'
    PARTIAL_ACTION_DONE = 'partial_action_done'
    QUERY_ANSWER = 'query_answer'
    ERROR = 'error'

class IntentResponseErrorCode(str, Enum):
    NO_INTENT_MATCH = 'no_intent_match'
    NO_VALID_TARGETS = 'no_valid_targets'
    FAILED_TO_HANDLE = 'failed_to_handle'
    UNKNOWN = 'unknown'

class IntentResponseTargetType(str, Enum):
    AREA = 'area'
    FLOOR = 'floor'
    DEVICE = 'device'
    ENTITY = 'entity'
    DOMAIN = 'domain'
    DEVICE_CLASS = 'device_class'
    CUSTOM = 'custom'

@dataclass(slots=True)
class IntentResponseTarget:
    name: str
    type: IntentResponseTargetType
    id: str | None = ...

class IntentResponse:
    language: Incomplete
    intent: Incomplete
    speech: dict[str, dict[str, Any]]
    reprompt: dict[str, dict[str, Any]]
    card: dict[str, dict[str, str]]
    error_code: IntentResponseErrorCode | None
    intent_targets: list[IntentResponseTarget]
    success_results: list[IntentResponseTarget]
    failed_results: list[IntentResponseTarget]
    matched_states: list[State]
    unmatched_states: list[State]
    speech_slots: dict[str, Any]
    response_type: Incomplete
    def __init__(self, language: str, intent: Intent | None = None) -> None: ...
    def async_set_speech(self, speech: str, speech_type: str = 'plain', extra_data: Any | None = None) -> None: ...
    def async_set_reprompt(self, speech: str, speech_type: str = 'plain', extra_data: Any | None = None) -> None: ...
    def async_set_card(self, title: str, content: str, card_type: str = 'simple') -> None: ...
    def async_set_error(self, code: IntentResponseErrorCode, message: str) -> None: ...
    def async_set_targets(self, intent_targets: list[IntentResponseTarget]) -> None: ...
    def async_set_results(self, success_results: list[IntentResponseTarget], failed_results: list[IntentResponseTarget] | None = None) -> None: ...
    def async_set_states(self, matched_states: list[State], unmatched_states: list[State] | None = None) -> None: ...
    def async_set_speech_slots(self, speech_slots: dict[str, Any]) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
