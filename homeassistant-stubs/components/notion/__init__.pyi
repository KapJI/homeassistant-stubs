from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

PLATFORMS: Incomplete
ATTR_SYSTEM_MODE: str
ATTR_SYSTEM_NAME: str
DEFAULT_SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_register_new_bridge(hass: HomeAssistant, bridge: dict, entry: ConfigEntry) -> None: ...

class NotionEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _bridge_id: Incomplete
    _sensor_id: Incomplete
    _system_id: Incomplete
    _task_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, task_id: str, sensor_id: str, bridge_id: str, system_id: str, description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    def _async_update_bridge_id(self) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
