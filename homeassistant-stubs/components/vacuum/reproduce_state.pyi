from . import ATTR_FAN_SPEED as ATTR_FAN_SPEED, DOMAIN as DOMAIN, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_SET_FAN_SPEED as SERVICE_SET_FAN_SPEED, SERVICE_START as SERVICE_START, SERVICE_STOP as SERVICE_STOP, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_RETURNING as STATE_RETURNING
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Iterable

VALID_STATES_TOGGLE: Any
VALID_STATES_STATE: Any

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
