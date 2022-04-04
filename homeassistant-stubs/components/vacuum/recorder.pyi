from . import ATTR_FAN_SPEED_LIST as ATTR_FAN_SPEED_LIST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
