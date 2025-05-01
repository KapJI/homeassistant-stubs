from . import SynoApi as SynoApi
from .const import CONF_VOLUMES as CONF_VOLUMES, ENTITY_UNIT_LOAD as ENTITY_UNIT_LOAD
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMConfigEntry as SynologyDSMConfigEntry
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_DEVICES as CONF_DEVICES, CONF_DISKS as CONF_DISKS, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow

@dataclass(frozen=True, kw_only=True)
class SynologyDSMSensorEntityDescription(SensorEntityDescription, SynologyDSMEntityDescription): ...

UTILISATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_VOL_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
STORAGE_DISK_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
EXTERNAL_USB_DISK_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
EXTERNAL_USB_PARTITION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]
INFORMATION_SENSORS: tuple[SynologyDSMSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SynoDSMSensor(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator], SensorEntity):
    entity_description: SynologyDSMSensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMSensorEntityDescription) -> None: ...

class SynoDSMUtilSensor(SynoDSMSensor):
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

class SynoDSMStorageSensor(SynologyDSMDeviceEntity, SynoDSMSensor):
    entity_description: SynologyDSMSensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMSensorEntityDescription, device_id: str | None = None) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class SynoDSMExternalUSBSensor(SynologyDSMDeviceEntity, SynoDSMSensor):
    entity_description: SynologyDSMSensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMSensorEntityDescription, device_id: str | None = None) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class SynoDSMInfoSensor(SynoDSMSensor):
    _previous_uptime: str | None
    _last_boot: datetime | None
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
