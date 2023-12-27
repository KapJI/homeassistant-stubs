from . import ATTR_FAN_SPEED as ATTR_FAN_SPEED, DOMAIN as DOMAIN, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_SET_FAN_SPEED as SERVICE_SET_FAN_SPEED, SERVICE_START as SERVICE_START, SERVICE_STOP as SERVICE_STOP, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_RETURNING as STATE_RETURNING
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete
VALID_STATES_TOGGLE: Incomplete
VALID_STATES_STATE: Incomplete

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
