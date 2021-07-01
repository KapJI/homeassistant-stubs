from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, CONF_SERIAL as CONF_SERIAL, CONF_VOLUMES as CONF_VOLUMES, COORDINATOR_CAMERAS as COORDINATOR_CAMERAS, COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, COORDINATOR_SWITCHES as COORDINATOR_SWITCHES, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_USE_SSL as DEFAULT_USE_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, ENTITY_CLASS as ENTITY_CLASS, ENTITY_ENABLE as ENTITY_ENABLE, ENTITY_ICON as ENTITY_ICON, ENTITY_NAME as ENTITY_NAME, ENTITY_UNIT as ENTITY_UNIT, EntityInfo as EntityInfo, PLATFORMS as PLATFORMS, SERVICES as SERVICES, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_SHUTDOWN as SERVICE_SHUTDOWN, STORAGE_DISK_BINARY_SENSORS as STORAGE_DISK_BINARY_SENSORS, STORAGE_DISK_SENSORS as STORAGE_DISK_SENSORS, STORAGE_VOL_SENSORS as STORAGE_VOL_SENSORS, SYNO_API as SYNO_API, SYSTEM_LOADED as SYSTEM_LOADED, UNDO_UPDATE_LISTENER as UNDO_UPDATE_LISTENER, UTILISATION_SENSORS as UTILISATION_SENSORS
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_DISKS as CONF_DISKS, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from synology_dsm.api.dsm.network import SynoDSMNetwork as SynoDSMNetwork
from synology_dsm.api.surveillance_station.camera import SynoCamera as SynoCamera
from typing import Any, Callable

CONFIG_SCHEMA: Any
ATTRIBUTION: str
_LOGGER: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def _async_setup_services(hass: HomeAssistant) -> None: ...

class SynoApi:
    _hass: Any
    _entry: Any
    dsm: Any
    information: Any
    network: Any
    security: Any
    storage: Any
    surveillance_station: Any
    system: Any
    upgrade: Any
    utilisation: Any
    _fetching_entities: Any
    _with_information: bool
    _with_security: bool
    _with_storage: bool
    _with_surveillance_station: bool
    _with_system: bool
    _with_upgrade: bool
    _with_utilisation: bool
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    def subscribe(self, api_key: str, unique_id: str) -> Callable[[], None]: ...
    def _async_setup_api_requests(self) -> None: ...
    def _fetch_device_configuration(self) -> None: ...
    async def async_reboot(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def async_unload(self) -> None: ...
    async def async_update(self, now: Union[timedelta, None] = ...) -> None: ...

class SynologyDSMBaseEntity(CoordinatorEntity):
    _api: Any
    _api_key: Any
    entity_type: Any
    _name: Any
    _class: Any
    _enable_default: Any
    _icon: Any
    _unit: Any
    _unique_id: Any
    def __init__(self, api: SynoApi, entity_type: str, entity_info: EntityInfo, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]]) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity):
    _device_id: Any
    _device_name: Any
    _device_manufacturer: Any
    _device_model: Any
    _device_firmware: Any
    _device_type: Any
    _name: Any
    def __init__(self, api: SynoApi, entity_type: str, entity_info: EntityInfo, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], device_id: Union[str, None] = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
