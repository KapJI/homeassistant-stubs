from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

PLATFORMS: Any
ATTR_SYSTEM_MODE: str
ATTR_SYSTEM_NAME: str
DEFAULT_ATTRIBUTION: str
DEFAULT_SCAN_INTERVAL: Any
CONFIG_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_register_new_bridge(hass: HomeAssistant, bridge: dict, entry: ConfigEntry) -> None: ...

class NotionEntity(CoordinatorEntity):
    _attr_device_class: Any
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_name: Any
    _attr_unique_id: Any
    _bridge_id: Any
    _sensor_id: Any
    _system_id: Any
    _task_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, task_id: str, sensor_id: str, bridge_id: str, system_id: str, name: str, device_class: str) -> None: ...
    @property
    def available(self) -> bool: ...
    async def _async_update_bridge_id(self) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
