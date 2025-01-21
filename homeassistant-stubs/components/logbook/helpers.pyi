from .const import ALWAYS_CONTINUOUS_DOMAINS as ALWAYS_CONTINUOUS_DOMAINS, AUTOMATION_EVENTS as AUTOMATION_EVENTS, BUILT_IN_EVENTS as BUILT_IN_EVENTS, DOMAIN as DOMAIN
from .models import LogbookConfig as LogbookConfig
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, EVENT_LOGBOOK_ENTRY as EVENT_LOGBOOK_ENTRY, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback, is_callback as is_callback, split_entity_id as split_entity_id
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.util.event_type import EventType as EventType
from typing import Any

def async_filter_entities(hass: HomeAssistant, entity_ids: list[str]) -> list[str]: ...
@callback
def _async_config_entries_for_ids(hass: HomeAssistant, entity_ids: list[str] | None, device_ids: list[str] | None) -> set[str]: ...
def async_determine_event_types(hass: HomeAssistant, entity_ids: list[str] | None, device_ids: list[str] | None) -> tuple[EventType[Any] | str, ...]: ...
@callback
def extract_attr(source: Mapping[str, Any], attr: str) -> list[str]: ...
@callback
def event_forwarder_filtered(target: Callable[[Event], None], entities_filter: Callable[[str], bool] | None, entity_ids: list[str] | None, device_ids: list[str] | None) -> Callable[[Event], None]: ...
@callback
def async_subscribe_events(hass: HomeAssistant, subscriptions: list[CALLBACK_TYPE], target: Callable[[Event[Any]], None], event_types: tuple[EventType[Any] | str, ...], entities_filter: Callable[[str], bool] | None, entity_ids: list[str] | None, device_ids: list[str] | None) -> None: ...
def is_sensor_continuous(hass: HomeAssistant, ent_reg: er.EntityRegistry, entity_id: str) -> bool: ...
def _is_state_filtered(new_state: State, old_state: State) -> bool: ...
