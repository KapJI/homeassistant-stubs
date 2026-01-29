from .coordinator import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: JVCConfigEntry) -> bool: ...
async def async_migrate_entities(hass: HomeAssistant, config_entry: JVCConfigEntry, coordinator: JvcProjectorDataUpdateCoordinator) -> None: ...
