from .const import DOMAIN as DOMAIN
from homeassistant.components.climate import ClimateEntityFeature as ClimateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

SERVICE_SET_FAN_TIMER: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
