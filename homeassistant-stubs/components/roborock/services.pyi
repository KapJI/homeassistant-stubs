from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers import service as service

GET_MAPS_SERVICE_NAME: str
SET_VACUUM_GOTO_POSITION_SERVICE_NAME: str
GET_VACUUM_CURRENT_POSITION_SERVICE_NAME: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
