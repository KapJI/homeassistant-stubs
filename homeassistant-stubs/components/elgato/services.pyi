from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

SERVICE_IDENTIFY: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
