from . import DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_LOCK as SERVICE_LOCK, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Dict, Iterable, Optional

VALID_STATES: Any

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Optional[Context]=..., reproduce_options: Optional[Dict[str, Any]]=...) -> None: ...
