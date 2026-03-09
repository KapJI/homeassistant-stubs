from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.typing import VolDictType as VolDictType

ATTR_KEYWORD: str
SERVICE_SEARCH: str
SEARCH_SCHEMA: VolDictType

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
