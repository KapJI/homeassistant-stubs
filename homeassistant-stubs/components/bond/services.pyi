from .const import DOMAIN as DOMAIN
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

ATTR_POWER_STATE: str
SERVICE_SET_FAN_SPEED_TRACKED_STATE: str
SERVICE_SET_POWER_TRACKED_STATE: str
SERVICE_SET_LIGHT_POWER_TRACKED_STATE: str
SERVICE_SET_LIGHT_BRIGHTNESS_TRACKED_STATE: str
SERVICE_START_INCREASING_BRIGHTNESS: str
SERVICE_START_DECREASING_BRIGHTNESS: str
SERVICE_STOP: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
