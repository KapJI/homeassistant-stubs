from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_NAME as ATTR_COLOR_NAME, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_KELVIN as ATTR_KELVIN, ATTR_PROFILE as ATTR_PROFILE, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any, NamedTuple

_LOGGER: Incomplete
VALID_STATES: Incomplete
ATTR_GROUP: Incomplete
COLOR_GROUP: Incomplete

class ColorModeAttr(NamedTuple):
    parameter: str
    state_attr: str

COLOR_MODE_TO_ATTRIBUTE: Incomplete
DEPRECATED_GROUP: Incomplete
DEPRECATION_WARNING: str

def _color_mode_same(cur_state: State, state: State) -> bool: ...
async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
def check_attr_equal(attr1: Mapping, attr2: Mapping, attr_str: str) -> bool: ...
