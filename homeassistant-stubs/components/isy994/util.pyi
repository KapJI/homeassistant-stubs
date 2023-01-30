from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def _async_cleanup_registry_entries(hass: HomeAssistant, entry_id: str) -> None: ...
