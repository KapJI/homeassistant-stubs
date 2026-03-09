from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers import service as service

SERVICE_RAW_GET_POSITIONS: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
