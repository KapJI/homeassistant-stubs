from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_LOCK_CURRENT_STATE as CHAR_LOCK_CURRENT_STATE, CHAR_LOCK_TARGET_STATE as CHAR_LOCK_TARGET_STATE, SERV_LOCK as SERV_LOCK
from _typeshed import Incomplete
from homeassistant.components.lock import DOMAIN as DOMAIN, STATE_JAMMED as STATE_JAMMED, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import State as State, callback as callback
from typing import Any

_LOGGER: Incomplete
HASS_TO_HOMEKIT_CURRENT: Incomplete
HASS_TO_HOMEKIT_TARGET: Incomplete
VALID_TARGET_STATES: Incomplete
HOMEKIT_TO_HASS: Incomplete
STATE_TO_SERVICE: Incomplete

class Lock(HomeAccessory):
    _code: Incomplete
    char_current_state: Incomplete
    char_target_state: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def set_state(self, value: int) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...
