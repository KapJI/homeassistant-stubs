from . import ATTR_CUR as ATTR_CUR, ATTR_LAST_TRIGGERED as ATTR_LAST_TRIGGERED, ATTR_MAX as ATTR_MAX, ATTR_MODE as ATTR_MODE, CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
