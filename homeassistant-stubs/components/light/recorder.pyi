from . import ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_MAX_COLOR_TEMP_KELVIN as ATTR_MAX_COLOR_TEMP_KELVIN, ATTR_MAX_MIREDS as ATTR_MAX_MIREDS, ATTR_MIN_COLOR_TEMP_KELVIN as ATTR_MIN_COLOR_TEMP_KELVIN, ATTR_MIN_MIREDS as ATTR_MIN_MIREDS, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
