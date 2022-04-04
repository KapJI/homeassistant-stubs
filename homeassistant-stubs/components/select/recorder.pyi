from . import ATTR_OPTIONS as ATTR_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
