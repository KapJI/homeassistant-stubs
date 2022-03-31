from .common import SynoApi as SynoApi
from .const import COORDINATOR_CAMERAS as COORDINATOR_CAMERAS, COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, COORDINATOR_SWITCHES as COORDINATOR_SWITCHES, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, EXCEPTION_DETAILS as EXCEPTION_DETAILS, EXCEPTION_UNKNOWN as EXCEPTION_UNKNOWN, PLATFORMS as PLATFORMS, SYNO_API as SYNO_API, SYSTEM_LOADED as SYSTEM_LOADED, SynologyDSMEntityDescription as SynologyDSMEntityDescription, UNDO_UPDATE_LISTENER as UNDO_UPDATE_LISTENER
from .service import async_setup_services as async_setup_services
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from synology_dsm.api.surveillance_station.camera import SynoCamera as SynoCamera
from typing import Any

CONFIG_SCHEMA: Any
ATTRIBUTION: str
_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class SynologyDSMBaseEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, dict[str, Any]]]]):
    entity_description: SynologyDSMEntityDescription
    unique_id: str
    _attr_attribution: Any
    _api: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity):
    _device_id: Any
    _device_name: Any
    _device_manufacturer: Any
    _device_model: Any
    _device_firmware: Any
    _device_type: Any
    _name: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription, device_id: Union[str, None] = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
