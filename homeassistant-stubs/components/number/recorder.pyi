from . import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_MODE as ATTR_MODE, ATTR_STEP as ATTR_STEP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
