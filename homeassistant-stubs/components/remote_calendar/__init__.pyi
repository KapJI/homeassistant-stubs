from .const import DOMAIN as DOMAIN
from .coordinator import RemoteCalendarConfigEntry as RemoteCalendarConfigEntry, RemoteCalendarDataUpdateCoordinator as RemoteCalendarDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: RemoteCalendarConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RemoteCalendarConfigEntry) -> bool: ...
