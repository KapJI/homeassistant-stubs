from . import ATTR_AUTO as ATTR_AUTO, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ORDER as ATTR_ORDER
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
