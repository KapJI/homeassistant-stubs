from .const import CONF_TRACKED_ENTITIES as CONF_TRACKED_ENTITIES
from .coordinator import ProximityConfigEntry as ProximityConfigEntry, ProximityDataUpdateCoordinator as ProximityDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event, async_track_state_change_event as async_track_state_change_event

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ProximityConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ProximityConfigEntry) -> bool: ...
