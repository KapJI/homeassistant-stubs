from . import ATTR_PERCENTAGE as ATTR_PERCENTAGE, DOMAIN as DOMAIN, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import intent as intent

INTENT_FAN_SET_SPEED: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...
