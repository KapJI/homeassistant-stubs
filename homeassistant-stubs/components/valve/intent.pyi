from . import ATTR_POSITION as ATTR_POSITION, DOMAIN as DOMAIN
from homeassistant.const import SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

async def async_setup_intents(hass: HomeAssistant) -> None: ...
