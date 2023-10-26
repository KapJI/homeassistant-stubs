from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_IN_USE as CHAR_IN_USE, CHAR_NAME as CHAR_NAME, CHAR_ON as CHAR_ON, CHAR_OUTLET_IN_USE as CHAR_OUTLET_IN_USE, CHAR_VALVE_TYPE as CHAR_VALVE_TYPE, SERV_OUTLET as SERV_OUTLET, SERV_SWITCH as SERV_SWITCH, SERV_VALVE as SERV_VALVE, TYPE_FAUCET as TYPE_FAUCET, TYPE_SHOWER as TYPE_SHOWER, TYPE_SPRINKLER as TYPE_SPRINKLER, TYPE_VALVE as TYPE_VALVE
from .util import cleanup_name_for_homekit as cleanup_name_for_homekit
from _typeshed import Incomplete
from homeassistant.components import button as button, input_button as input_button
from homeassistant.components.input_select import ATTR_OPTIONS as ATTR_OPTIONS, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION
from homeassistant.components.switch import DOMAIN as DOMAIN
from homeassistant.components.vacuum import SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_START as SERVICE_START, STATE_CLEANING as STATE_CLEANING, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_TYPE as CONF_TYPE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.event import async_call_later as async_call_later
from pyhap.characteristic import Characteristic as Characteristic
from typing import Any, NamedTuple

_LOGGER: Incomplete

class ValveInfo(NamedTuple):
    category: int
    valve_type: int

VALVE_TYPE: dict[str, ValveInfo]
ACTIVATE_ONLY_SWITCH_DOMAINS: Incomplete
ACTIVATE_ONLY_RESET_SECONDS: int

class Outlet(HomeAccessory):
    char_on: Incomplete
    char_outlet_in_use: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def set_state(self, value: bool) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class Switch(HomeAccessory):
    activate_only: Incomplete
    char_on: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def is_activate(self, state: State) -> bool: ...
    def reset_switch(self, *args: Any) -> None: ...
    def set_state(self, value: bool) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class Vacuum(Switch):
    def set_state(self, value: bool) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class Valve(HomeAccessory):
    category: Incomplete
    char_active: Incomplete
    char_in_use: Incomplete
    char_valve_type: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def set_state(self, value: bool) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...

class SelectSwitch(HomeAccessory):
    domain: Incomplete
    select_chars: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def select_option(self, option: str) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...
