from . import ATTR_EVENT_TYPES as ATTR_EVENT_TYPES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
