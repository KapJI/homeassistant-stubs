from .const import DOMAIN as DOMAIN, MAX_TIME_BETWEEN_UPDATES as MAX_TIME_BETWEEN_UPDATES
from .coordinator import SensorPushCloudConfigEntry as SensorPushCloudConfigEntry, SensorPushCloudCoordinator as SensorPushCloudCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfLength as UnitOfLength, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

ATTR_ALTITUDE: Final[str]
ATTR_ATMOSPHERIC_PRESSURE: Final[str]
ATTR_BATTERY_VOLTAGE: Final[str]
ATTR_DEWPOINT: Final[str]
ATTR_HUMIDITY: Final[str]
ATTR_SIGNAL_STRENGTH: Final[str]
ATTR_VAPOR_PRESSURE: Final[str]
PARALLEL_UPDATES: int
SENSORS: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: SensorPushCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SensorPushCloudSensor(CoordinatorEntity[SensorPushCloudCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SensorPushCloudCoordinator, entity_description: SensorEntityDescription, device_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
