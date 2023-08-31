from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
