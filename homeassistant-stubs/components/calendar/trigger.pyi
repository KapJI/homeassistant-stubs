import asyncio
import datetime
from . import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_OFFSET as CONF_OFFSET, CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.automation import move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.target import TargetEntityChangeTracker as TargetEntityChangeTracker, TargetSelection as TargetSelection
from homeassistant.helpers.trigger import Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
EVENT_START: str
EVENT_END: str
UPDATE_INTERVAL: Incomplete
CONF_OFFSET_TYPE: str
OFFSET_TYPE_BEFORE: str
OFFSET_TYPE_AFTER: str
_SINGLE_ENTITY_EVENT_OPTIONS_SCHEMA: Incomplete
_SINGLE_ENTITY_EVENT_TRIGGER_SCHEMA: Incomplete
_EVENT_TRIGGER_SCHEMA: Incomplete

@dataclass
class QueuedCalendarEvent:
    trigger_time: datetime.datetime
    event: CalendarEvent
    entity_id: str

@dataclass
class Timespan:
    start: datetime.datetime
    end: datetime.datetime
    def with_offset(self, offset: datetime.timedelta) -> Timespan: ...
    def __contains__(self, trigger: datetime.datetime) -> bool: ...
    def next_upcoming(self, now: datetime.datetime, interval: datetime.timedelta) -> Timespan: ...
    def __str__(self) -> str: ...
type EventFetcher = Callable[[Timespan], Awaitable[list[tuple[str, CalendarEvent]]]]
type QueuedEventFetcher = Callable[[Timespan], Awaitable[list[QueuedCalendarEvent]]]

def get_entity(hass: HomeAssistant, entity_id: str) -> CalendarEntity: ...
def event_fetcher(hass: HomeAssistant, entity_ids: set[str]) -> EventFetcher: ...
def queued_event_fetcher(fetcher: EventFetcher, event_type: str, offset: datetime.timedelta) -> QueuedEventFetcher: ...

class CalendarEventListener:
    _hass: Incomplete
    _action_runner: Incomplete
    _trigger_payload: Incomplete
    _unsub_event: CALLBACK_TYPE | None
    _unsub_refresh: CALLBACK_TYPE | None
    _fetcher: Incomplete
    _timespan: Incomplete
    _events: list[QueuedCalendarEvent]
    def __init__(self, hass: HomeAssistant, action_runner: TriggerActionRunner, trigger_payload: dict[str, Any], fetcher: QueuedEventFetcher) -> None: ...
    async def async_attach(self) -> None: ...
    @callback
    def async_detach(self) -> None: ...
    @callback
    def _listen_next_calendar_event(self) -> None: ...
    def _clear_event_listener(self) -> None: ...
    async def _handle_calendar_event(self, now: datetime.datetime) -> None: ...
    def _dispatch_events(self, now: datetime.datetime) -> None: ...
    async def _handle_refresh(self, now_utc: datetime.datetime) -> None: ...

class TargetCalendarEventListener(TargetEntityChangeTracker):
    _event_type: Incomplete
    _offset: Incomplete
    _run_action: Incomplete
    _trigger_data: Incomplete
    _pending_listener_task: asyncio.Task[None] | None
    _calendar_event_listener: CalendarEventListener | None
    def __init__(self, hass: HomeAssistant, target_selection: TargetSelection, event_type: str, offset: datetime.timedelta, run_action: TriggerActionRunner) -> None: ...
    @callback
    def _handle_entities_update(self, tracked_entities: set[str]) -> None: ...
    async def _start_listening(self, tracked_entities: set[str]) -> None: ...
    def _unsubscribe(self) -> None: ...

class SingleEntityEventTrigger(Trigger):
    _options: dict[str, Any]
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...

class EventTrigger(Trigger):
    _options: dict[str, Any]
    _event_type: str
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _target: Incomplete
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...

class EventStartedTrigger(EventTrigger):
    _event_type = EVENT_START

class EventEndedTrigger(EventTrigger):
    _event_type = EVENT_END

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
