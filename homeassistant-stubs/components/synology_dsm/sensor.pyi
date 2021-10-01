from . import SynoApi as SynoApi, SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity
from .const import CONF_VOLUMES as CONF_VOLUMES, COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, DOMAIN as DOMAIN, ENTITY_UNIT_LOAD as ENTITY_UNIT_LOAD, INFORMATION_SENSORS as INFORMATION_SENSORS, STORAGE_DISK_SENSORS as STORAGE_DISK_SENSORS, STORAGE_VOL_SENSORS as STORAGE_VOL_SENSORS, SYNO_API as SYNO_API, SynologyDSMSensorEntityDescription as SynologyDSMSensorEntityDescription, UTILISATION_SENSORS as UTILISATION_SENSORS
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISKS as CONF_DISKS, DATA_MEGABYTES as DATA_MEGABYTES, DATA_RATE_KILOBYTES_PER_SECOND as DATA_RATE_KILOBYTES_PER_SECOND, DATA_TERABYTES as DATA_TERABYTES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

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
    _previous_uptime: Any
    _last_boot: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[Any, None]: ...
