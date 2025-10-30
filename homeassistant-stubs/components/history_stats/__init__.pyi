from .const import CONF_DURATION as CONF_DURATION, CONF_END as CONF_END, CONF_START as CONF_START, PLATFORMS as PLATFORMS
from .coordinator import HistoryStatsUpdateCoordinator as HistoryStatsUpdateCoordinator
from .data import HistoryStats as HistoryStats
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device import async_entity_id_to_device_id as async_entity_id_to_device_id, async_remove_stale_devices_links_keep_entity_device as async_remove_stale_devices_links_keep_entity_device
from homeassistant.helpers.helper_integration import async_handle_source_entity_changes as async_handle_source_entity_changes, async_remove_helper_config_entry_from_source_device as async_remove_helper_config_entry_from_source_device
from homeassistant.helpers.template import Template as Template

type HistoryStatsConfigEntry = ConfigEntry[HistoryStatsUpdateCoordinator]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HistoryStatsConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HistoryStatsConfigEntry) -> bool: ...
