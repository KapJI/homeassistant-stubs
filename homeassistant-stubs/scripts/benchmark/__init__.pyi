from homeassistant import core as core
from homeassistant.components.websocket_api.const import JSON_DUMP as JSON_DUMP
from homeassistant.const import ATTR_NOW as ATTR_NOW, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_TIME_CHANGED as EVENT_TIME_CHANGED
from homeassistant.helpers.entityfilter import convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Any, Callable, TypeVar

CALLABLE_T = TypeVar('CALLABLE_T', bound=Callable)
BENCHMARKS: dict[str, Callable]

def run(args: Any) -> None: ...
async def run_benchmark(bench: Any) -> None: ...
def benchmark(func: CALLABLE_T) -> CALLABLE_T: ...
async def fire_events(hass: Any): ...
async def fire_events_with_filter(hass: Any): ...
async def time_changed_helper(hass: Any): ...
async def state_changed_helper(hass: Any): ...
async def state_changed_event_helper(hass: Any): ...
async def state_changed_event_filter_helper(hass: Any): ...
async def logbook_filtering_state(hass: Any): ...
async def logbook_filtering_attributes(hass: Any): ...
async def filtering_entity_id(hass: Any): ...
async def valid_entity_id(hass: Any): ...
async def json_serialize_states(hass: Any): ...