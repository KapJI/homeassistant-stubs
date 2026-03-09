from .const import DOMAIN as DOMAIN
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

SERVICE_CALL_METHOD: str
SERVICE_CALL_QUERY: str
ATTR_PARAMETERS: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
