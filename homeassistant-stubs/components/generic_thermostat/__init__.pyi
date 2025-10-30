from .const import CONF_HEATER as CONF_HEATER, CONF_SENSOR as CONF_SENSOR, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.device import async_entity_id_to_device_id as async_entity_id_to_device_id, async_remove_stale_devices_links_keep_entity_device as async_remove_stale_devices_links_keep_entity_device
from homeassistant.helpers.event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from homeassistant.helpers.helper_integration import async_handle_source_entity_changes as async_handle_source_entity_changes, async_remove_helper_config_entry_from_source_device as async_remove_helper_config_entry_from_source_device

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
