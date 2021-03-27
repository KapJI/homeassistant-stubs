from . import DOMAIN as DOMAIN
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_CURRENT_TILT_POSITION as ATTR_CURRENT_TILT_POSITION, ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Dict, Iterable, Optional

VALID_STATES: Any

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Optional[Context]=..., reproduce_options: Optional[Dict[str, Any]]=...) -> None: ...
