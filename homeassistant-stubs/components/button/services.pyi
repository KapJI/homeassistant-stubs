from .const import DATA_COMPONENT as DATA_COMPONENT, SERVICE_PRESS as SERVICE_PRESS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
