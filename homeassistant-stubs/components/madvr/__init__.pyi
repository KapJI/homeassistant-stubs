from .coordinator import MadVRConfigEntry as MadVRConfigEntry, MadVRCoordinator as MadVRCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_handle_unload(coordinator: MadVRCoordinator) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: MadVRConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MadVRConfigEntry) -> bool: ...
