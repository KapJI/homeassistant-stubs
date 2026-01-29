from .const import BEOLINK_JOIN_SOURCES as BEOLINK_JOIN_SOURCES, DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
