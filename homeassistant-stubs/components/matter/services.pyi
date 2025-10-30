from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

ATTR_DURATION: str
ATTR_EMERGENCY_BOOST: str
ATTR_TEMPORARY_SETPOINT: str
SERVICE_WATER_HEATER_BOOST: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
