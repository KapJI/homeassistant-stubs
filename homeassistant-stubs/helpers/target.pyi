import dataclasses
from . import group as group
from .deprecation import deprecated_class as deprecated_class
from .event import async_track_state_change_event as async_track_state_change_event
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FLOOR_ID as ATTR_FLOOR_ID, ATTR_LABEL_ID as ATTR_LABEL_ID, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from logging import Logger
from typing import Any, TypeGuard

_LOGGER: Incomplete

@dataclasses.dataclass(slots=True, frozen=True)
class TargetStateChangedData:
    state_change_event: Event[EventStateChangedData]
    targeted_entity_ids: set[str]

def _has_match(ids: str | list[str] | None) -> TypeGuard[str | list[str]]: ...

class TargetSelection:
    __slots__: Incomplete
    entity_ids: Incomplete
    device_ids: Incomplete
    area_ids: Incomplete
    floor_ids: Incomplete
    label_ids: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    @property
    def has_any_target(self) -> bool: ...

class TargetSelectorData(TargetSelection):
    @property
    def has_any_selector(self) -> bool: ...

@dataclasses.dataclass(slots=True)
class SelectedEntities:
    referenced: set[str] = dataclasses.field(default_factory=set)
    indirectly_referenced: set[str] = dataclasses.field(default_factory=set)
    missing_devices: set[str] = dataclasses.field(default_factory=set)
    missing_areas: set[str] = dataclasses.field(default_factory=set)
    missing_floors: set[str] = dataclasses.field(default_factory=set)
    missing_labels: set[str] = dataclasses.field(default_factory=set)
    referenced_devices: set[str] = dataclasses.field(default_factory=set)
    referenced_areas: set[str] = dataclasses.field(default_factory=set)
    def log_missing(self, missing_entities: set[str], logger: Logger) -> None: ...

def async_extract_referenced_entity_ids(hass: HomeAssistant, target_selection: TargetSelection, expand_group: bool = True) -> SelectedEntities: ...

class TargetStateChangeTracker:
    _hass: Incomplete
    _target_selection: Incomplete
    _action: Incomplete
    _entity_filter: Incomplete
    _state_change_unsub: CALLBACK_TYPE | None
    _registry_unsubs: list[CALLBACK_TYPE]
    def __init__(self, hass: HomeAssistant, target_selection: TargetSelection, action: Callable[[TargetStateChangedData], Any], entity_filter: Callable[[set[str]], set[str]]) -> None: ...
    def async_setup(self) -> Callable[[], None]: ...
    def _track_entities_state_change(self) -> None: ...
    def _setup_registry_listeners(self) -> None: ...
    def _unsubscribe(self) -> None: ...

def async_track_target_selector_state_change_event(hass: HomeAssistant, target_selector_config: ConfigType, action: Callable[[TargetStateChangedData], Any], entity_filter: Callable[[set[str]], set[str]] = ...) -> CALLBACK_TYPE: ...
