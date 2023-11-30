from .const import CONF_COORDINATOR as CONF_COORDINATOR, DOMAIN as DOMAIN
from .coordinator import FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant

def get_coordinator(hass: HomeAssistant, config_entry_id: str) -> FritzboxDataUpdateCoordinator: ...
