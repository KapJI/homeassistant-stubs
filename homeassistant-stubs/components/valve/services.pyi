from .const import ATTR_POSITION as ATTR_POSITION, DATA_COMPONENT as DATA_COMPONENT, ValveEntityFeature as ValveEntityFeature
from homeassistant.const import SERVICE_CLOSE_VALVE as SERVICE_CLOSE_VALVE, SERVICE_OPEN_VALVE as SERVICE_OPEN_VALVE, SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION, SERVICE_STOP_VALVE as SERVICE_STOP_VALVE, SERVICE_TOGGLE as SERVICE_TOGGLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
