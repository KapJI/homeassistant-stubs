from . import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_MODE as ATTR_MODE, ATTR_PATTERN as ATTR_PATTERN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
