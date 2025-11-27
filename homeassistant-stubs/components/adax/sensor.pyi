from . import AdaxConfigEntry as AdaxConfigEntry
from .const import CONNECTION_TYPE as CONNECTION_TYPE, DOMAIN as DOMAIN, LOCAL as LOCAL
from .coordinator import AdaxCloudCoordinator as AdaxCloudCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(kw_only=True, frozen=True)
class AdaxSensorDescription(SensorEntityDescription):
    data_key: str

SENSORS: tuple[AdaxSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AdaxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AdaxSensor(CoordinatorEntity[AdaxCloudCoordinator], SensorEntity):
    entity_description: AdaxSensorDescription
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AdaxCloudCoordinator, entity_description: AdaxSensorDescription, device_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int | float | None: ...
