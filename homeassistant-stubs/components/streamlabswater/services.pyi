from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsConfigEntry as StreamlabsConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import service as service

ATTR_AWAY_MODE: str
SERVICE_SET_AWAY_MODE: str
AWAY_MODE_AWAY: str
AWAY_MODE_HOME: str
CONF_LOCATION_ID: str
SET_AWAY_MODE_SCHEMA: Incomplete

def set_away_mode(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
