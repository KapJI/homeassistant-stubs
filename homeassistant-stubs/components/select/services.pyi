from .const import ATTR_CYCLE as ATTR_CYCLE, DATA_COMPONENT as DATA_COMPONENT, SERVICE_SELECT_FIRST as SERVICE_SELECT_FIRST, SERVICE_SELECT_LAST as SERVICE_SELECT_LAST, SERVICE_SELECT_NEXT as SERVICE_SELECT_NEXT, SERVICE_SELECT_PREVIOUS as SERVICE_SELECT_PREVIOUS
from homeassistant.const import ATTR_OPTION as ATTR_OPTION, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
