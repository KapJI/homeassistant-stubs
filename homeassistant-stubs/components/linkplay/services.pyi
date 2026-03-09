from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

SERVICE_PLAY_PRESET: str
ATTR_PRESET_NUMBER: str
SERVICE_PLAY_PRESET_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
