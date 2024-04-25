from . import const as const
from _typeshed import Incomplete
from homeassistant.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_CONTEXT as COMPRESSED_STATE_CONTEXT, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, State as State
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data, json_bytes as json_bytes
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from typing import Any, Final

_LOGGER: Final[Incomplete]
MINIMAL_MESSAGE_SCHEMA: Final[Incomplete]
BASE_COMMAND_MESSAGE_SCHEMA: Final[Incomplete]
STATE_DIFF_ADDITIONS: str
STATE_DIFF_REMOVALS: str
ENTITY_EVENT_ADD: str
ENTITY_EVENT_REMOVE: str
ENTITY_EVENT_CHANGE: str
BASE_ERROR_MESSAGE: Incomplete
INVALID_JSON_PARTIAL_MESSAGE: Incomplete

def result_message(iden: int, result: Any = None) -> dict[str, Any]: ...
def construct_result_message(iden: int, payload: bytes) -> bytes: ...
def error_message(iden: int | None, code: str, message: str, translation_key: str | None = None, translation_domain: str | None = None, translation_placeholders: dict[str, Any] | None = None) -> dict[str, Any]: ...
def event_message(iden: int, event: Any) -> dict[str, Any]: ...
def cached_event_message(iden: int, event: Event) -> bytes: ...
def _partial_cached_event_message(event: Event) -> bytes: ...
def cached_state_diff_message(iden: int, event: Event[EventStateChangedData]) -> bytes: ...
def _partial_cached_state_diff_message(event: Event[EventStateChangedData]) -> bytes: ...
def _state_diff_event(event: Event[EventStateChangedData]) -> dict: ...
def _state_diff(old_state: State, new_state: State) -> dict[str, dict[str, dict[str, dict[str, str | list[str]]]]]: ...
def _message_to_json_bytes_or_none(message: dict[str, Any]) -> bytes | None: ...
def message_to_json_bytes(message: dict[str, Any]) -> bytes: ...
