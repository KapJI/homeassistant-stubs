from .const import DOMAIN as DOMAIN
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

SERVICE_SET_COVER_POSITION_AND_TILT: str
POSITION_MIN: int
POSITION_MAX: int

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
