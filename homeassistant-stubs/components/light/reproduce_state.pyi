from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_NAME as ATTR_COLOR_NAME, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_KELVIN as ATTR_KELVIN, ATTR_PROFILE as ATTR_PROFILE, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE_VALUE as ATTR_WHITE_VALUE, ATTR_XY_COLOR as ATTR_XY_COLOR, DOMAIN as DOMAIN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from types import MappingProxyType
from typing import Any, Dict, Iterable, Optional

VALID_STATES: Any
ATTR_GROUP: Any
COLOR_GROUP: Any
DEPRECATED_GROUP: Any
DEPRECATION_WARNING: str

async def async_reproduce_states(hass: HomeAssistantType, states: Iterable[State], *, context: Optional[Context]=..., reproduce_options: Optional[Dict[str, Any]]=...) -> None: ...
def check_attr_equal(attr1: MappingProxyType, attr2: MappingProxyType, attr_str: str) -> bool: ...
