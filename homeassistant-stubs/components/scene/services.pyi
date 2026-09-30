from .const import DATA_COMPONENT as DATA_COMPONENT
from homeassistant.components.light import ATTR_TRANSITION as ATTR_TRANSITION
from homeassistant.const import SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
