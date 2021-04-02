from . import ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Iterable

_LOGGER: Any

async def _async_reproduce_state(hass: HomeAssistantType, state: State, *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Union[Context, None]=..., reproduce_options: Union[dict[str, Any], None]=...) -> None: ...
