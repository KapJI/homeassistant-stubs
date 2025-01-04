from .accessories import HomeAccessory as HomeAccessory
from .const import CHAR_MUTE as CHAR_MUTE, CHAR_PROGRAMMABLE_SWITCH_EVENT as CHAR_PROGRAMMABLE_SWITCH_EVENT, CONF_LINKED_DOORBELL_SENSOR as CONF_LINKED_DOORBELL_SENSOR, SERV_DOORBELL as SERV_DOORBELL, SERV_SPEAKER as SERV_SPEAKER, SERV_STATELESS_PROGRAMMABLE_SWITCH as SERV_STATELESS_PROGRAMMABLE_SWITCH
from .util import state_changed_event_is_same_state as state_changed_event_is_same_state
from _typeshed import Incomplete
from homeassistant.const import STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HassJobType as HassJobType, State as State
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from typing import Any

_LOGGER: Incomplete
DOORBELL_SINGLE_PRESS: int
DOORBELL_DOUBLE_PRESS: int
DOORBELL_LONG_PRESS: int

class HomeDoorbellAccessory(HomeAccessory):
    _char_doorbell_detected: Incomplete
    _char_doorbell_detected_switch: Incomplete
    linked_doorbell_sensor: Incomplete
    doorbell_is_event: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def async_update_doorbell_state_event(self, event: Event[EventStateChangedData]) -> None: ...
    def async_update_doorbell_state(self, old_state: State | None, new_state: State) -> None: ...
