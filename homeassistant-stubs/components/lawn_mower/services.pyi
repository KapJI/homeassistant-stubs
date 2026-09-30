from .const import DATA_COMPONENT as DATA_COMPONENT, LawnMowerEntityFeature as LawnMowerEntityFeature, SERVICE_DOCK as SERVICE_DOCK, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_START_MOWING as SERVICE_START_MOWING, SERVICE_STOP as SERVICE_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
