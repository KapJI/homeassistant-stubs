from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

ATTR_DURATION: str
ATTR_TARGET_TEMPERATURE: str
ATTR_FAN_DURATION: str
SERVICE_START_SESSION: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
