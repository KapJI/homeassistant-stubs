from .const import DATA_COMPONENT as DATA_COMPONENT
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
