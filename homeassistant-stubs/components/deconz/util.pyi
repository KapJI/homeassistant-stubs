from . import DeconzConfigEntry as DeconzConfigEntry
from .const import DOMAIN as DOMAIN
from .hub import DeconzHub as DeconzHub
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def serial_from_unique_id(unique_id: str | None) -> str | None: ...
@callback
def get_master_hub(hass: HomeAssistant) -> DeconzHub: ...
