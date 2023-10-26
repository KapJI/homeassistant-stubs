from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import ATTR_OBSTRUCTION_DETECTED as ATTR_OBSTRUCTION_DETECTED, CHAR_CURRENT_DOOR_STATE as CHAR_CURRENT_DOOR_STATE, CHAR_CURRENT_POSITION as CHAR_CURRENT_POSITION, CHAR_CURRENT_TILT_ANGLE as CHAR_CURRENT_TILT_ANGLE, CHAR_HOLD_POSITION as CHAR_HOLD_POSITION, CHAR_OBSTRUCTION_DETECTED as CHAR_OBSTRUCTION_DETECTED, CHAR_POSITION_STATE as CHAR_POSITION_STATE, CHAR_TARGET_DOOR_STATE as CHAR_TARGET_DOOR_STATE, CHAR_TARGET_POSITION as CHAR_TARGET_POSITION, CHAR_TARGET_TILT_ANGLE as CHAR_TARGET_TILT_ANGLE, CONF_LINKED_OBSTRUCTION_SENSOR as CONF_LINKED_OBSTRUCTION_SENSOR, HK_DOOR_CLOSED as HK_DOOR_CLOSED, HK_DOOR_CLOSING as HK_DOOR_CLOSING, HK_DOOR_OPEN as HK_DOOR_OPEN, HK_DOOR_OPENING as HK_DOOR_OPENING, HK_POSITION_GOING_TO_MAX as HK_POSITION_GOING_TO_MAX, HK_POSITION_GOING_TO_MIN as HK_POSITION_GOING_TO_MIN, HK_POSITION_STOPPED as HK_POSITION_STOPPED, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_DOOR as SERV_DOOR, SERV_GARAGE_DOOR_OPENER as SERV_GARAGE_DOOR_OPENER, SERV_WINDOW as SERV_WINDOW, SERV_WINDOW_COVERING as SERV_WINDOW_COVERING
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_CURRENT_TILT_POSITION as ATTR_CURRENT_TILT_POSITION, ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntityFeature as CoverEntityFeature, DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import State as State, callback as callback
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import EventType as EventType
from pyhap.service import Service as Service
from typing import Any

DOOR_CURRENT_HASS_TO_HK: Incomplete
DOOR_TARGET_HASS_TO_HK: Incomplete
MOVING_STATES: Incomplete
_LOGGER: Incomplete

class GarageDoorOpener(HomeAccessory):
    char_current_state: Incomplete
    char_target_state: Incomplete
    char_obstruction_detected: Incomplete
    linked_obstruction_sensor: Incomplete
    def __init__(self, *args: Any) -> None: ...
    async def run(self) -> None: ...
    def _async_update_obstruction_event(self, event: EventType[EventStateChangedData]) -> None: ...
    def _async_update_obstruction_state(self, new_state: State | None) -> None: ...
    def set_state(self, value: int) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class OpeningDeviceBase(HomeAccessory):
    features: Incomplete
    _supports_stop: Incomplete
    chars: Incomplete
    _supports_tilt: Incomplete
    serv_cover: Incomplete
    char_hold_position: Incomplete
    char_target_tilt: Incomplete
    char_current_tilt: Incomplete
    def __init__(self, *args: Any, category: int, service: Service) -> None: ...
    def set_stop(self, value: int) -> None: ...
    def set_tilt(self, value: float) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class OpeningDevice(OpeningDeviceBase, HomeAccessory):
    char_current_position: Incomplete
    char_target_position: Incomplete
    char_position_state: Incomplete
    def __init__(self, *args: Any, category: int, service: Service) -> None: ...
    def move_cover(self, value: int) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class Door(OpeningDevice):
    def __init__(self, *args: Any) -> None: ...

class Window(OpeningDevice):
    def __init__(self, *args: Any) -> None: ...

class WindowCovering(OpeningDevice):
    def __init__(self, *args: Any) -> None: ...

class WindowCoveringBasic(OpeningDeviceBase, HomeAccessory):
    char_current_position: Incomplete
    char_target_position: Incomplete
    char_position_state: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def move_cover(self, value: int) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

def _hass_state_to_position_start(state: str) -> int: ...
