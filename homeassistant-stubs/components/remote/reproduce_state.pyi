from . import DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Iterable

_LOGGER: Any
VALID_STATES: Any

async def _async_reproduce_state(hass: HomeAssistantType, state: State, *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
