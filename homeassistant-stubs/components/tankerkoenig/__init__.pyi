from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from .coordinator import TankerkoenigConfigEntry as TankerkoenigConfigEntry, TankerkoenigDataUpdateCoordinator as TankerkoenigDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TankerkoenigConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TankerkoenigConfigEntry) -> bool: ...
