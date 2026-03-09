from .const import DOMAIN as DOMAIN, MOW as MOW, PARK as PARK
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

OVERRIDE_MODES: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
