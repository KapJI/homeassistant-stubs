from . import SynoApi as SynoApi
from .const import CONF_VOLUMES as CONF_VOLUMES, COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, DOMAIN as DOMAIN, ENTITY_UNIT_LOAD as ENTITY_UNIT_LOAD, SYNO_API as SYNO_API
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISKS as CONF_DISKS, DATA_MEGABYTES as DATA_MEGABYTES, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DATA_TERABYTES as DATA_TERABYTES, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

class SynologyDSMSensorEntityDescription(SensorEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

UTILISATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_VOL_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_DISK_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
INFORMATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMSensor(SynologyDSMBaseEntity, SensorEntity):
    entity_description: SynologyDSMSensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMSensorEntityDescription) -> None: ...

class SynoDSMUtilSensor(SynoDSMSensor):
    @property
    def native_value(self) -> Union[Any, None]: ...
    @property
    def available(self) -> bool: ...

class SynoDSMStorageSensor(SynologyDSMDeviceEntity, SynoDSMSensor):
    entity_description: SynologyDSMSensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMSensorEntityDescription, device_id: Union[str, None] = ...) -> None: ...
    @property
    def native_value(self) -> Union[Any, None]: ...

class SynoDSMInfoSensor(SynoDSMSensor):
    _previous_uptime: Incomplete
    _last_boot: Incomplete
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[Any, None]: ...
