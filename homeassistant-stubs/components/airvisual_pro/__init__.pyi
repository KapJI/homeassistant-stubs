from .coordinator import AirVisualProConfigEntry as AirVisualProConfigEntry, AirVisualProCoordinator as AirVisualProCoordinator, AirVisualProData as AirVisualProData
from _typeshed import Incomplete
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirVisualProConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirVisualProConfigEntry) -> bool: ...
