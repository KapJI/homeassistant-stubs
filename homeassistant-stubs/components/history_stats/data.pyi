import datetime
from .helpers import async_calculate_period as async_calculate_period, floored_timestamp as floored_timestamp
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import EventType as EventType

MIN_TIME_UTC: Incomplete

@dataclass
class HistoryStatsState:
    seconds_matched: float | None
    match_count: int | None
    period: tuple[datetime.datetime, datetime.datetime]
    def __init__(self, seconds_matched, match_count, period) -> None: ...

@dataclass
class HistoryState:
    state: str
    last_changed: float
    def __init__(self, state, last_changed) -> None: ...

class HistoryStats:
    hass: Incomplete
    entity_id: Incomplete
    _period: Incomplete
    _state: Incomplete
    _history_current_period: Incomplete
    _previous_run_before_start: bool
    _entity_states: Incomplete
    _duration: Incomplete
    _start: Incomplete
    _end: Incomplete
    def __init__(self, hass: HomeAssistant, entity_id: str, entity_states: list[str], start: Template | None, end: Template | None, duration: datetime.timedelta | None) -> None: ...
    async def async_update(self, event: EventType[EventStateChangedData] | None) -> HistoryStatsState: ...
    async def _async_history_from_db(self, current_period_start_timestamp: float, current_period_end_timestamp: float) -> None: ...
    def _state_changes_during_period(self, start_ts: float, end_ts: float) -> list[State]: ...
    def _async_compute_seconds_and_changes(self, now_timestamp: float, start_timestamp: float, end_timestamp: float) -> tuple[float, int]: ...
