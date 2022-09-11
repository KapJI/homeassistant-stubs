from .const import ATTR_NEXT_EVENT as ATTR_NEXT_EVENT
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
