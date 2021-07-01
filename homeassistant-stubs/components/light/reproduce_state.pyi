from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_NAME as ATTR_COLOR_NAME, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_KELVIN as ATTR_KELVIN, ATTR_PROFILE as ATTR_PROFILE, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ATTR_WHITE_VALUE as ATTR_WHITE_VALUE, ATTR_XY_COLOR as ATTR_XY_COLOR, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_HS as COLOR_MODE_HS, COLOR_MODE_RGB as COLOR_MODE_RGB, COLOR_MODE_RGBW as COLOR_MODE_RGBW, COLOR_MODE_RGBWW as COLOR_MODE_RGBWW, COLOR_MODE_UNKNOWN as COLOR_MODE_UNKNOWN, COLOR_MODE_WHITE as COLOR_MODE_WHITE, COLOR_MODE_XY as COLOR_MODE_XY, DOMAIN as DOMAIN
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from types import MappingProxyType
from typing import Any

_LOGGER: Any
VALID_STATES: Any
ATTR_GROUP: Any
COLOR_GROUP: Any
COLOR_MODE_TO_ATTRIBUTE: Any
DEPRECATED_GROUP: Any
DEPRECATION_WARNING: str

def _color_mode_same(cur_state: State, state: State) -> bool: ...
async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
def check_attr_equal(attr1: MappingProxyType, attr2: MappingProxyType, attr_str: str) -> bool: ...
