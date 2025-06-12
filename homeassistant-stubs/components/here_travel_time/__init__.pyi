from .const import TRAVEL_MODE_PUBLIC as TRAVEL_MODE_PUBLIC
from .coordinator import HERERoutingDataUpdateCoordinator as HERERoutingDataUpdateCoordinator, HERETransitDataUpdateCoordinator as HERETransitDataUpdateCoordinator, HereConfigEntry as HereConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_MODE as CONF_MODE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HereConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: HereConfigEntry) -> bool: ...
