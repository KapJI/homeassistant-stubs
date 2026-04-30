from .const import ATTR_COLOR_BW as ATTR_COLOR_BW, CBW as CBW, DOMAIN as DOMAIN, MOV as MOV
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

_ATTR_PRESET: str
_ATTR_PTZ_MOV: str
_ATTR_PTZ_TT: str
_DEFAULT_TT: float

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
