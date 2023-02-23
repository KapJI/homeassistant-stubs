from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, ATTR_EVENT_SCORE as ATTR_EVENT_SCORE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
