import asyncio
from .const import TIMER_DATA as TIMER_DATA
from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ID as ATTR_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import intent as intent
from homeassistant.util import ulid as ulid
from propcache import cached_property
from typing import Any

_LOGGER: Incomplete
TIMER_NOT_FOUND_RESPONSE: str
MULTIPLE_TIMERS_MATCHED_RESPONSE: str
NO_TIMER_SUPPORT_RESPONSE: str

@dataclass
class TimerInfo:
    id: str
    name: str | None
    seconds: int
    device_id: str | None
    start_hours: int | None
    start_minutes: int | None
    start_seconds: int | None
    created_at: int
    updated_at: int
    language: str
    is_active: bool = ...
    area_id: str | None = ...
    area_name: str | None = ...
    floor_id: str | None = ...
    conversation_command: str | None = ...
    conversation_agent_id: str | None = ...
    _created_seconds: int = ...
    def __post_init__(self) -> None: ...
    @property
    def seconds_left(self) -> int: ...
    @property
    def created_seconds(self) -> int: ...
    @cached_property
    def name_normalized(self) -> str: ...
    def cancel(self) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def add_time(self, seconds: int) -> None: ...
    def finish(self) -> None: ...

class TimerEventType(StrEnum):
    STARTED = 'started'
    UPDATED = 'updated'
    CANCELLED = 'cancelled'
    FINISHED = 'finished'
type TimerHandler = Callable[[TimerEventType, TimerInfo], None]

class TimerNotFoundError(intent.IntentHandleError):
    def __init__(self) -> None: ...

class MultipleTimersMatchedError(intent.IntentHandleError):
    def __init__(self) -> None: ...

class TimersNotSupportedError(intent.IntentHandleError):
    def __init__(self, device_id: str | None = None) -> None: ...

class TimerManager:
    hass: Incomplete
    timers: dict[str, TimerInfo]
    timer_tasks: dict[str, asyncio.Task]
    handlers: dict[str, TimerHandler]
    def __init__(self, hass: HomeAssistant) -> None: ...
    def register_handler(self, device_id: str, handler: TimerHandler) -> Callable[[], None]: ...
    def start_timer(self, device_id: str | None, hours: int | None, minutes: int | None, seconds: int | None, language: str, name: str | None = None, conversation_command: str | None = None, conversation_agent_id: str | None = None) -> str: ...
    async def _wait_for_timer(self, timer_id: str, seconds: int, updated_at: int) -> None: ...
    def cancel_timer(self, timer_id: str) -> None: ...
    def add_time(self, timer_id: str, seconds: int) -> None: ...
    def remove_time(self, timer_id: str, seconds: int) -> None: ...
    def pause_timer(self, timer_id: str) -> None: ...
    def unpause_timer(self, timer_id: str) -> None: ...
    def _timer_finished(self, timer_id: str) -> None: ...
    def is_timer_device(self, device_id: str) -> bool: ...

@callback
def async_device_supports_timers(hass: HomeAssistant, device_id: str) -> bool: ...
@callback
def async_register_timer_handler(hass: HomeAssistant, device_id: str, handler: TimerHandler) -> Callable[[], None]: ...

class FindTimerFilter(StrEnum):
    ONLY_ACTIVE = 'only_active'
    ONLY_INACTIVE = 'only_inactive'

def _find_timer(hass: HomeAssistant, device_id: str | None, slots: dict[str, Any], find_filter: FindTimerFilter | None = None) -> TimerInfo: ...
def _find_timers(hass: HomeAssistant, device_id: str | None, slots: dict[str, Any]) -> list[TimerInfo]: ...
def _normalize_name(name: str) -> str: ...
def _get_total_seconds(slots: dict[str, Any]) -> int: ...
def _round_time(hours: int, minutes: int, seconds: int) -> tuple[int, int, int]: ...

class StartTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class CancelTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class CancelAllTimersIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class IncreaseTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class DecreaseTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class PauseTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class UnpauseTimerIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class TimerStatusIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    description: str
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
