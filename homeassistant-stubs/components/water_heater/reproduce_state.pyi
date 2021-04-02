from . import ATTR_AWAY_MODE as ATTR_AWAY_MODE, ATTR_OPERATION_MODE as ATTR_OPERATION_MODE, ATTR_TEMPERATURE as ATTR_TEMPERATURE, DOMAIN as DOMAIN, SERVICE_SET_AWAY_MODE as SERVICE_SET_AWAY_MODE, SERVICE_SET_OPERATION_MODE as SERVICE_SET_OPERATION_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE, STATE_ECO as STATE_ECO, STATE_ELECTRIC as STATE_ELECTRIC, STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_PERFORMANCE as STATE_PERFORMANCE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Iterable

VALID_STATES: Any

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...