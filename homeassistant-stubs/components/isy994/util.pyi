from .const import LOGGER as LOGGER
from .models import IsyConfigEntry as IsyConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def _async_cleanup_registry_entries(hass: HomeAssistant, entry: IsyConfigEntry) -> None: ...
