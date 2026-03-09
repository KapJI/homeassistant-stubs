from .const import DOMAIN as DOMAIN
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

ATTR_NAVIGATION: str
ATTR_CATEGORY: str
ATTR_ZONE: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
