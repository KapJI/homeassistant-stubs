import voluptuous as vol
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from enum import Enum
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, TypeVar

_LOGGER: Incomplete
_SlotsType = dict[str, Any]
_T = TypeVar('_T')
INTENT_TURN_OFF: str
INTENT_TURN_ON: str
INTENT_TOGGLE: str
SLOT_SCHEMA: Incomplete
DATA_KEY: str
SPEECH_TYPE_PLAIN: str
SPEECH_TYPE_SSML: str

def async_register(hass: HomeAssistant, handler: IntentHandler) -> None: ...
async def async_handle(hass: HomeAssistant, platform: str, intent_type: str, slots: Union[_SlotsType, None] = ..., text_input: Union[str, None] = ..., context: Union[Context, None] = ..., language: Union[str, None] = ...) -> IntentResponse: ...

class IntentError(HomeAssistantError): ...
class UnknownIntent(IntentError): ...
class InvalidSlotInfo(IntentError): ...
class IntentHandleError(IntentError): ...
class IntentUnexpectedError(IntentError): ...

def async_match_state(hass: HomeAssistant, name: str, states: Union[Iterable[State], None] = ...) -> State: ...
def async_test_feature(state: State, feature: int, feature_name: str) -> None: ...

class IntentHandler:
    intent_type: Union[str, None]
    slot_schema: Union[vol.Schema, None]
    _slot_schema: Union[vol.Schema, None]
    platforms: Union[Iterable[str], None]
    def async_can_handle(self, intent_obj: Intent) -> bool: ...
    def async_validate_slots(self, slots: _SlotsType) -> _SlotsType: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...
    def __repr__(self) -> str: ...

def _fuzzymatch(name: str, items: Iterable[_T], key: Callable[[_T], str]) -> Union[_T, None]: ...

class ServiceIntentHandler(IntentHandler):
    slot_schema: Incomplete
    intent_type: Incomplete
    domain: Incomplete
    service: Incomplete
    speech: Incomplete
    def __init__(self, intent_type: str, domain: str, service: str, speech: str) -> None: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...

class IntentCategory(Enum):
    ACTION: str
    QUERY: str

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
    def __init__(self, hass: HomeAssistant, platform: str, intent_type: str, slots: _SlotsType, text_input: Union[str, None], context: Context, language: str, category: Union[IntentCategory, None] = ...) -> None: ...
    def create_response(self) -> IntentResponse: ...

class IntentResponseType(Enum):
    ACTION_DONE: str
    PARTIAL_ACTION_DONE: str
    QUERY_ANSWER: str
    ERROR: str

class IntentResponseErrorCode(str, Enum):
    NO_INTENT_MATCH: str
    NO_VALID_TARGETS: str
    FAILED_TO_HANDLE: str
    UNKNOWN: str

class IntentResponseTargetType(str, Enum):
    AREA: str
    DEVICE: str
    ENTITY: str
    DOMAIN: str
    DEVICE_CLASS: str
    CUSTOM: str

class IntentResponseTarget:
    name: str
    type: IntentResponseTargetType
    id: Union[str, None]
    def __init__(self, name, type, id) -> None: ...

class IntentResponse:
    language: Incomplete
    intent: Incomplete
    speech: Incomplete
    reprompt: Incomplete
    card: Incomplete
    error_code: Incomplete
    intent_targets: Incomplete
    success_results: Incomplete
    failed_results: Incomplete
    response_type: Incomplete
    def __init__(self, language: str, intent: Union[Intent, None] = ...) -> None: ...
    def async_set_speech(self, speech: str, speech_type: str = ..., extra_data: Union[Any, None] = ...) -> None: ...
    def async_set_reprompt(self, speech: str, speech_type: str = ..., extra_data: Union[Any, None] = ...) -> None: ...
    def async_set_card(self, title: str, content: str, card_type: str = ...) -> None: ...
    def async_set_error(self, code: IntentResponseErrorCode, message: str) -> None: ...
    def async_set_targets(self, intent_targets: list[IntentResponseTarget]) -> None: ...
    def async_set_results(self, success_results: list[IntentResponseTarget], failed_results: Union[list[IntentResponseTarget], None] = ...) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
