from . import ATTR_MAX_TEMP as ATTR_MAX_TEMP, ATTR_MIN_TEMP as ATTR_MIN_TEMP, ATTR_OPERATION_LIST as ATTR_OPERATION_LIST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
