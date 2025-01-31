from .const import PLATFORMS as PLATFORMS
from .entry_manager import CrownstoneConfigEntry as CrownstoneConfigEntry, CrownstoneEntryManager as CrownstoneEntryManager
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: CrownstoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CrownstoneConfigEntry) -> bool: ...
async def async_update_listener(hass: HomeAssistant, entry: CrownstoneConfigEntry) -> None: ...
