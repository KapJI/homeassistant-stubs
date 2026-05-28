from .const import ATTR_DURATION as ATTR_DURATION, DOMAIN as DOMAIN, SERVICE_ACTIVATE_TIMER_MODE as SERVICE_ACTIVATE_TIMER_MODE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
